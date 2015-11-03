import subprocess, getopt, sys
import CGAT.Experiment as E
import CGAT.IOTools as IOTools
import CGAT.Blat as Blat
import CGAT.GTF as GTF

def usage():
	print("This is the way you are supposed to use the program")
	print("Here is an example of the syntax")
	print("These are the requirements for this program")
	print("These are the contact details of the coder")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hoag:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for option, value in opts:
        if option == in ("-v", "--verbose"):
            verbose = True
        elif option in ("-h", "--help"):
            usage()
            sys.exit()
        elif option in ("-o", "--output"):
            output = value
        elif option in ("-g", "--genome"):
		   reference_genome = valueel
		elif option in ("-a", "--assembly"):
		reference_genome = value
        else:
            assert False, "unrecognized option: known arguments are -v,-h,-o,-g,-a"
    # ...

if __name__ == "__main__":
    main()



blat_output_psl = subprocess.check_output(['blat -t dna -q dna -tileSize 11 -minIdentity 95 -maxIntron 1001 -out psl', '-1'])
print 'Finished BLAT'


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



