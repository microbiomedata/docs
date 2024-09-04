Reads QC Workflow (v1.0.1)
=============================

.. image:: ../_static/images/1_RQC_rqc_workflow.png
   :align: center
   :scale: 50%


Workflow Overview
-----------------

This workflow utilizes the program “rqcfilter2” from BBTools to perform quality control on raw Illumina reads. The workflow performs quality trimming, artifact removal, linker trimming, adapter trimming, and spike-in removal (using BBDuk), and performs human/cat/dog/mouse/microbe removal (using BBMap).

Workflow Availability
---------------------

The workflow from GitHub uses all the listed docker images to run all third-party tools.
The workflow is available in GitHub: https://github.com/microbiomedata/ReadsQC; the corresponding
Docker image is available in DockerHub: https://hub.docker.com/r/microbiomedata/bbtools.

Requirements for Execution 
--------------------------

(recommendations are in **bold**) 

- WDL-capable Workflow Execution Tool (**Cromwell**)
- Container Runtime that can load Docker images (**Docker v2.1.0.3 or higher**) 

Hardware Requirements
---------------------

- Disk space: 106 GB for the RQCFilterData database 
- Memory: >40 GB RAM


Workflow Dependencies
---------------------

Third party software (This is included in the Docker image.)  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `BBTools v38.90 <https://jgi.doe.gov/data-and-tools/bbtools/>`_ (License: `BSD-3-Clause-LBNL <https://bitbucket.org/berkeleylab/jgi-bbtools/src/master/license.txt>`_)

Requisite database
~~~~~~~~~~~~~~~~~~

The RQCFilterData Database must be downloaded and installed. This is a 106 GB tar file which includes reference datasets of artifacts, adapters, contaminants, the phiX genome, and some host genomes.  

The following commands will download the database:: 

    mkdir refdata
    wget http://portal.nersc.gov/dna/microbial/assembly/bushnell/RQCFilterData.tar
    tar -xvf RQCFilterData.tar -C refdata
    rm RQCFilterData.tar	

Sample dataset(s)
-----------------

Zymobiomics mock-community DNA control (`SRR7877884 <https://www.ebi.ac.uk/ena/browser/view/SRR7877884>`_); the original gzipped dataset is ~4 GB. 


.. note::

    If the input data is paired-end data, it must be in interleaved format. The following command will interleave the files, using the above dataset as an example:
    
.. code-block:: bash    

    paste <(zcat SRR7877884_1.fastq.gz | paste - - - -) <(zcat SRR7877884_2.fastq.gz | paste - - - -) | tr '\t' '\n' | gzip -c > SRR7877884-int.fastq.gz
    
For testing purposes and for the following examples, we used a 10% sub-sampling of the above dataset: `SRR7877884-int-0.1.fastq.gz <https://portal.nersc.gov/cfs/m3408/test_data/SRR7877884-int-0.1.fastq.gz>`_. This dataset is already interleaved.

Inputs
------

A JSON file containing the following information: 

1.	the path to the database
2.	the path to the interleaved fastq file (input data) 
3.	the path to the output directory
4.	(optional) parameters for memory 
5.	(optional) number of threads requested


An example input JSON file is shown below:

.. code-block:: JSON

    {
        "jgi_rqcfilter.database": "/path/to/refdata",
        "jgi_rqcfilter.input_files": [
            "/path/to/SRR7877884-int-0.1.fastq.gz "
        ],
        "jgi_rqcfilter.outdir": "/path/to/rqcfiltered",
        "jgi_rqcfilter.memory": "35G",
        "jgi_rqcfilter.threads": "16"
    }

.. note::

    In an HPC environment, parallel processing allows for processing multiple samples. The "jgi_rqcfilter.input_files" parameter is an array data structure. It can be used for multiple samples as input separated by a comma (,).
    Ex: "jgi_rqcfilter.input_files":[“first-int.fastq”,”second-int.fastq”]


Output
------

A directory named with the prefix of the FASTQ input file will be created and multiple output files are generated; the main QC FASTQ output is named prefix.anqdpht.fastq.gz. Using the dataset above as an example, the main output would be named SRR7877884-int-0.1.anqdpht.fastq.gz. Other files include statistics on the quality of the data; what was trimmed, detected, and filtered in the data; a status log, and a shell script documenting the steps implemented so the workflow can be reproduced.

Part of an example output JSON file is shown below:
   
.. code-block:: bash    
    
    SRR7877884-int-0.1
    |-- SRR7877884-int-0.1.anqdpht.fastq.gz
    |-- filterStats.txt
    |-- filterStats.json
    |-- filterStats2.txt
    |-- adaptersDetected.fa
    |-- reproduce.sh
    |-- spikein.fq.gz
    |-- status.log
    |-- ...


Below is an example of all the output directory files with descriptions to the right.

==================================== ============================================================================
FileName                              Description
==================================== ============================================================================
SRR7877884-int-0.1.anqdpht.fastq.gz   main output (clean data)       
adaptersDetected.fa                   adapters detected and removed        
bhist.txt                             base composition histogram by position 
cardinality.txt                       estimation of the number of unique kmers 
commonMicrobes.txt                    detected common microbes 
file-list.txt                         output file list for rqcfilter2.sh 
filterStats.txt                       summary statistics 
filterStats.json                      summary statistics in JSON format 
filterStats2.txt                      more detailed summary statistics 
gchist.txt                            GC content histogram 
human.fq.gz                           detected human sequence reads 
ihist_merge.txt                       insert size histogram 
khist.txt                             kmer-frequency histogram 
kmerStats1.txt                        synthetic molecule (phix, linker, lamda, pJET) filter run log  
kmerStats2.txt                        synthetic molecule (short contamination) filter run log 
ktrim_kmerStats1.txt                  detected adapters filter run log 
ktrim_scaffoldStats1.txt              detected adapters filter statistics 
microbes.fq.gz                        detected common microbes sequence reads 
microbesUsed.txt                      common microbes list for detection 
peaks.txt                             number of unique kmers in each peak on the histogram 
phist.txt                             polymer length histogram 
refStats.txt                          human reads filter statistics 
reproduce.sh                          the shell script to reproduce the run
scaffoldStats1.txt                    detected synthetic molecule (phix, linker, lamda, pJET) statistics 
scaffoldStats2.txt                    detected synthetic molecule (short contamination) statistics 
scaffoldStatsSpikein.txt              detected skipe-in kapa tag statistics 
sketch.txt                            mash type sketch scanned result against nt, refseq, silva database sketches.  
spikein.fq.gz                         detected skipe-in kapa tag sequence reads 
status.log                            rqcfilter2.sh running log 
synth1.fq.gz                          detected synthetic molecule (phix, linker, lamda, pJET) sequence reads 
synth2.fq.gz                          detected synthetic molecule (short contamination) sequence reads 
==================================== ============================================================================


Version History
---------------

- 1.0.1 (release date **02/16/2021**; previous versions: 1.0.0)


Point of contact
----------------

- Original author: Brian Bushnell <bbushnell@lbl.gov>

- Package maintainer: Chienchi Lo <chienchi@lanl.gov>

