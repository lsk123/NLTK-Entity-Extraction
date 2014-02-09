#-------------------------------------------------------------------------------
# Name:        NLTK-Entity-Extraction
# Author:      Pratap Vardhan
# Created:     07-11-2013
#-------------------------------------------------------------------------------

import nltk

# Read the file
f = open('file.txt')

# Each sentence stored in line
data = f.readlines()
 
for line in data:
  # Tokenize each line
  tokens = nltk.word_tokenize(line)
  # Apply POS Tagger on tokens
	tagged = nltk.pos_tag(tokens)
	# NE chunking on tags
	entities = nltk.chunk.ne_chunk(tagged)
	print entities
f.close()
