Download the dataset for hotels from http://kavita-ganesan.com/entity-ranking-data . I have included the reviews for the cars dataset.
Store all the python codes in the OpinRankDataset folder extracted with the folders cars & hotels

1. First run create_review_files.py to create the reviews from the Cars and Hotels dataset to generate reviews inside the Reviews folder
2. Next run sentiment.py to generate sentiments of the reviews. You need to change the path in line 6 from cars to hotels to generate sentiment data for the dataset. A file called sentiment_scores.txt is generated inside the Reviews folder
3. form_hash_tables.py to run the program without considering the multiple aspects in the query
4. form_hash_tables_aspects.py to run the program considering the multiple aspects in the query
5. When the program asks for you to enter the query terms, separate the different aspects of the query using the comma to observe the results.

Final results also get stored in the file final_output.txt in the form of <Entity name> <BM25 score> <Sentiment score>