# This script modifies a copy of the `mkdocs.yml` configuration file residing in the `nmdc-runtime` repository.

from typing import List
import argparse
import re

import yaml

# TODO: Write some tests that target this code.

# This is the value you want the `site_url` YAML field to contain.
SITE_URL = r"https://microbiomedata.github.io/docs/nmdc-runtime-documentation/"


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
        mkdocs_config: dict = yaml.safe_load(f)

    # Replace the `site_url` value.
    # Note: MkDocs incorporates this value into "canonical" URLs in the HTML `<head>` section.
    #       Reference: https://www.mkdocs.org/user-guide/configuration/#site_url
    # TODO: Make the value configurable (e.g. via a script argument or environment variable).
    print("Replacing site-specific values.")
    mkdocs_config["site_url"] = SITE_URL

    print(f"Writing resulting YAML file: {args.output_file_path.name}")
    with open(args.output_file_path.name, "w") as f:
        yaml.safe_dump(mkdocs_config, f)
