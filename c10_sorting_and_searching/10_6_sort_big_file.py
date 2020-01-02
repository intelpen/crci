# 10.6 Sort Big File: Imagine you have a 20 GB file with one string per line. Explain how you would sort
# the file.

# Probably he wants to sort inplace ?
# From the hint, he wants to take parts of the file in memory, sort and merge the chunks

# For example, split in 10 chunks of 2 gb
# save the 10 chunks to disk in separate files
# then for merging you load in memory about 1/10th of each file for a total of 2gb .
# Then mergesort them in memory while making sure we never get to the end of one of the chunks.
# When one chunk is at the end be sure to reload new chuunks from the indexes we had