import logging


def on_page_context(context, page, **kwargs):
    r"""
    Sets the `edit_url` of the page to the URL in the `edit_url` field of the page's YAML front matter.
    If the page doesn't have YAML front matter, or its YAML front matter doesn't have the `edit_url` field,
    this function don't do anything to that page.

    Usage: To override the `edit_url` of a given page, add the following YAML front matter
           to the top of the page's Markdown document:
           ```
           ---
           edit_url: https://www.example.com
           ---
           ```

    Note: The idea of using MkDocs hooks to achieve this came from the following PR:
          https://github.com/renovatebot/renovatebot.github.io/pull/187/files

    Note: The MkDocs plugin "events" (which dictate the name of this function) are depicted here:
          https://www.mkdocs.org/dev-guide/plugins/#events
    
    Note: The MkDocs development server (typically launched via `mkdocs serve`) will not
          automatically apply changes made to this function to the already-running server.
          In order to apply the changes, restart the MkDocs development server.

    References:
    - https://www.mkdocs.org/user-guide/configuration/#hooks
    """

    if "edit_url" in page.meta:
        edit_url_from_front_matter = page.meta["edit_url"]
        logging.warning(f"Overriding `edit_url` to be: {edit_url_from_front_matter}")
        page.edit_url = edit_url_from_front_matter

    return context
