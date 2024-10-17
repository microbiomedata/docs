# This script modifies a copy of the `mkdocs.yml` configuration file residing in the `nmdc-runtime` repository.

from typing import List
import argparse
import re
from io import StringIO

import yaml

# TODO: Write some tests that target this code.

# This is the value you want the `site_url` YAML field to contain.
SITE_URL = r"https://microbiomedata.github.io/docs/nmdc-runtime-documentation/"


def sanitize_yaml_lines(raw_lines: List[str]):
    r"""Helper function that wraps a specific value in quotes so PyYAML can parse it."""

    sanitized_lines = []
    for line in raw_lines:
        matches = re.match(
            r"^(\s*)(format):\s*(!!python/name:pymdownx\.superfences\.fence_code_format)\s*$",
            line,
        )
        if matches is not None:
            spaces = matches[1]
            label = matches[2]
            value = matches[3]
            sanitized_line = f'{spaces}{label}: "{value}"'
        else:
            sanitized_line = line
        sanitized_lines.append(sanitized_line)
    return sanitized_lines


def main():
    r"""
    Modifies a MkDocs configuration file so it can be used to build a website that will be hosted at a different URL
    from the URL the file currently lists.
    """

    parser = argparse.ArgumentParser(
        description="Modify the `mkdocs.yml` file from `nmdc-runtime`"
    )
    parser.add_argument(
        "input_file_path", type=argparse.FileType("r"), help="Path to `mkdocs.yml` file"
    )
    parser.add_argument(
        "output_file_path", type=argparse.FileType("w"), help="Path to output file"
    )
    args = parser.parse_args()

    # Read the input file, parsing its contents as YAML.
    print(f"Parsing original YAML file: {args.input_file_path.name}")
    with open(args.input_file_path.name, "r") as f:
        # Note: When I used `safe_load()` or I used `load()` with `Loader=yaml.SafeLoader`, Python raised this error:
        #       ```
        #       yaml.constructor.ConstructorError: could not determine a constructor for the tag
        #       'tag:yaml.org,2002:python/name:pymdownx.superfences.fence_code_format'
        #       ```
        #       So, I first modify the relevant line of the YAML file, putting quotes around its value,
        #       since PyYAML seems to load the result OK.
        #
        raw_lines = f.readlines()
        sanitized_lines = sanitize_yaml_lines(raw_lines)
        stream = StringIO("\n".join(sanitized_lines))
        mkdocs_config: dict = yaml.safe_load(stream)

    # Replace the `site_url` value.
    # Note: MkDocs incorporates this value into "canonical" URLs in the HTML `<head>` section.
    #       Reference: https://www.mkdocs.org/user-guide/configuration/#site_url
    # TODO: Make the value configurable (e.g. via a script argument or environment variable).
    print("Replacing site-specific values.")
    mkdocs_config["site_url"] = SITE_URL

    print(f"Writing resulting YAML file: {args.output_file_path.name}")
    with open(args.output_file_path.name, "w") as f:
        yaml.safe_dump(mkdocs_config, f)
