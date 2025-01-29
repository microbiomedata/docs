# Running the NMDC Workflows in NMDC EDGE Tutorials

## NMDC EDGE QuickStart

<!--
    Note: The following HTML snippet was copied from the "Share > Embed" popup on the video's YouTube page, then, its
          original `width="560" height="315"` attribute pair was replaced with `class="nmdc-embedded-youtube-video"`.  
-->
<iframe class="nmdc-embedded-youtube-video" src="https://www.youtube-nocookie.com/embed/Z5Oq7BXo43k?si=pEVuglBAlggXqUBX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

>NMDC EDGE QuickStart Tutorial Practice
>
>Task 1:  Create an NMDC EDGE account with your ORCiD information.
>
>Task 2: Download the small interleaved [data file](https://portal.nersc.gov/cfs/m3408/test_data/SRR7877884/SRR7877884-int-0.1.fastq.gz) listed here. (Note: This is paired-end data with the pairs interleaved together into a single file.) Upload the file to NMDC EDGE.
>
>Task 3 (optional):  Click on "My Profile". Edit your account to receive email notification of project status by clicking “ON”.

## Metagenomics

### ReadsQC

>NMDC EDGE Metagenome ReadsQC Tutorial Practice 
>
>Task: Log into NMDC EDGE and run the Metagenome ReadsQC workflow using the dataset uploaded in the QuickStart tutorial. When the run has finished, answer the questions below using the workflow results. 
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 1:  How many reads were in the input file? How many bases were in the input file?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 2:  How many reads were in the output file? How many bases were in the output file?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 3:  Which output file would you then use as the input for a subsequent workflow if you wanted QC'ed data?


### Read-based Taxonomy Classification

>NMDC EDGE Metagenome Read-based Taxonomy Classification Tutorial Practice 
>
>Task: Run the Metagenome Read-based Taxonomy Classification workflow with all three taxonomy classification tools. (Note: All three tools are selected by default. While a user can opt to turn off one or two tools, it is recommended to run all three.) Use the clean data output file from the project run in the ReadsQC Tutorial. When the run finishes, answer the questions below using the workflow outputs.
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 1:  How many of the Top 10 **species** are identified by more than one tool?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 2:  List the **genera** that are identified by all three tools within the Top 10.
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 3:  From the Krona plot shown from the Centrifuge results at the **species level**, what percentage of the sample is estimated to be _Pseudomonas aeruginosa_? 

### Assembly

>NMDC EDGE Metagenome Assembly Tutorial Practice 
>
>Task: Log into NMDC EDGE and run the Metagenome Assembly workflow. Use the clean data output file from the project run in the ReadsQC Tutorial as the input. In this case, the file is interleaved paired data and only one file is required for input. When the run finishes, answer the questions below using the workflow outputs.
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 1:  How many contigs were generated from the assembly?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 2:  How many scaffolds were generated from the assembly?

### Annotation

>NMDC EDGE Metagenome Annotation Tutorial Practice 
>
>Task: Log into NMDC EDGE and run the Metagenome Annotation workflow. Use the assembled contigs which are output from the project run in the Assembly Tutorial (assembled_contigs.fna). When the run finishes, answer the questions below using the workflow outputs.
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 1:  How many contigs had genes called (sequences_with_genes)?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 2:  Can you find coding sequences (genes) that were predicted by Prodigal? By GeneMark?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 3:  What is the coding density of this metagenome?

### MAGs Generation

>NMDC EDGE MAGs Generation Tutorial Practice 
>
>Task: Log into NMDC EDGE and run the Metagenome MAGs workflow. Use the assembled contigs and the read mapping file which are output from the project run in the Assembly Tutorial (assembled_contigs.fna and pairedMapped_sorted.bam) and the combined functional annotation file from the Annotation Tutorial (the file ending in fuctional_annotation.gff). When the run finishes, answer the questions below using the workflow outputs.
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 1:  Calculate the percentage of the contigs that were binned.
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 2:  How many bins were determined to be high quality (HQ)? How many bins were determined to be medium quality (MQ)?
>
>&nbsp;&nbsp;&nbsp;&nbsp;Question 3: What is the organism that was identified from the bin that is most complete and has the least contamination (the highest quality bin)? (Note: Scroll to the far right of the summary table in the results to get the species assignment.)




## Answers to Tutorial Questions

### Metagenomics ReadsQC
>Question 1: Input file contained 4,496,774 reads and 674,516,100 bases.
>
>Question 2: Output contained 3,353,438 reads and 487,250,239 bases.
>
>Question 3: For this project, the clean, filtered data is in the output file called SRR7877884-int-0.1.filtered.gz.

### Metagenomics Read-based Taxonomy Classification
>Question 1: There are seven species called by more than one taxonomy tool: *Pseudomonas aeruginosa, Salmonella enterica, Listeria monocytogenes, Enterococcus faecalis, Lactobacillus fermentum, Bacillus subtilis, and Escherichia coli.*
>
>Question 2: There are four genera called by all three taxonomy classification tools: *Pseudomonas, Bacillus, Enterococcus, and Lactobacillus.*
>
>Question 3: The Krona plot shows that Centrifuge estimates that 12% of the sample is *Pseudomonas aeruginosa.*

### Metagenomics Assembly
>Question 1: 3,196 contigs were assembled.
>
>Question 2: 3,141 scaffolds were created.

### Metagenomics Annotation
>Question 1: 3,031 contigs had genes called.
>
>Question 2: 2,495 CDS (coding sequences or genes) were called by GeneMark and 936 CDS were called by Prodigal. Several should be seen in the output table.
>
>Question 3: The coding density of the metagenome is 89.15%.

### Metagenome MAGs 
>Question 1: 24% of the contigs were binned (binned contigs divided by total number of binned and unbinned contigs)
>
>Question 2: One bin was determined to be high quality and five bins were determined to be medium quality.
>
>Question 3: The organism called by gtdbtk for the highest quality bin is *Bacillus marinus.*
