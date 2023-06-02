#!/usr/bin/python

import sys, os
from Bio import SeqIO


def get_unigenes(species, transrate_f, chimera_f):
	all_seqs = SeqIO.to_dict(SeqIO.parse(transrate_f, "fasta"))

	chimeras = []
	with open(chimera_f, "r") as inf:
		for line in inf:
			chimeras.append(line.strip().split()[0])

	good_seqs = {}
	for seqid, seqobject in all_seqs.items():

		if seqid in chimeras:
			continue

		gene = "_".join(seqid.split("_")[:-1])

		if gene not in good_seqs.keys():
			good_seqs[gene] = seqobject
			continue

		if len(seqobject.seq) > len(good_seqs[gene].seq):
			good_seqs[gene] = seqobject

	SeqIO.write(good_seqs.values(), "unigenes.{}".format(species), "fasta")
	print('total transcripts: ', len(good_seqs.keys()))



def compare_cut_transcripts(species, transrate_dir, chimera_f):
	#transrate_bad = os.path.join(transrate_dir, species, "trinity_{}.Trinity".format(species), "bad.trinity_{}.Trinity.fasta".format(species))
	#transrate_bad = os.path.join(transrate_dir, 'bad.{}'.format(species))
	transrate_bad = os.path.join(transrate_dir, "bad.trinity_{}.Trinity.fasta".format(species))
	t = []
	with open(transrate_bad, 'r') as inf:
		for line in inf:
			if line.startswith('>'):
				t.append(line.strip()[1:])

	c = []
	with open(chimera_f, 'r') as inf:
		for line in inf:
			l = line.strip().split()
			c.append(l[0])

	overlap = set(t).intersection(set(c))
	t_only = set(t).difference(overlap)
	c_only = set(c).difference(overlap)

	print('total isoforms removed: ', len(overlap) + len(t_only) + len(c_only))
	print('overlap: ', len(overlap))
	print('transrate only: ', len(t_only))
	print('chimeric only: ', len(c_only))


def main():
	transrate_dir = os.path.abspath(sys.argv[1])
	chimera_dir = os.path.abspath(sys.argv[2])

	#samples = ['.'.join(i.split('.')[:-3]) for i in os.listdir(chimera_dir) if i.endswith('.cut')]
	samples = [i.split('.')[0] for i in os.listdir(chimera_dir) if i.endswith('cut')]
	#samples = [i for i in os.listdir(transrate_dir)]
	print(samples)	
	for i in samples:
		print(i)
		#transrate_f = os.path.join(transrate_dir, i, "trinity_{}.Trinity".format(i), "good.trinity_{}.Trinity.fasta".format(i))
		transrate_f = os.path.join(transrate_dir, "good.trinity_{}.Trinity.fasta".format(i))
		#chimera_f = os.path.join(chimera_dir, "{}.cut".format(i))
		chimera_f = os.path.join(chimera_dir, "{}.blastx.tsv.cut".format(i))
		#transrate_f = os.path.join(transrate_dir, 'good.{}'.format(i))
		#chimera_f = os.path.join(chimera_dir, '{}.blastx.tsv.cut'.format(i))
		get_unigenes(i, transrate_f, chimera_f)
		compare_cut_transcripts(i, transrate_dir, chimera_f)

		print()


if __name__ == "__main__":
	main()
