#! /bin/bash

# Fetch individual workflow docs source directories (i.e. clone the repos in a way that downloads _only_ what we need).
#
# Note: Here, I'm using a combination of the technique described in https://stackoverflow.com/a/52269934 (i.e., cloning
#       without checking anything out, then doing a sparse checkout) and a technique described in
#       https://github.blog/open-source/git/get-up-to-speed-with-partial-clone-and-shallow-clone/ (i.e., cloning only a
#       specific branch, and only the latest commit—no deeper—on that branch). By using that combination of techniques,
#       we save time, bandwidth, and disk space. At the time of this writing, the result occupies less than 10% of the
#       disk space compared to normal clones.
#
mkdir -p /tmp/clones
git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/ReadsQC /tmp/clones/ReadsQC                     && cd /tmp/clones/ReadsQC           && git sparse-checkout set --no-cone /docs && git checkout
git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/ReadbasedAnalysis /tmp/clones/ReadbasedAnalysis && cd /tmp/clones/ReadbasedAnalysis && git sparse-checkout set --no-cone /docs && git checkout
git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/metaAssembly /tmp/clones/metaAssembly           && cd /tmp/clones/metaAssembly      && git sparse-checkout set --no-cone /docs && git checkout
git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/mg_annotation /tmp/clones/mg_annotation         && cd /tmp/clones/mg_annotation     && git sparse-checkout set --no-cone /docs && git checkout
git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/metaMAGs /tmp/clones/metaMAGs                   && cd /tmp/clones/metaMAGs          && git sparse-checkout set --no-cone /docs && git checkout
git clone --no-checkout --depth=1 --single-branch --branch=main   --filter=tree:0 https://github.com/microbiomedata/metaT /tmp/clones/metaT                         && cd /tmp/clones/metaT             && git sparse-checkout set --no-cone /docs && git checkout
git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/metaPro /tmp/clones/metaPro                     && cd /tmp/clones/metaPro           && git sparse-checkout set --no-cone /docs && git checkout
git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/metaMS /tmp/clones/metaMS                       && cd /tmp/clones/metaMS            && git sparse-checkout set --no-cone /docs && git checkout
git clone --no-checkout --depth=1 --single-branch --branch=master --filter=tree:0 https://github.com/microbiomedata/enviroMS /tmp/clones/enviroMS                   && cd /tmp/clones/enviroMS          && git sparse-checkout set --no-cone /docs && git checkout

# Arrange the "docs" directories into chapters.
mkdir -p /tmp/book/src/chapters
mv /tmp/clones/ReadsQC/docs           /tmp/book/src/chapters/1_RQC
mv /tmp/clones/ReadbasedAnalysis/docs /tmp/book/src/chapters/2_ReadAnalysis
mv /tmp/clones/metaAssembly/docs      /tmp/book/src/chapters/3_MetaGAssembly
mv /tmp/clones/mg_annotation/docs     /tmp/book/src/chapters/4_MetaGAnnotation
mv /tmp/clones/metaMAGs/docs          /tmp/book/src/chapters/5_MAG
mv /tmp/clones/metaT/docs             /tmp/book/src/chapters/6_MetaT
mv /tmp/clones/metaPro/docs           /tmp/book/src/chapters/7_Metaproteomics
mv /tmp/clones/metaMS/docs            /tmp/book/src/chapters/8_Metabolomics
mv /tmp/clones/enviroMS/docs          /tmp/book/src/chapters/9_NOM
