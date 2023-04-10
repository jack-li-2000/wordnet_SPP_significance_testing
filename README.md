# COG403_final
processing, analysis of wordnet data vs SPP data.

The purpose of this project is to determine if similarity in wordnet is correlated to similarity of word relations of humans. 
Wordnet was originally developed to model similarity structures in humans but has evolved since its adoption in the natural language processing space. We attempt to determine if it still functions in its original purpose.

We compare structural layout of words in Wordnet based on similarity and other metrics (using #some similarity metric) with semantic similarity between prime word and target word in SPP (based on reaction time and accuracy of tasks).

Data that is used in this project is from https://www.montana.edu/attmemlab/spp.html where we process the lexical decision and naming tasks of people.
Data from wordnet is used as the other side of the comparison. 

Major data sets used are all naming subjects.xlsx and NT_trials_all_sims_with_NaNs.csv with sppanalysis_cleaned.ipynb being the main notebook for analysis. Everything should be reproducible. 
