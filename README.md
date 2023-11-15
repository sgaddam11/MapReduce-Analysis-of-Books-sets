

# Hadoop MapReduce Analysis - Books Set

In this project we are going to analyse the data provided by openlibrary.org

http://openlibrary.org/data/ol_dump_works_latest.txt.gz

As it has huge data we are going to analyse it using hadoop streaming API


First clone the mapper.py and reducer.py from the current repository



#After cloning mapper and reducer programs run the following command.

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /data/openlibrary/ol_dump_works_latest-20161202.txt -output /users-cloud-16fs/sgaddam/p03-out/output2 -mapper ~/p03/mapper.py -reducer ~/p03/reducer.py -file ~/p03/{mapper,reducer}.py

# To view the output of mapreduce run the following command.
hdfs dfs -cat /users-cloud-16fs/sgaddam/p03-out/project1007/part-00000
