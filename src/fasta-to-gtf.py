import subprocess, getopt, sys
#import CGAT.Experiment as E
#import CGAT.IOTools as IOTools
#import CGAT.Blat as Blat
#import CGAT.GTF as GTF

	
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
		print 'Unable to parse arguments.'
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
		print('All three fields -g -a -o must be specified...')
		sys.exit()

	blat_command = "blat %s %s -t dna -q dna -tileSize 11 -minIdentity 95 -maxIntron 1001 -out psl" % (genome, assembly)
	if verbose: 
		print("Starting BLAT using transcripts from %s as queries to map to the reference genome %s ..." % (assembly,genome))
		print("Running "+blat_command)

	#blat_output_psl = subprocess.check_output([blat_command, '-1'])

	if verbose:
		print 'BLAT finished; parsing output and converting to GTF...'

	
	"""
	iterator = Blat.BlatIterator(blat_output_psl)

	ninput, noutput, nskipped = 0, 0, 0

	gff = GTF.Entry()
	gff.source = "psl"
	gff.feature = "exon"

	ids = {}

	while 1:

		if options.test and ninput >= options.test:
			break

		match = iterator.next()

		if match is None:
			break

		ninput += 1

		if match.mQueryId not in ids:
			ids[match.mQueryId] = 1
			id = match.mQueryId
		else:
			id = match.mQueryId + ":%i" % ids[match.mQueryId]
			ids[match.mQueryId] += 1


		gff.contig = match.mSbjctId
		gff.gene_id = id
		gff.transcript_id = id


		if id in map_id2strand:
			gff.strand = map_id2strand[id]
		else:
			gff.strand = match.strand

		for qstart, sstart, size in match.getBlocks():

			gff.start = sstart
			gff.end = sstart + size
			options.stdout.write(str(gff) + "\n")

		noutput += 1
		"""


#did this go through?????


if __name__ == "__main__":
	main()
    


