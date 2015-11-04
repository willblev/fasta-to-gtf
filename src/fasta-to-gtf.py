import subprocess, getopt, sys,time
	
def usage():
	print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~fasta-to-gtf~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print('fasta-to-gtf.py -g <path/reference_genome.fasta> -a <path/assembly.fasta> -o <path/output_name.gtf>')
	print('This is a python script which produces GTF annotations using a transcriptome assembly and reference genome (in fasta format).')
	print('The script requires python 2.7 (or later) and the following python modules:')
	print('getopt, CGAT')
	print('To run this script, you must specify a reference genome, an assembly, and an output file name.')
	print('Use -v or --verbose to print intermediate status updates')


def main():
	verbose=False
	assembly=None
	output=None
	genome=None
	try:
		opts, args = getopt.getopt(sys.argv[1:], "o:g:a:hv", ["help", "verbose", "output=", "genome=", "assembly="])
	except:
		print 'fasta-to-gtf.py Says:     Unable to parse arguments.'
		usage()
		sys.exit()

	for option, value in opts:
		if option in ("-h", "--help"):
			usage()
			sys.exit()
		elif option in ("-o", "--output"):
			output = value
			print output
		elif option in ("-g", "--genome"):
			genome = value
			print genome
		elif option in ("-a", "--assembly"):
			assembly = value
			print assembly
		elif option in ("-v", "--verbose"):
			verbose = True
		else:
			assert False, 'Unrecognized option: known options are -v,-h,-o,-g,-a'
	if output == None or genome==None or assembly==None:
		print('fasta-to-gtf.py Says:     All three fields -g -a -o must be specified...')
		sys.exit()

	blat_command = "blat %s %s temp_output.psl -t=dna -q=dna -tileSize=11 -minIdentity=95 -maxIntron=1001 -out=psl" % (genome, assembly)
	if verbose: 
		print("fasta-to-gtf.py Says:     Starting BLAT using transcripts from %s as queries to map to the reference genome %s ..." % (assembly,genome))
		print("fasta-to-gtf.py Says:     Running "+blat_command)

	subprocess.call(['blat', genome, assembly, 'temp_output.psl', '-t=dna','-q=dna','-tileSize=11','-minIdentity=95','-maxIntron=1001','-out=psl'])
	if verbose:
		print('fasta-to-gtf.py Says:     BLAT finished; parsing output...')
	with open('temp_output.psl','r') as blat_output:
		with open(output,'w') as outfile:
			if verbose:
				print 'fasta-to-gtf.py Says:     Generating GTF file...'
			
			for line in blat_output:
				if line[0].isdigit():  #checks if line is header or not
					#blast format:
					split_line= line.split("\t")
					matches=split_line[0]
					misMatches=split_line[1]
					repMatches=split_line[2] 
					nCount=split_line[3]
					qNumInsert=split_line[4] 
					qBaseInsert=split_line[5] 
					tNumInsert=split_line[6]
					tBaseInsert=split_line[7]
					strand=split_line[8]
					qName=split_line[9] 
					qSize=split_line[10] 
					qStart=split_line[11] 
					qEnd=split_line[12] 
					tName=split_line[13] 
					tSize=split_line[14]
					tStart=split_line[15]
					tEnd=split_line[16]
					#gtf format: seqname, source, feature, start, end, score, strand, frame, attribute (with semicolon separated stuff)
					attributes=qName+";"+qSize
					if misMatches =="0":
						perc_ident="100"
					else:
						perc_ident=str(100-(int(misMatches)/(int(matches)+int(misMatches))))

					outfile.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (tName, "BLAT\ttranscript", tStart, tEnd, perc_ident, strand, '0', attributes))
			
		outfile.close()
	blat_output.close()
	print('fasta-to-gtf.py Says:     Finished; removing temporary files...')
	subprocess.call(['rm','temp_output.psl'])
if __name__ == "__main__":
	main()
    


