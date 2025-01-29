=======
Runtime
=======

..
    Note: Visitors will not see this page. A redirect defined in `conf.py` will redirect them to `/runtime/` instead,
          and `/runtime/` is the path of the Runtime documentation "sub-site," not this page.

    You may be wondering — if visitors will be redirected away from this page — why this file exists in the first place.
    This file exists as a workaround for a limitation of Sphinx that has existed since at least 2015.

    Reference: https://github.com/sphinx-doc/sphinx/issues/701

    The gist is that, if this file did not exists, Sphinx would refuse to generate a link to `./runtime.html` in its
    table of contents (i.e. the `toctree` section of `index.rst`). Sphinx only generates ToC links for two types of
    targets: (a) pages that are part of the same Sphinx site, and (b) absolute URLs. Since (a) our Runtime
    documentation is part of a different, non-Sphinx site, and (b) we want to have the flexibility of deploying this
    website to different URLs (e.g. for production, for staging, for local development), we do the following:
    (a) leave this file here to so Sphinx will generate the ToC link, and (b) implement a redirect in `conf.py` so
    visitors never actually end up at this page. Whew!
