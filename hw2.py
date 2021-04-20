import sys


def get_gc_content(s):
	s_GC = 0
	for nt in s:
	    if nt == 'G' or nt == 'C':
	        s_GC += 1
	return s_GC

def get_prob(N, GC, s):
	s_GC = get_gc_content(s)

	# prob that we get exactly this sequence generated from nts by random with GC-content == GC:
	s_prob = ((GC/2)**s_GC) * (((1-GC)/2)**(len(s)-s_GC)) 
	# ( (<exp_prob-to-get-G> ^ <observed_nr_of_occurences>) + (same-for-C) ) * ( (same-for-A) + (same-for-T) )
	# as exp prob for A == prob for T, and same for GC - we could combine it as it was done above.

	# prob that we get only other sequences for N times of generating: 
	not_s_in_N_times = (1 - s_prob)**N

	# prob that we get at least one exact sequence:
	prob = 1 - not_s_in_N_times

	#
	return '%0.3f' % prob




def main():
	if len(sys.argv) < 3:
		print('Usage: python hw2.py <number-of-sequences-to-generate> <GC-content> <sequence>')
		exit()

	N = int(sys.argv[1]) # 90000
	GC = float(sys.argv[2]) # 0.6
	s = sys.argv[3] # 'ATAGCCGA'

	print( get_prob(N, GC, s) ) # 0.689

if __name__ == '__main__':
	main()

