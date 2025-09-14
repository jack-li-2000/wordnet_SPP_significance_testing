WordNet vs. SPP Significance Testing

Summary

This project investigates whether semantic similarity measures in WordNet still align with human semantic processing patterns as measured by the Semantic Priming Project (SPP). WordNet was originally designed to model human similarity structures, but its role has evolved in the NLP space. This analysis compares WordNet‑based similarity metrics with human reaction time and accuracy data from lexical decision and naming tasks to determine if the original cognitive alignment still holds.
Motivation

While WordNet remains a cornerstone in computational linguistics, it’s unclear whether its similarity structure continues to reflect human semantic relationships. By comparing it to large‑scale human behavioural data from the SPP, this project aims to answer:

* Does WordNet’s similarity network still mirror human semantic processing?
* Are certain similarity metrics more cognitively valid than others?

Hypothesis

* Higher WordNet similarity scores (e.g., Wu–Palmer) will correlate with faster reaction times and higher accuracy in human lexical decision and naming tasks.
* Collocated word pairs will show stronger alignment between WordNet similarity and human performance than non‑collocated pairs.

Data Sources

SPP Data – https://www.montana.edu/attmemlab/spp.html
All naming - subjects.xlsx: Prime word, target word, reaction time, accuracy, ISI, etc. (human benchmark)

WordNet Data

NT_trials_split_up_WordNet_pairs.csv: Similarity ratings (Wu–Palmer, Lin, PathSim, etc.) for non‑collocated pairs
NT_trials_split_up_collocation_pairs.csv: Similarity ratings for collocated pairs

Methods

Tools & Languages: Python, Jupyter Notebook, NLTK WordNet interface, Pandas, NumPy, SciPy

Process:

1. Data Cleaning – Standardized word formats, removed missing values, merged datasets on prime–target pairs.
2. Metric Selection – Focused on Wu–Palmer similarity for primary analysis.
3. Statistical Testing – Correlation analysis between WordNet similarity scores and SPP reaction times/accuracy.
4. Condition Comparison – Separate analysis for collocated vs. non‑collocated word pairs.
5. Visualization – Scatter plots, histograms, and significance test summaries.

Conclusion

* Correlation Strength – Moderate alignment between WordNet similarity and human semantic priming, stronger for collocated pairs.
* Metric Performance – Wu–Palmer showed the most consistent correlation with human data among tested metrics.
* Implication – WordNet retains some cognitive validity, but alignment is not perfect, suggesting potential for hybrid models combining lexical databases with behavioural data.

How to Run

Clone the repository:
   
    bash git clone https://github.com/jack-li-2000/wordnet_SPP_significance_testing.git 
    cd wordnet_SPP_significance_testing
    
Open and run the Jupyter notebooks:

    sppanalysis_script.py (used as an imported module)
    sppanalysis_wordnetsim.ipynb
    sppanalysis_coll.ipynb
