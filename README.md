# THIS REPO IS NOT MAINTAINED! 
This script was something I whipped up for my own use, but decided to share in case it could help others. However, I won't be updating the code or revewing open issues, as other solutions [like GMAP](http://research-pub.gene.com/gmap/) exist which can serve the same purpose.

## ~~fasta-to-gtf


~~This is a python script which uses a transcriptome assembly in fasta format to generate a gtf file (for use in genome/annotation visualization comparison). 

~~**It takes as input:**

~~1. a de novo transcriptome assembly [fasta format]
~~2. a reference genome [fasta format] 

~~**It outputs a gtf file (tab separated columns) with the following fields:**

~~1. seqname - name of the chromosome or scaffold; chromosome names can be given with or without the 'chr' prefix. Important note: the seqname must be one used within Ensembl, i.e. a standard chromosome name or an Ensembl identifier such as a scaffold ID, without any additional content such as species or assembly. See the example GFF output below.
~~2. source - name of the program that generated this feature, or the data source (database or project name)
~~3. feature - feature type name, e.g. Gene, Variation, Similarity
~~4. start - Start position of the feature, with sequence numbering starting at 1.
~~5. end - End position of the feature, with sequence numbering starting at 1.
~~6. score - A floating point value.
~~7. strand - defined as + (forward) or - (reverse).
~~8. frame - One of '0', '1' or '2'. '0' indicates that the first base of the feature is the first base of a codon, '1' that the second base is the first base of a codon, and so on..
~~9. attribute - A semicolon-separated list of tag-value pairs, providing additional information about each feature.

~~# System requirements
~~* Linux OS (tested on Fedora/Scientific Linux/Ubuntu)
~~* Python version 2.7
~~* BLAT version 34
