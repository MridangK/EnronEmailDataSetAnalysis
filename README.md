# Enron Dataset Analysis

In this question, we analyze the Enron dataset to gain insights from the emails. The steps below outline the process.

1. Download the Enron dataset from the site [http://www.cs.cmu.edu/~enron/](http://www.cs.cmu.edu/~enron/) by clicking on the provided link.

2. After downloading, unzip the file using the following commands:
   ```
   gzip -d enron_mail_20150507.tar.gz
   tar -xvf enron_mail_20150507.tar
   ```
   This will create a "maildir" folder.

3. For the analysis, focus on the "sent" folder only, as the entire dataset might be too large. Extract the username, sent_items, and email_contents from all the files using the provided Python code. Store this information in a CSV file for easier visualization.

4. Clean the extracted data further by keeping only the username and the email body, as these are the most relevant for our analysis.

5. Visualize the cleaned data to understand the content and distribution.

6. Check if there are any rows with null values and remove them, as they are not important for our analysis.

7. Further clean the data by converting all letters to lowercase and storing it in a CSV file.

8. Verify if there are any null values in the final CSV file.

9. Start Hadoop and remove Hadoop from safe mode.

10. Create an input directory in HDFS using the following command:
    ```
    hadoop fs -mkdir -p /user/your/path/here/finals/input
    ```

11. Put the final cleaned.csv file into the input directory:
    ```
    hadoop fs -put /your/path/to/finalcleaned.csv /user/your/path/here/finals/input
    ```

12. Run the mapper and reducer to get different files for each user with all their texts:
    ```
    hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -file /your/path/to/mapper.py -mapper /your/path/to/mapper.py -file /your/path/to/reducer.py -reducer /your/path/to/reducer.py -input /user/your/path/here/finals/input/finalcleaned.csv -output /user/your/path/here/finals/output/count_output15
    ```

13. Retrieve the output file from HDFS using the following command:
    ```
    hadoop fs -get /user/your/path/here/finals/output/count_output15/part-00000
    ```

14. Create separate files for each user using the following code:
    ```
    # Code to create separate files for each user
    ```

15. Transfer all the files to HDFS for use with Mahout:
    ```
    hadoop fs -put cleanedemails /user/your/path/here/finals
    ```

16. Convert the text files to sequence files using the seqdirectory command:
    ```
    mahout seqdirectory -i /user/your/path/here/finals/cleanedemails -o /user/your/path/here/finals/cleanedemails-seqFiles -ow
    ```

17. Use the seq2sparse command to create sparse vectors:
    ```
    mahout seq2sparse -i /user/your/path/here/finals/cleanedemails-seqFiles -o /user/your/path/here/finals/cleanedemails-vectors -ow -nv -chunk 100
    ```

18. Run the canopy command to cluster the vectors:
    ```
    mahout canopy -i /user/your/path/here/finals/cleanedemails-vectors/tf-vectors -o /user/your/path/here/finals/cleanedemails-vectors/cleanedemails-canopy-centroids -dm org.apache.mahout.common.distance.CosineDistanceMeasure -t1 1500 -t2 2000
    ```

19. Perform K-means clustering on the vectors:
    ```
    mahout kmeans -i /user/your/path/here/finals/cleanedemails-vectors/tfidf-vectors -c /user/your/path/here/finals/cleanedemails-vectors/cleanedemails-canopy-centroids -o /user/your/path/here/finals/cleanedEmails-clusters -dm org.apache.mahout.common.distance.CosineDistanceMeasure -cl -cd 0.1 -ow -x 20 -k 3
    ```

20. Use the clusterdump command to fetch the cluster information:
    ```
    mahout clusterdump -dt sequencefile -d /user/your/path/here/finals/cleanedemails-vectors/dictionary.file-0 -i /user/your/path/here/finals/cleanedEmails-clusters/clusters-2-final -o clusters.txt -b 100 -p /user/your/path/here/finals/cleanedEmails-clusters/clusteredPoints -n 100
    ```

Since we stored our files in the format of `username.txt`, we can see what each user talked about the most. For example, in `townsend-j.txt`, we see that the person mentioned words like Christmas and church. This information can be used for targeted ads, such as Christmas shopping or gifts. It's worth noting that there might be filler words present, and the significance depends on how you plan to analyze the data.

Please replace "your path name here" with the actual path on your system where the respective files and directories are located.
