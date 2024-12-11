Metagenomic Workflow 
================================================

.. image:: ./metag_workflow2024.svg
   :align: center

Workflow Overview
-----------------
The NMDC standardized metagenome workflow leverages parts of JGI's production pipeline for short-read data and consists of: `reads quality control (QC) <https://github.com/microbiomedata/ReadsQC>`_, `metagenome assembly <https://github.com/microbiomedata/metaAssembly>`_, `metagenome annotation <https://github.com/microbiomedata/mg_annotation>`_, `read-based taxonomy <https://github.com/microbiomedata/ReadbasedAnalysis>`_, and binning of population genomes to `generate metagenome-assembled genomes (MAGs) <https://github.com/microbiomedata/metaMAGs>`_ workflows.

The reads QC workflow utilizes rqcfilter2 to trim and filter low quality data from raw metagenome Illumina reads (FASTQ files). The workflow additionally removes artifacts, linkers, adapters, spike-in reads, and reads mapping to several hosts and common contaminants.

The read-based taxonomy classification workflow utilizes GOTTCHA2, Kraken2, and Centrifuge to profile quality-controlled reads to accommodate varied project goals and sequencing approaches that cover a spectrum from high sensitivity to high specificity that is dependent on the algorithms and cut-off levels chosen from different tools. 

The metagenome assembly workflow uses bbcms, metaSPAdes, and BBMap to run error correction, assembly, and assembly validation, respectively. The metagenome annotation workflow takes in assembled metagenomes and generates structural and functional annotations. The MAGs workflow uses MetaBAT 2 to generate metagenome bins and applies the MIMAG standards using annotated tRNAs, rRNAs, and marker genes with checkM to estimate completeness and contamination and subsequent taxonomic lineage assignment.

Users can run a single workflow within the metagenome pipeline with the appropriate input files, but the entire metagenome workflow is available to run from start to finish on NMDC EDGE from a single input raw Illumina file.


Workflow Availability
---------------------
The workflow is available in its individual components on GitHub and as a whole to run on `NMDC EDGE <https://nmdc-edge.org/home>`_. 

- `ReadsQC <https://github.com/microbiomedata/ReadsQC>`_ 
- `MetaAssembly <https://github.com/microbiomedata/metaAssembly>`_
- `MG Annotation <https://github.com/microbiomedata/mg_annotation>`_
- `MetaMAGs <https://github.com/microbiomedata/metaMAGs>`_ 
- `Read-based Taxonomy <https://github.com/microbiomedata/ReadbasedAnalysis>`_


Requirements for Execution outside `NMDC EDGE <nmdc-edge.org>`_:  
~~~~~~~~~~~~~~~~~~~~~~~~~~~

(recommendations are in **bold**)

- WDL-capable Workflow Execution Tool (**Cromwell**)
- Container Runtime that can load Docker images (**Docker v2.1.0.3 or higher**)

Hardware Requirements:
~~~~~~~~~~~~~~~~~~~~~~
- Disk space: 258 GB for databases 
- 86 GB RAM

Workflow Dependencies
---------------------

Third-party software:
~~~~~~~~~~~~~~~~~~~~~

Docker images containing third-party software are available in the respective repositories. More information is available in the workflow repositories listed above. 

- `microbiomedata/bbtools:38.96 <https://hub.docker.com/r/microbiomedata/bbtools>`_
- `bryce911/smrtlink:12.0.0.177059 <https://hub.docker.com/r/bryce911/smrtlink>`_
- `staphb/racon:1.4.20 <https://hub.docker.com/r/staphb/racon>`_
- `staphb/minimap2:2.25 <https://hub.docker.com/r/staphb/minimap2>`_
- `staphb/samtools:1.18 <https://hub.docker.com/r/staphb/samtools>`_
- `staphb/spades:4.0.0 <https://hub.docker.com/r/staphb/spades>`_
- `microbiomedata/img-omics:5.2.0 <https://hub.docker.com/r/microbiomedata/img-omics>`_
- `microbiomedata/nmdc_mbin <https://hub.docker.com/r/microbiomedata/nmdc_mbin>`_
- `microbiomedata/nmdc_mbin_vis:0.7.0 <https://hub.docker.com/r/microbiomedata/nmdc_mbin_vis>`_



Sample dataset(s):
~~~~~~~~~~~~~~~~~~

- Soil microbial communities from the East River watershed near Crested Butte, Colorado, United States - ER_DNA_379 metagenome (`SRR8553641 <https://www.ncbi.nlm.nih.gov/sra/SRX5355418>`) with `metadata available in the NMDC Data Portal <https://data.microbiomedata.org/details/study/nmdc:sty-11-dcqce727>`_. This dataset has 18.3G bases

  - The zipped raw fastq file is available `here <https://portal.nersc.gov/cfs/m3408/test_data/SRR8553641/SRR8553641.fastq.gz>`_

- Zymobiomics mock-community DNA control (`SRR7877884 <https://www.ncbi.nlm.nih.gov/sra/SRX4716743>`_); this `dataset <https://portal.nersc.gov/cfs/m3408/test_data/SRR7877884/>`_ is has 6.7G bases.

  - The non-interleaved raw fastq files are available as `R1 <https://portal.nersc.gov/cfs/m3408/test_data/SRR7877884/SRR7877884_1.fastq.gz>`_ and `R2 <https://portal.nersc.gov/cfs/m3408/test_data/SRR7877884/SRR7877884_2.fastq.gz>`
  - The interleaved file is `here <https://portal.nersc.gov/cfs/m3408/test_data/SRR7877884/SRR7877884-int.fastq.gz>`_
  - A 10% subset of the interleaved file is available as a quick dataset `here <https://portal.nersc.gov/cfs/m3408/test_data/SRR7877884/SRR7877884-int-0.1.fastq.gz>`



Input: 
~~~~~~~~~~~~~~~~~~~~

To run the full workflow via NMDC EDGE web UI, the following inputs are needed: 

#. Project/Run Name
#. Is interleaved (boolean)
#. Interleaved fastq(s), (FASTQ #1; FASTQ #2...)
#. If non-interleaved paired-end reads, Pair(FASTQ R1, FASTQ R2)...

To run individual workflows, see website or individual GitHub repositories. (See Workflow Availability links)


Output:
~~~~~~~
Upon completion of the run, the NMDC EDGE interface provides results grouped by individual workflow for viewing.

In addition to the workflow outputs are summary tables for each portion: 

- ReadsQC: statistics and metrics, including the number of reads and bases before and after QC filtering
- Read-based taxonomy: summary tables and interactive Krona plots as visual outputs
- Assembly: summary statistics table
- Annotation: statistics for processed sequences, predicted genes, and general quality information
- MAGs: summary section with information on binned and unbinned contigs, genome completeness, estimated contamination, and the number of genes present on all bins determined to be high quality or medium quality



Point of contact
----------------

- Workflow maintainers: Chienchi Lo <chienchi@lanl.gov>, Mark Flynn <mflynn@lanl.gov>
