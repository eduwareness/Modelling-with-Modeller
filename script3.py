from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='tseq1', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='tseq1A', atom_files='tseq1.pdb')
aln.append(file='qseq.ali', align_codes='qseq')
aln.align2d()
aln.write(file='qseq-tseq1A.ali', alignment_format='PIR')
aln.write(file='qseq-tseq1A.pap', alignment_format='PAP')