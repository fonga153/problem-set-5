#!/usr/bin/env python

#import ipdb

from collections import Counter
import cyvcf2
import pybedtools
import sys
import string


filenamebed = '/Users/test/GitHub/ProblemSet1/problem-set-1/data-sets/bed/lamina.bed'
filename = '/Users/test/GitHub/ProblemSet1/problem-set-1/data-sets/fastq/SP1.fq'

genes = pybedtools.BedTool(filenamebed)

#ProblemSet5,#1:On what chromosome is the region with the largest start
#position(2nd column) in lamina.bed?

#reader = cyvcf2.Reader(filenamebed)

largest = 0
largeEnd = 0

for record in genes:

    chrom = record.chrom
    start = record.start
    end = record.end


    if (start >= largest):
        largest = start
        largestName = chrom


print "answer-1:", largestName


#ProblemSet5,#2: What is the region with the largest end position on chrY
# in lamina.bed?  Report as chrom start end value region_length

for record in genes:

    name = record.name
    chrom = record.chrom
    start = record.start
    end = record.end

    if chrom == 'chrY':

        if (end >= largeEnd):
            largeEnd = end
            largechrom = chrom
            largestart = start
            largename = name

        else: continue
    else: continue



print "".join(["answer-2: ", largechrom,":",str(largestart),"-",str(largeEnd)])

#print "answer-2:",largechrom,sys.stdout.write(':'), largestart, sys.stdout.write('-'), largeEnd


#ipdb.set_trace()


#Which of the first 10sequence records has the largest number of "C"
#residues in the sequence?  Report its record name.


def parse_fastq(fq):
    line_num = 0
    record = 0
    countC = 0
    maxName = ''

    for line in open(fq):

        line_type = line_num % 4

        if line_type == 0:
            name = line.strip()
            record += 1

        elif line_type == 1:
            seq = line.strip()
            count = Counter(seq)
            if record < 9:
                if count['C'] > countC:
                    countC = count['C']
                    maxName = name

        elif line_type == 3:
            quals = line.strip()

        #yield name, seq, quals

        line_num += 1


    print "answer-3:", maxName


parse_fastq(filename)



#For each record, convert each character in the quality score to a number
#and sum the numbers.  Use the python function 'ord' to convert characters
#to numbers.  Report the largest total quality score.

def sum_quals(fastq):

    line_num = 0
    finalsumquals = 0

    for line in open(fastq):

        line_type = line_num % 4

        if line_type == 0:
            name = line.strip()

        elif line_type == 1:
            seq = line.strip()

        elif line_type == 3:
            quals = line.strip()

            sum_quals = 0
            for char in quals:
                sum_quals += ord(char)

            if sum_quals > finalsumquals:
                finalsumquals = sum_quals

        line_num += 1

    print "answer-4:", finalsumquals

sum_quals(filename)


#Report the reverse complement of each of the first 10 sequences.  You
#will have to define a reverse-complement() method, or find one from
#another package.

def reverse_complement(seqfq):
    line_num = 0
    rev_comp = ''
    recordnum = 0
    listrevseq = []

    for line in open(seqfq):
        comps = []
        recordnum += 1
        revseq = []

        line_type = line_num % 4

        if line_type == 0:
            name = line.strip()

        elif line_type == 1:
            seq = line.strip()

#assigning the reverse complement of each nucleotide in sequence

            for char in seq:
                if char == 'G':
                    comps.append('C')
                elif char == 'A':
                    comps.append('T')
                elif char == 'T':
                    comps.append('A')
                elif char == 'C':
                    comps.append('G')

            rev_comp = ''.join(reversed(comps))
            revseq = [rev_comp]
            listrevseq.append(revseq[0])
    #append to make a list and you call it 0 to add to the first entry

        elif line_type == 3:
            quals = line.strip()

        line_num += 1
        #adding 1 each time to account for each ine in each record
        #since only want the first 10 records

        if recordnum > 40:
            break
    print "answer-5:", listrevseq

reverse_complement(filename)

#to pipe the python answers to answers.yml, do the following:
# python ProblemSet5a.py > answers.yml
# you can then cat answers.yml to see the answers


