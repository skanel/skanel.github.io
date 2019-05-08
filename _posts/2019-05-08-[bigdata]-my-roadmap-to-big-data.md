---
layout: post
title: BigData|ផែនការសម្រាប់ការឆ្ពោះទៅប្រើBigData
---

នេះជាផែនការដែលខ្ញុំបានអនុវត្តក្នុងការផ្លាស់ប្ដូរមកប្រើ BigData Technology Stack.

# ROADMAP:
|>Preparation 01 month <br/>
|>Milestone1 02 months <br/>
|>Milestone2 1.5 month <br/>
|>Milestone3 01 month <br/>
|>Milestone 01 month <br/>

Preparation: duration: 1 month
===========

1. Resources: Need person to working on this, should be person in report team.
	- One project leader who have knowledge of agile / Scrum & Six sigma: 
	- One person good at Hadoop ecosystem/SQL server: 
	- One developer using Java or Python or Scala.
2. Ecosystem infrastructure
	-Need a cluster: The cluster is the set of host machines (nodes). Nodes may be partitioned in racks. This is the hardware part of the infrastructure.
	-Need a YARN Infrastructure:   Responsible for providing the computational resources (e.g., CPUs, memory, etc.) needed for application executions.
	-Or Cloud at AWS or any cloud platform.


Milestone1: duration: 3 months
==========

1. For Data warehouse:
Objective: To transfer all data warehouse sql to big data data warehouse
How:
  1. using sqoop to transfer data from sql server to HDFS (Hadoop file system)
  2. using hive to manage the data warehouse
2. For Data Landing:
Objective: To transfer all data landing into HDFS landing
  How:
    1. Using Apache spark/sqoop to transfer sql data landing to HDFS
    2. using hive/hbase to manage the data landing 

Milestone2: duration: 1.5: month
===========

Objective: Extreme Cube Olap engine for big data
How: 
1. From warehouse to cube olap by using Apache kylin which provide SQL interface and multi-dimensional analysis (OLAP) on Hadoop/Spark.
		
Milestone3: duration: 1: month
==========
Objective: BI & Reporting
How:
1. Create web interface to access big data report for business user.
	-loan first
	-saving second
	-TB third
				
1. Training technical user who can response to maintain Hadoop
2. Training business user how to work with olap cube with big dataset.

Milestone4: duration: 1: month
==========

Objective: Machine Learning in finance
How: Select a simple user case or small project to implement.
		
Supports:
========
 - For internal resource AMK could provide the 2 days training from https://kyligence.io/apache-kylin-certification/ 
 - For internal resources we can provide the training (Udemy online)

* [Note]: *
This road map will  implement step by step , by not blocking any business operation at all.
How:
- by keeping Insight available to business user and moving the critical part such as loan/saving , stmt.entry, categ.entry.
- keep insight cube as work for business users. 
