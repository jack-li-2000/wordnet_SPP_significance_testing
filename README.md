# wordnet spp significance testing
processing, analysis of wordnet data vs SPP data.

The purpose of this project is to determine if similarity in wordnet is correlated to similarity of word relations of humans. 
Wordnet was originally developed to model similarity structures in humans but has evolved since its adoption in the natural language processing space. We attempt to determine if it still functions in its original purpose.

We compare structural layout of words in Wordnet based on similarity and other metrics (using #some similarity metric) with semantic similarity between prime word and target word in SPP (based on reaction time and accuracy of tasks).


DATA ANALYSIS SECTION: 
Data that is used in this project is from https://www.montana.edu/attmemlab/spp.html where we process the lexical decision and naming tasks of people.
Data from wordnet is used as the other side of the comparison. 

Major data sets used are all naming subjects.xlsx and NT_trials_split_up_WordNet_pairs.csv, and NT_trials_split_up_collocation_pairs.csv. sppanalysis_script.py, sppanalysis_wordnetsim, and sppanalysis_coll are the main notebook for analysis. 

all naming subjects.xlsx: SPP data which includes the features: prime word, target word, reaction time, accuracy, isi, etc. The human benchmark.

NT_trials_split_up_WordNet_pairs: wordnet data which includes similarity ratings from wu-palmer, lin, path sim, etc. Analysis used wu-palmer for similarity. NOTE: This data set contains NO collocated pairs.

NT_trials_split_up_collocation_pairs: wordnet data which includes only collocated pairs with the same similarity ratings included as before. 

Run only the notebooks since the python script is used as imported module. Read the paper to gain insight on the purposes of the functions and how to apply them.


Everything should be reproducible. 
