# Running the Workflows

## NMDC EDGE QuickStart

<div style="text-align: center; margin-bottom: 2rem;">
    <!-- Note: The following HTML snippet was copied from the "Share > Embed" popup on the video's YouTube page. -->
    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Z5Oq7BXo43k?si=pEVuglBAlggXqUBX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

>NMDC EDGE QuickStart Tutorial Practice
>
>Task 1:  Create an NMDC EDGE account with either your email address or your ORCiD account.
>
>Task 2: Download the small interleaved [data file](https://portal.nersc.gov/cfs/m3408/test_data/SRR7877884/SRR7877884-int-0.1.fastq.gz) listed here. (Note: This is paired-end data with the pairs interleaved together into a single file.) Upload the file to NMDC EDGE.
>
>Task 3: Click the user icon (in the top right corner with your initials) and under “Files”, click on “Manage Uploads”. Verify that the file you uploaded is there. (Note: Later you can delete uploads that are no longer needed.)
>
>Task 4 (optional):  Click the user icon and under “Account”, click on “Profile”. Edit your account to receive email notification of project status by clicking “ON”.

## Metagenomics

### ReadsQC

<div align="center">
    <video src="https://nmdc-edge.org/docs/videos/ReadsQC.mp4" width="80%" height="80%" controls />
</div>
<br><br>

>NMDC EDGE Metagenome ReadsQC Tutorial Practice 
>
>Task: Log into NMDC EDGE and run the Metagenome ReadsQC workflow using the dataset uploaded in the QuickStart tutorial.
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 1:  How many reads were in the input file? How many bases were in the input file?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 2:  How many reads were in the output file? How many bases were in the output file?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 3:  What file in the output would be used in the next workflow?


### Read-based Taxonomy Classification

<div align="center">
    <video src="https://nmdc-edge.org/docs/videos/ReadBasedAnalysis.mp4" width="80%" height="80%" controls />
</div>
<br><br>

>NMDC EDGE Metagenome Read-based Taxonomy Classification Tutorial Practice 
>
>Task:
run the Metagenome Read-based Taxonomy Classification workflow with all three taxonomy classification tools. (Note: All three tools are selected by default. While a user can opt to turn off one or two tools, it is recommended to run all three.) Use the clean data output file from the project run in the ReadsQC Tutorial (the file ending in .anqdpht.fq.gz). In this case, the file will be treated as single-end reads.
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 1:  How many of the Top 10 species are called by more than one tool?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 2:  List the **genera** that are called by all three tools in the Top 10.
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 3:  From the Krona plot shown from the taxonomy classification tool Centrifuge results at **species level**, what percentage of the sample is estimated to be _Pseudomonas aeruginosa_? 

### Assembly

<div align="center">
    <video src="https://nmdc-edge.org/docs/videos/MetagenomeAssembly.mp4" width="80%" height="80%" controls />
</div>
<br><br>

>NMDC EDGE Metagenome Assembly Tutorial Practice 
>
>Task: Log into NMDC EDGE and run the Metagenome Assembly workflow. Use the clean data output file from the project run in the ReadsQC Tutorial (the file ending in .anqdpht.fq.gz). In this case, the file is interleaved paired data and only one file is required for input.
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 1:  How many contigs were generated from the assembly?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 2:  How many scaffolds were generated from the assembly?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 3:  Download the covstats.txt file. From the top of the file, what percentage of the reads map back to the assembled contigs?

### Annotation

<div align="center">
    <video src="https://nmdc-edge.org/docs/videos/MetagenomeAnnotation.mp4" width="80%" height="80%" controls />
</div>
<br><br>

>NMDC EDGE Metagenome Annotation Tutorial Practice 
>
>Task: Log into NMDC EDGE and run the Metagenome Annotation workflow. Use the assebled contigs which are output from the project run in the Assembly Tutorial (assembled_contigs.fna). 
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 1:  How many contigs had genes called (sequences_with_genes)?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 2:  How many coding sequences (genes) were called by Prodigal? How many were called by GeneMark?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 3:  What is the coding density of this metagenome?

### MAGs Generation

<div align="center">
    <video src="https://nmdc-edge.org/docs/videos/MetagenomeMAGs.mp4" width="80%" height="80%" controls />
</div>
<br><br>

>NMDC EDGE MAGs Generation Tutorial Practice 
>
>Task: Log into NMDC EDGE and run the Metagenome MAGs workflow. Use the assebled contigs and the read mapping file which are output from the project run in the Assembly Tutorial (assembled_contigs.fna and pairedMapped_sorted.bam) and the combined functional annotation file fromt he Annotation Tutorial (the file ending in fuctional_annotation.gff)
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 1:  Calculate the percentage of the contigs were binned.
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 2:  How many bins were determined to be high quality (HQ)? How many bins were determined to be medium quality (MQ)?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 3: What is the organism identified from genome in the bin which is most complete and has the least contamination (the highest quality bin)? (Note: Scroll to the far right of the summary table in the results to get the species assignment.)

### Running multiple workflows or the full metagenomic pipeline with a single input

<div align="center">
    <video src="https://nmdc-edge.org/docs/videos/pipeline.mp4" width="80%" height="80%" controls />
</div>
<br><br>

>NMDC EDGE Full Metagenome Piepline Tutorial Practice 
>
>Task: Log into NMDC EDGE and run the full Metagenome pipeline (multiple workflows- all workflows are selected by default). Use the same dataset uploaded in the QuickStart tutorial. Check your results for the full pipeline against your results from the previous tutorials. The results should be identical/nearly identical to the results from the previous tutorials for each individual workflow with the added benefit of submitting all the workflows with a single input of raw sequencing data.
>
>If you want to just test the full pipeline and not the individual workflows, [download this data set.](https://portal.nersc.gov/cfs/m3408/test_data/SRR7877884/SRR7877884-int-0.1.fastq.gz) Upload the file to NMDC EDGE and run the full pipeline.


## Metatranscriptomics

<div align="center">
    <video src="https://nmdc-edge.org/docs/videos/MetaT.mp4" width="80%" height="80%" controls />
</div>
<br><br>





>NMDC EDGE Metatranscriptomics Tutorial Practics
>
>Task 1: Download the small interleaved [data file](https://nmdc-edge.org/publicdata/metaT/test_smaller_interleave.fastq.gz) listed here. (Note: This is paired-end data with the pairs interleaved together into a single file.) 
>
>Task 2: Log into NMDC EDGE and upload the file. 
>
>Task 3: Click the user icon (in the top right corner with your initials) and under “Files”, click on “Manage Uploads”. Verify that the file you uploaded is there. (Note: Later you can delete uploads that are no longer needed.)
>
>Task 4: Run the MetaT single workflow with this dataset in your upload folder. When the analysis is complete, the Top_features summary table under Metatranscriptome Result tab shows the proteins assigned to transcripts with the highest rpkm values. The full results (rpkm_sorted_features.tsv) can be downloaded from the metat_output folder under the Browser/Download output tab. The assembled transcripts and the annotation fules can also be downloaded from the respective folders under the Browser/Download output tab.
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 1: What product (protein) is assigned to the transcript with the highest rpkm value? (Note: Scroll to the far right to see these results.)
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 2: Download the contigs.fa (transcripts) file.  How many transcripts were assembled?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 3: Download the rpkm_sorted_features.tsv file.  How many transcripts were assigned a product (protein) that is **not hypothetical**?



## Answers to Tutorial Questions

### Metegenomics ReadsQC
>Question 1: Input contained 4,496,774 reads and 674,516,100 bases.
>
>Question 2: Output contained 3,353,438 reads and 487,250,239 bases.
>
>Question 3: For this project, the clean, filtered data is in the output file called SRR7877884-int-0.1.anqdpht.fastq.gz.

### Metegenomics Read-based Taxonomy Classification
>Question 1: There are seven species called by more than one taxonomy tool: *Pseudomonas aeruginosa, Salmonella enterica, Listeria monocytogenes, Enterococcus faecalis, Lactobacillus fermentum, Bacillus subtilis, and Escherichia coli.*
>
>Question 2: There are four genera called by all three taxonomy classification tools: *Pseudomonas, Bacillus, Enterococcus, and Lactobacillus.*
>
>Question 3: The Krona plot shows that Centrifuge estimates that 12% of the sample is *Pseudomonas aeruginosa."

### Metegenomics Assembly
>Question 1: 3,196 contigs were assembled.
>
>Question 2: 3,141 scaffolds were created.
>
>Question 3: 

### Metegenomics Annotation
>Question 1: 3,031 contigs had genes called.
>
>Question 2: 2,495 CDS (coding sequences or genes) were called by GeneMark and 936 CDS were called by Prodigal.
>
>Question 3: The coding density of the metagenome is 89.15%.

### Metagenome MAGs 
>Question 1: 24% of the contigs were binned.
>
>Question 2: One bin was determined to be high quality and five bins were determined to be medium quality.
>
>Question 3: The organism called by gtdbtk for the highest quality bin is *Bacillus marinus.*
