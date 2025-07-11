<!-- 
# ![Logo for NMDC EDGE product, a multicolored M and a square green graphic with EDGE](../_static/images/nmdc-edge-logo.png) -->
# NMDC EDGE Quick Start User Guide

## Setting Up

### Register for an account

1. Visit the homepage for NMDC EDGE platform by going to [https://nmdc-edge.org](https://nmdc-edge.org/home)
   ![Home page for NMDC EDGE with a bubble labeled 2 for the ORCiD LOGIN button](../_static/images/howto_guides/workflows/quickStart/03102025_login-in.png)
2. Click on "ORCiD LOGIN" to login to your account on the NMDC EDGE platform.  
   ![ORCiD login page with bubble labeled 3 for "Register now"](../_static/images/howto_guides/workflows/quickStart/03102025_orcid.png)
3. Log in to ORCiD using your registered credentials. If you do not have an ORCiD, click on "Register Now" and follow the instructions to set-up an ORCiD account.
   ![NMDC EDGE "My Profile" page with bubble labeled 4 for the highlighted "My Profile" button](../_static/images/howto_guides/workflows/quickStart/03102025_my_profile.png)
4. If you are logging in for the first time, click on "My Profile" and optionally provide your First Name, Last Name, and Email. The first grayed out box will already have your ORCiD. You can also set the "Project Status Notification" to ON (OFF by default). If ON, notifications about your workflow runs will be sent to the Email you provided. Click on "Save Changes"

### Upload data

You can upload your own data to process through the workflows. 
1. Click on "Upload Files" in the left menu bar. 
2. This will open a page which allows you to drag and drop files or browse for your data files. If you do not have a dataset to test, you can download this Illumina short-read metagenomic [test data](https://portal.nersc.gov/cfs/m3408/test_data/SRR7877884/SRR7877884-int-0.1.fastq.gz) (Illumina interleaved file) and upload it to the NMDC EDGE platform. 

!["Upload Files" page on NMDC EDGE, with a bubble labeled 1 pointing to the "Upload Files" tab in left vertical navigation bar, and a bubble labeled 2 under "Drag files or Click to Browse"](../_static/images/howto_guides/workflows/quickStart/03102025_upload_files.png)

Additionally, there are some datasets in the Public Data folder for you to test within the NMDC EDGE platform.


Alternatively, you can (1) select "Retrieve SRA Data" in the left menu bar and (2) input NCBI SRA accession number(s) to pull data directly from SRA. 

!["Retrieve SRA Data" page on NMDC EDGE, with a bubble labeled 1 pointing to the "Retrieve SRA Data" tab in left vertical navigation bar, and a bubble labeled 2 pointing to a text box for SRA accession number(s) entry](../_static/images/howto_guides/workflows/quickStart/03102025_retrieve_SRA.png)

---

##  Running the Workflows

One of the core end-to-end tools available to NMDC EDGE users is the Metagenomics workflow. It takes raw, short-read Illumina or long-read PacBio FASTQ files and runs the following workflows (linked to their respective GitHub repositories):

 - [ReadsQC](https://github.com/microbiomedata/ReadsQC) (reads quality control)
 - [Read-based Taxonomy](https://github.com/microbiomedata/ReadbasedAnalysis) (read-based taxonomic classification)
 - [MetaAssembly](https://github.com/microbiomedata/metaAssembly) (metagenome assembly)
 - [Viruses and Plasmids](https://portal.nersc.gov/genomad/) (virus and plasmid genome identification)
 - [MG Annotation](https://github.com/microbiomedata/mg_annotation) (metagenome annotation)
 - [MetaMAGs](https://github.com/microbiomedata/metaMAGs) (binning of population genomes to generate metagenome-assembled genomes)

More information on these metagenomic workflows is available in the [workflow documentation](https://docs.microbiomedata.org/workflows/chapters/1_Metagenome_Workflow_Overview/index.html). 

A summary of the workflows and link to their documentation is available in [this table](#workflow-summaries).

### Running the full metagenomic workflow for short-reads

In this example, we will run the interleaved FASTQ file for Zymobiomics mock-community DNA control ([SRR7877884](https://www.ncbi.nlm.nih.gov/sra/SRX4716743)), which is available in the public data folder in NMDC EDGE file section options (as `SRR7877884-int.fastq.gz`) and [online](https://portal.nersc.gov/cfs/m3408/test_data/SRR7877884/SRR7877884-int.fastq.gz). Note that this is a larger file at 3.65 GB. A smaller option (10% subset of SRR7877884) is available at 367.25 MB both in the public data folder (as `SRR7877884-int-0.1.fastq.gz`) and online as a [URL](https://portal.nersc.gov/cfs/m3408/test_data/SRR7877884/SRR7877884-int-0.1.fastq.gz). To copy the file URLs, right click (CTRL+Left Click on Mac) and select "Copy Link".

!["Run Multiple Workflows" submission page for short-reads with bubbles labeled 1 through 8 pointing at different clickable buttons and typeable fields](../_static/images/howto_guides/workflows/metaG/05302025_run_metag_short.png)


1. Click on the "Metagenomics" tab on the left vertical navigation bar. 
2. Select the "Run Multiple Workflows" option from the dropdown.
3.  Enter a unique Project/Run Name with no spaces (underscores are fine).
4.  Enter a description (optional, but recommended).
5.  Select if the input data is Illumina short-read or PacBio long-read (Illumina by default). Here, we will select Illumina.
6.  Select if the input data is interleaved (YES by default). If the data is paired select NO and it will allow you to upload both, forward and reverse files.
7.  Then select the input file(s). Clicking on the button to select "Interleaved FASTQ #1" opens a box called "Select a file" (as shown in the image below) to allow the user to find the desired files, either from the public data folder, or files uploaded by the user. If the files are uploaded to an accessible URL, the URL can be pasted into the box.
    ![A pop-up window titled "Select a file" over a grayed out background for the workflow submission page. It shows a file structure for public metagenomic test data.](../_static/images/howto_guides/workflows/metaG/05212025_run_metag_short_file.png)
8.  Click "Submit" to start a metagenome workflow run.

### Running the full metagenomic workflow for long-reads

In this example, we will run a PacBio file for a Zymobiomics synthetic metagenome SRR13128014, which is available in the public data folder in NMDC EDGE file section options (as `SRR13128014.pacbio.subsample.ccs.fastq.gz`) and [online](https://portal.nersc.gov/project/m3408//test_data/SRR13128014.pacbio.subsample.ccs.fastq.gz). Note that for testing we have subsampled the dataset, the original dataset is ~18GB.

!["Run Multiple Workflows" submission page with bubbles labeled 1 through 7 pointing at different clickable buttons and typeable fields](../_static/images/howto_guides/workflows/metaG/05222025_run_metag_long.png)


1. Click on the "Metagenomics" tab on the left vertical navigation bar. 
2. Select the "Run Multiple Workflows" option from the dropdown.
3.  Enter a unique Project/Run Name with no spaces (underscores are fine).
4.  Enter a description (optional, but recommended).
5.  Select if the input data is Illumina short-read or PacBio long-read (Illumina by default). Here, we will select PacBio.
6.  Then select the input file(s). Clicking on the button to select "PacBio FASTQ #1" opens a box called "Select a file" (as shown in the image below) to allow the user to find the desired files, either from the public data folder, or files uploaded by the user. If the files are uploaded to an accessible URL, the URL can be pasted into the box.
    ![A pop-up window titled "Select a file" over a grayed out background for the workflow submission page. It shows a file structure for public metagenomic test data.](../_static/images/howto_guides/workflows/metaG/05212025_run_metag_long_file.png)
8.  Click "Submit" to start a metagenome long-reads workflow run.


### Running a single metagenomics workflow 

Each component of the end-to-end Metagenomics workflow can be run on its own if given the correct input file type(s). The following are some examples for running these individual workflows.

!["Run a Single Workflow" page with dropdown menu listing the individual workflows available to run.](../_static/images/howto_guides/workflows/metaG/062425_run_single_wf_dropdown.png)


For example, to run a paired set of FASTQ files through ReadsQC, the user can perform the following steps:

!["Run a Single Workflow" page with fields filled out for a non-interleaved ReadsQC run.](../_static/images/howto_guides/workflows/metaG/05212025_run_qc_paired.png)

1. Click on the "Metagenomics" tab on the left vertical navigation bar. 
2. Select the "Run a Single Workflow" option from the dropdown.
3. Enter a unique Project/Run Name with no spaces (underscores are fine).
4. Enter a description (optional, but recommended).
5. Select the workflow desired from the drop-down menu.
6. Select if the input data is Illumina short-read or PacBio long-read (Illumina by default).
7. Select if the input data is interleaved (YES by default). If the data is paired select NO and it will allow you to upload both forward and reverse files. 
8. Select the input file box and paste in the desired URL or choose a file from the button on the right. For this example, we will use [SRR7877884's R1](https://portal.nersc.gov/cfs/m3408/test_data/SRR7877884/SRR7877884_1.fastq.gz).
9. Paste the FASTQ URL for the associated R2 file ([SRR7877884's R2](https://portal.nersc.gov/cfs/m3408/test_data/SRR7877884/SRR7877884_2.fastq.gz)) or select a file using the file selection menu.
10. Click "Submit" to start a workflow run.

### Running a Bulk Submission Workflow

NMDC-EDGE also allows for bulk submission projects. Users can run up to 10 end-to-end Metagenomics workflows or just ReadsQC for each bulk submission.

!["Run Bulk Submission" submission page with bubbles labeled 1 through 8 pointing at different clickable buttons and typeable fields.](../_static/images/howto_guides/workflows/metaG/061725_run_bulk_submission.png)


1. Click on the "Metagenomics" tab on the left vertical navigation bar. 
2. Select the "Bulk Submission" option from the dropdown.
3. Enter a unique Project/Run Name with no spaces (underscores are fine).
4. Enter a description (optional, but recommended).
5. Select the workflow desired from the drop-down menu. Here, we will be running "Multiple Workflows".
    ![Drop-down menu with options "Multiple Workflows" or "ReadsQC".](../_static/images/howto_guides/workflows/metaG/05212025_run_bulk_submission_select.png)
6. Download the Excel Template to populate with necessary components. Hover over cells below first row to see a description of the item and whether or not an input in mandatory or optional.
   ![Excel Spreadsheet with Columns that need to be filled to run Bulk Submission.](../_static/images/howto_guides/workflows/metaG/05202025_run_bulk_submission_input.png)
7. Choose your populated "NMDC-EDGE-Metagenomics-pipeline-bulk-submission.xlsx" file or your own properly formatted Excel spreadsheet. Here, metag_1 is running long-reads, metag_2 is running short-reads, and metag_3 is running a short-reads run that neads interleaving.
   ![Excel Spreadsheet with Columns that are filled to run a Bulk Submission.](../_static/images/howto_guides/workflows/metaG/061725_bulk_submission_test_input.png)
8. Click "Submit" to start a workflow run. [Results here](#bulk-submissions)


### Inputs

Some other options for inputs include multiple sets of FASTQ files in interleaved or paired form for samples that may want to be run together. One such example is as follows, with Step 8 being the button to allow for the multiple file selections.

!["Run a Single Workflow" page with 2 sets of paired FASTQ file inputs for ReadsQC](../_static/images/howto_guides/workflows/metaG/05212025_run_multi_rqc.png) ![File selection for 2 sets of paired FASTQ file inputs](../_static/images/howto_guides/workflows/metaG/05212025_run_multi_rqc_file.png)

Other ways the inputs for each workflow may change include the types of files needed as well as the number of different types of files. For example, with Read-based Taxonomy, the input is a filtered FASTQ file. This can be uploaded by the user, input as a URL, or taken from the result of other workflows run on NMDC EDGE. The results of your other workflows will be available in the file selection menu if the file type is right for the workflow you need to run. For the Read-based Taxonomy Classification workflow, the input is filtered FASTQ files, which is the output of the ReadsQC workflow.

!["Run a Single Workflow" page for Read-based Taxonomy Classification](../_static/images/howto_guides/workflows/metaG/05292025_run_rba_from_qc_out.png) ![File selection showing projects that the user](../_static/images/howto_guides/workflows/metaG/062425_run_rba_from_qc_out_file.png)

Each workflow submission page will list the types of files necessary. For further reading, please refer to the [individual workflow documentation](https://docs.microbiomedata.org/workflows/) for a full list of inputs and outputs. 

### Outputs

![My Projects page containing a list of projects submitted by user in various run states and bubble labels for different buttons.](../_static/images/howto_guides/workflows/quickStart/062425_projects_page.png)

1. To view the status of projects and their outputs, navigate to the My Projects tab at the top of the page. 
2. Links (in the purple circles) are provided to share projects, make projects public, or delete projects
3. The "Status" column shows whether the job is in the queue (gray), submitted (blue), running (yellow), has failed (red) or completed (green). If a project fails, a log will give the error messages for troubleshooting.
4. For a quick summary on the specific project, click the dropdown arrow to the left of the project checkbox.
5. To view the full project results, click on the folder with the arrow under the "Result" column.

In this example, we will view the results of the end-to-end short-read metagenomics run set up in the [Running the full metagenomic workflow for Short Reads](#running-the-full-metagenomic-workflow-for-short-reads) section. Please note that the result page is the same for short and long reads.


### Project Summary (Results)

![Project summary page for a full metagenomic workflow run for short-reads.](../_static/images/howto_guides/workflows/metaG/062425_view_full_metag.png)

1. Project/Run Name
2. A direct link to [create an entry in the NMDC Submission Portal](https://docs.microbiomedata.org/howto_guides/submit2nmdc)
3. Contains a quick summary of the workflow(s) run and drop-down sections for a quick tabular/visual overview of results
   ![Project summary page with expanded "General" dropdown with details about the workflow run.](../_static/images/howto_guides/workflows/metaG/03102025_view_full_metag_general.png)
4. Folder of all the downloadable output files. 

For a quick overview of every output type available for metagenomic analysis, we will be looking at the results of "Running the full metagenomic workflow for short-reads".
To download the results, [go here](https://portal.nersc.gov/project/m3408//test_data/SRR7877884/SRR7877884-0.1_MetaG/).

This example shows the results of a metagenome workflow run, which shows run time under the General tab, the workflow results of each individual metagenome workflow, and the files available for download under the Download Outputs tab.

---

## Workflow Summaries 

Before diving into more detail on inputs and outputs for components of the Metagenome workflow, this table provides a summary of all workflows (linked to their documentation) to conclude the "quick-start" portion of this guide.

| Workflow                                                                                                                      | Summary                                                                   | Inputs                                                     | Outputs                                                                  | Available Downstream NMDC EDGE Analysis                          |
|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------|
| [ReadsQC](https://docs.microbiomedata.org/workflows/chapters/3_Metagenome_Reads_QC/index.html )                               | Quality control on raw Illumina reads or PacBio reads                                     | `.fastq`, `.fq`, `.fastq.gz`, `.fq.gz`                     | `fq.gz`                                                                  | Read-based Taxonomy, MetaAssembly                                |
| [Read-based Taxonomy](https://docs.microbiomedata.org/workflows/chapters/2_Read_Based_Taxonomy/index.html)                    | Taxonomic classification profiling of Illumina or PacBio sequencing file reads      | (filtered) `.fastq`, `.fq`, `.fastq.gz`, `.fq.gz`          | `.tsv`, `.html`                                                          |                                                                  |
| [MetaAssembly](https://docs.microbiomedata.org/workflows/chapters/4_Metagenome_Assembly/index.html )                          | Error correction, contig assembly, and contig mapping                     | (filtered) `.fastq`, `.fq`, `.fastq.gz`, `.fq.gz`          | `.agp`, `.fna`, `.sam.gz`, `.bam`, `.json`                               | MG Annotation, Viruses and Plasmids                                |
| [Viruses and Plasmids](https://portal.nersc.gov/genomad/index.html)                                                             | Identifies virus and plasmid genomes from nucleotide sequences            |  `.fasta`, `.fa`, `.fna`                                   | `.tsv`, `.faa`, `.json`                                                  |                                                                  |
| [MG Annotation](https://docs.microbiomedata.org/workflows/chapters/5_Metagenome_and_Metatranscriptome_Annotation/index.html)  | Structural and functional annotation of assembled metagenomes             | `.fasta`, `.fa`, `.fna`, `.fasta.gz`, `.fa.gz`, `.fna.gz`  | `.html`, `.gff`, `.tsv`, `.fna`                                          | MetaMAGs                                                         |
| [MetaMAGs](https://docs.microbiomedata.org/workflows/chapters/6_Metagenome_Assembled_Genome/index.html)                       | Classifies contigs into bins and refines them using functional annotation | `.fasta`, `.fa`, `.fna`, `.sam.gz`, `.bam`,`.gff`          | `tar.gz` bins of `.html`, `.pdf`, `.txt`, `.tsv`, `.faa`, `.fna`, `.gff` |                                                                  |
| [Metagenomics](https://docs.microbiomedata.org/workflows/chapters/1_Metagenome_Workflow_Overview/index.html)                  | Standardized end-to-end metagenome workflow                               | `.fastq`, `.fq`, `.fastq.gz`, `.fq.gz`                     | All the above                                                            | Components can be submitted to: ReadsQC, Read-based Taxonomy, MetaAssembly, Viruses and Plasmids, MG Annotation, MetaMAGs |
| [Metatranscriptomics](https://docs.microbiomedata.org/workflows/chapters/7_Metatranscriptome_Workflow_Overview/index.html)    | Standardized end-to-end metatranscriptome workflow                        | `.fastq`, `.fq`, `.fastq.gz`, `.fq.gz`                     | All the above                                                            | MG Annotation, Viruses and Plasmids                                |
| [Metaproteomics](https://docs.microbiomedata.org/workflows/chapters/11_Metaproteomics/index.html)                             | End-to-end data processing pipeline for studying proteomes using LC-MS/MS | `RAW` MS/MS, `.fasta` `.faa` output of MG Annotation       | `.tsv`, `.txt`, `.fasta`, `.gff`                                         |                                                                  |
| [Natural Organic Matter](https://docs.microbiomedata.org/workflows/chapters/13_Natural_Organic_Matter/index.html)             | Signal processing and molecular formula assignment of DI FT-MS data       | mass list, `.tsv`, `.txt`                                  | `.csv`, `.rsv`, `.hdf`, `.xlsx`, `.json`                                 |                                                                  |


--------

--------


### Workflow Results

#### ReadsQC

This workflow performs quality control on raw Illumina or PacBio reads to trim/filter low quality data and to remove artifacts, linkers, adapters, spike-in reads and reads mapping to several hosts and common microbial contaminants. If run on its own via the "Run Single Workflow" option, the results page would look as such:

![Workflow result page for a ReadsQC run via the "Run a Single Workflow" option with the "General" dropdown opened.](../_static/images/howto_guides/workflows/metaG/03102025_view_single_qc.png)

Regardless of whether the workflow was run on its own or as part of the larger Metagenomic pipeline, the outputs will be the same. 

![ReadsQC Result dropdown, first tab consisting of an interactive HTML area with visualizations and tables.](../_static/images/howto_guides/workflows/metaG/03102025_view_qc_result.png) ![Second tab of the Result dropdown with a bar graph of read counts and type.](../_static/images/howto_guides/workflows/metaG/03102025_view_qc_summary.png) 

The ReadsQC Result section provides a variety of metrics including the number of reads and bases before and after trimming and filtering. Both tabs of the Result section are allowed for larger viewing through the "Summary full window view" link. 

![Download section dropdown with clickable file names for downloading the workflow outputs.](../_static/images/howto_guides/workflows/metaG/03102025_download_rqc.png)

The Download Output section provides output files available to download. The clean data will be in an interleaved `.fq.gz` file. General QC statistics are in the `filterStats.txt` file.


#### Read-based Taxonomy Classification

This workflow takes in Illumina sequencing files (single-end or paired-end) or PacBio long-reads and profiles the reads using multiple taxonomic classification tools. 

!["Run a Single Workflow" page for Read-based Taxonomy Classification.](../_static/images/howto_guides/workflows/metaG/05222025_run_rba.png)

This workflow goes through three analysis tools: GOTTCHA2, Kraken2, and Centrifuge.

![Results page for Read-based Taxonomy Classification, showing summary tables generated from workflow outputs.](../_static/images/howto_guides/workflows/metaG/03102025_view_rba.png) 

The Read-based Taxonomy Classification Result section has a summary section at the top and results for each tool at three levels of taxonomy in the Taxonomy Top 10 section. The Detail section has classified reads results and relative abundance results for each tool at three levels of taxonomy.

![Circular graph with different species, genus, and family organization of workflow output.](../_static/images/howto_guides/workflows/metaG/03102025_view_rba_graph.png) 

The tables are followed by interactive multilevel pie charts to visualize organisms and classifications. The Krona plots are generated for the results at each of the three taxonomic levels for each of the tools and these can also be found in the Detail section. 

![Download section dropdown with clickable file names for downloading the workflow outputs.](../_static/images/howto_guides/workflows/metaG/03102025_download_rba.png)

The Download Output section provides output files available to download. Each tool has a separate folder for the results from that tool. Full tabular results are in the largest `.tsv` file and the interactive Krona plots (`.html` files) open in a separate browser window.


#### Assembly

This workflow takes in paired-end Illumina reads or long-read PacBio reads and performs error correction. Then the corrected reads are assembled using metaSPAdes. After assembly, the reads are mapped back to the contigs for coverage information.

![Status tab of the Metagenome Assembly Results section. Shows statistics of the assembly.](../_static/images/howto_guides/workflows/metaG/03102025_view_assy_results_1.png)
The Metagenome Assembly Result's Status tab contains summary statistics of the assembly.

![Report tab of the Metagenome Assembly Results section. Shows statistics of the assembled contigs.](../_static/images/howto_guides/workflows/metaG/03102025_view_assy_results_2.png) ![The expanded view of the Assembly Report with a graph for contig sizes.](../_static/images/howto_guides/workflows/metaG/03102025_view_assy_result_expand.png)
On the next tab, the Report shows contig based statistics and graph of the sizes. The window for the report is expanded in this example to show the full report tab.

![Download section dropdown with clickable file names for downloading the workflow outputs.](../_static/images/howto_guides/workflows/metaG/03102025_download_assy.png)

The Download Output section provides output files available to download. The primary result is the `assembly_contigs.fna` file which can also be the input for the Metagenome Annotation workflow. The `pairedMapped_sorted.bam` file along with the assembled contigs file can be the input for the MAGs Generation workflow.

#### Viruses and Plasmids

This workflow takes in assembly files (such as `contigs.fasta` or `contigs.fna`) and runs the geNomad workflow, followed by checkV to determine the quality and confidence of the geNomad results. The taxonomy that is reported is based on the [ICTV guidelines](https://ictv.global/vmr). A quickstart guide for geNomad can be found [here](https://portal.nersc.gov/genomad/quickstart.html). This workflow can be run as part of the larger Metagenome workflow or on its own. As part of the larger workflow, Viruses and Plasmids is run after Assembly. 

![Run Workflow page for Viruses and Plasmids with numbered steps and open Run Option dropdown.](../_static/images/howto_guides/workflows/metaG/03102025_run_vp.png) ![File selection pop-up for Viruses and Plasmids.](../_static/images/howto_guides/workflows/metaG/03102025_run_vp_file.png)

On its own, this workflow has three parameter options when submitting the workflow, shown in the opened dropdown box above (Step 5). The following is an explanation of the parameters. 

| Parameter Setting    | Minimum Score | Hallmark Gene Requirement | Additional Notes |
|---------------------|--------------|---------------------------|------------------|
| Default            | 0.7          | At least one for short contigs | - |
| Relaxed           | 0            | No requirement              | Reports all sequences identified as "virus" or "plasmid" regardless of score or annotation |
| Conservative      | 0.8          | At least one for all contigs | - |



![Virus prediction summary table in Results section (tab 1).](../_static/images/howto_guides/workflows/metaG/03102025_view_vp_result_1.png)

The Result tab displays information about predicted viruses in the input data including sequence length, topology, coordinates, number of genes, genetic code, virus score, false discovery rate (FDR), number of hallmark genes, marker enrichment, and taxonomy. More information about this output data can be found [here](https://portal.nersc.gov/genomad/quickstart.html#understanding-the-outputs).

![Plasmid prediction summary table in Results section (tab 2).](../_static/images/howto_guides/workflows/metaG/03102025_view_vp_result_2.png)

Another table in this section provides the plasmid prediction summary which includes information on sequence length, topology, number of genes, genetic code, plasmid score, false discovery rate (FDR), number of hallmark genes, marker enrichment, conjugation genes, and any antimicrobial resistance (AMR) genes present. As stated above, more information on this output data can be found [here](https://portal.nersc.gov/genomad/quickstart.html).

![Virus quality summary table in Results section (tab 3).](../_static/images/howto_guides/workflows/metaG/03102025_view_vp_result_3.png)

A virus quality summary table is also provided, where it details the contig ID, contig length, provirus information, gene counts, quality information, completeness information, completeness method, contamination, k-mer frequency, and any relevant warnings

All output files are available to download under the Download Outputs tab at the bottom of the results page. However, downloadable results for Viruses and Plasmids differ when running on its own versus as part of the full metagenomic pipeline. 

![Results to download for Viruses and Plasmids run on its own.](../_static/images/howto_guides/workflows/metaG/03102025_download_vp_single.png)

The basic results of the pipeline are CheckV and geNomad output files.

![Results to download for Viruses and Plasmids as part of larger metagenomic workflow.](../_static/images/howto_guides/workflows/metaG/03102025_download_vp_metag.png)

As part of the metagenome pipeline, additional output files consist of more classifications and annotations.



#### Annotation

This workflow takes assembled metagenomes and uses a number of open-source tools and databases to generate the structural and functional annotations. The input assembly is first structurally annotated, then those results are used for the functional annotation.

![Metagenome Annotation Result Statistics tables (tab 1).](../_static/images/howto_guides/workflows/metaG/03102025_view_anno_result_1.png)

The Metagenome Annotation Result section has statistics for Processed Sequences, Predicted Genes, and General Quality Information from the workflow.

![Metagenome Annotation Result protein size histogram (tab 2).](../_static/images/howto_guides/workflows/metaG/03102025_view_anno_result_2.png)

A graph for distribution of protein sizes is also provided in the second tab of the results. 

![Metagenome Annotation Result Opaver Web Path KEGG maps (tab 3).](../_static/images/howto_guides/workflows/metaG/03102025_view_anno_result_3.png)

The Opaver Web Path tab offers interactive KEGG maps for further analysis to the pathways detected in the workflow.

![Download section dropdown with clickable file names for downloading the workflow outputs.](../_static/images/howto_guides/workflows/metaG/03102025_download_assy.png)

The Download Output section provides output files available to download. The primary results are the functional annotation and the structural annotation files (`.gff`). The functional annotation file is required input for the MAGs Generation workflow along with the assembled contigs.


#### MAGs Generation

For all processed metagenomes, it classifies contigs into bins. Next, the bins are refined using the functional Annotation file (GFF) from the Metagenome Annotation workflow and optional contig lineage information. The completeness of and the contamination present in the bins are evaluated and assigned a quality level (High Quality (HQ), Medium Quality (MQ), Low Quality (LQ)).

![MAGs Result Summary statistics (tab 1).](../_static/images/howto_guides/workflows/metaG/03102025_view_mags_results_1.png)

The Metagenome MAGs Result section provides a Summary section with information on binned and unbinned contigs. 

![MAGs Result binning table (tab 2).](../_static/images/howto_guides/workflows/metaG/03102025_view_mags_results_2.png)

The MAGs section provides information such as the completeness of the genome, amount of contamination, and number of genes present on all bins determined to be high quality or medium quality.

![MAGs Result bar plot of genomes and modules (tab 3).](../_static/images/howto_guides/workflows/metaG/03102025_view_mags_results_3.png)

The Bar Plot contains information regarding metabolism module categories per genome, based off the KO analysis results.

![MAGs Result module completeness heatmap (tab 4).](../_static/images/howto_guides/workflows/metaG/03102025_view_mags_results_4.png)

The Heatmap presents the completeness of the modules shown in the bar plot.

![MAGs Result Krona plot for bins and classification (tab 5).](../_static/images/howto_guides/workflows/metaG/03102025_view_mags_results_5.png)

The Krona plot contains the KO analysis results for metagenome bins at two levels of module binning.

![Download section dropdown with clickable file names for downloading the workflow outputs.](../_static/images/howto_guides/workflows/metaG/03102025_download_mags.png)

The Download Output section provides output files available to download. The primary output file is the zipped file with all bins determined to be high quality or medium quality (`hqmq_bin.zip`).



#### Bulk Submissions

Bulk submissions are run as either just ReadsQC or through the entire metagenomic pipeline. Here, we will be looking at the results page of a Multiple Workflows(Full metagenomic pipeline) bulk submission:

![Workflow result page for a Bulk Submissions run with the "Multiple Workflows" option.](../_static/images/howto_guides/workflows/metaG/061725_bulk_submission_result_page.png)

1. Note that the results for bulk submission are in a separate tab.
2. The results of each run are listed. Whether you submit a workflow as a standalone run or include it in a bulk submission, each run’s output will look exactly the same as if it had been executed on its own.

![Bulk_submission summary results with individual projects listed.](../_static/images/howto_guides/workflows/metaG/061725_bulk_submssion_results.png) 

The Bulk Submission Results section displays the same information you would see when viewing a project in [My Projects](#outputs).


