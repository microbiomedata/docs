Metagenomic Workflow 
================================================

.. image:: metag_workflow2024.svg
   :align: center
   :scale: 25%

Workflow Overview
-----------------
The NMDC standardized metagenome workflow leverages parts of JGI's production pipeline for short-read data and consists of: `reads quality control (QC) <https://github.com/microbiomedata/ReadsQC>`_, `metagenome assembly <https://github.com/microbiomedata/metaAssembly>`_, `metagenome annotation <https://github.com/microbiomedata/mg_annotation>`_, `read-based taxonomy <https://github.com/microbiomedata/ReadbasedAnalysis>`_, and binning of population genomes to `generate metagenome-assembled genomes (MAGs) <https://github.com/microbiomedata/metaMAGs>`_ workflows.

The reads QC workflow utilizes rqcfilter2 to trim and filter low quality data from raw metagenome Illumina reads (FASTQ files). The workflow additionally removes artifacts, linkers, adapters, spike-in reads, and reads mapping to several hosts and common contaminants.

The read-based taxonomy classification workflow utilizes GOTTCHA2, Kraken2, and Centrifuge to profile quality-controlled reads to accommodate varied project goals and sequencing approaches that cover a spectrum from high sensitivity to high specificity that is dependent on the algorithms and cut-off levels chosen from different tools. 

The metagenome assembly workflow uses bbcms, metaSPAdes, and BBMap to run error correction, assembly, and assembly validation, respectively. The metagenome annotation workflow takes in assembled metagenomes and generates structural and functional annotations. The MAGs workflow uses metabat2 to generate metagenome bins and applies the MIMAG standards using annotated tRNAs, rRNAs, and marker genes with checkM to estimate completeness and contamination and subsequent taxonomic lineage assignment.

Users can run a single workflow within the metagenome pipeline with the appropriate input files, but the entire metagenome workflow is available to run from start to finish on NMDC EDGE from a single input raw Illumina file.


Workflow Availability
---------------------
The workflow is available in its individual components on GitHub and as a whole to run on `NMDC-EDGE <https://nmdc-edge.org/home>`_. 

- `ReadsQC <https://github.com/microbiomedata/ReadsQC>`_ 
- `MetaAssembly <https://github.com/microbiomedata/metaAssembly>`_
- `MG Annotation <https://github.com/microbiomedata/mg_annotation>`_
- `MetaMAGs <https://github.com/microbiomedata/metaMAGs>`_ 
- `Read-based Taxonomy <https://github.com/microbiomedata/ReadbasedAnalysis>`_


Requirements for Execution:  
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

Third party software:
~~~~~~~~~~~~~~~~~~~~~

Docker images containing third-party software are available in the repsective repositories. More information is available in the workflow repositories listed above. 

- `microbiomedata/bbtools:38.96 <https://hub.docker.com/r/microbiomedata/bbtools>`_
- `bryce911/smrtlink:12.0.0.177059`_
- `staphb/racon:1.4.20`_
- `staphb/minimap2:2.25`_
- `staphb/samtools:1.18`_
- `staphb/spades:4.0.0`_
- `microbiomedata/img-omics:5.2.0 <https://hub.docker.com/r/microbiomedata/img-omics>`_
- `microbiomedata/nmdc_mbin <https://hub.docker.com/r/microbiomedata/nmdc_mbin>`_
- `microbiomedata/nmdc_mbin_vis:0.7.0 <https://hub.docker.com/r/microbiomedata/nmdc_mbin_vis>`_



Sample dataset(s):
~~~~~~~~~~~~~~~~~~

Zymobiomics mock-community DNA control (SRR7877884); this dataset is ~7 GB.

Input: 
~~~~~~~~~~~~~~~~~~~~
A JSON file containing the following
#.	output file prefix
#.  path to :code:`input_file` if interleaved file
#.  paths to :code:`input_fq1` and :code:`input_fq2` non-interleaved paired-end reads 
#.	input_interleaved (boolean)
#.	RNA strand type (optional) either left blank, :code:`aRNA`, or :code:`non_stranded_RNA`


Output:
~~~~~~~
Upon completion of the run, the NMDC EDGE interface provides users can view the results, which are grouped by individual workflow. 

In addition to the workflow outputs are summary tables for each portion: 

- ReadsQC: statistics and metrics, including the number of reads and bases before and after QC filtering.
- Read-based taxonomy: summary tables and interactive Krona plots as visual outputs.
- Assembly: summary statistics
- Annotation: statistics for processed sequences, predicted genes, and general quality information
- MAGs: summary section with information on binned and unbinned contigs, genome completeness, estimated contamination, and the number of genes present on all bins determined to be high quality or medium quality.



Point of contact
----------------

- Package maintainers: Chienchi Lo <chienchi@lanl.gov>, Mark Flynn <mflynn@lanl.gov>
