---
layout: post
title: BigData|ទាញទិន្ន័យពី T24 ដោយប្រើApache Hadoop,Apache Spark 
---

នេះជាកូដដែលខ្ញុំប្រើដើម្បីទាញទិន្ន័យពីT24 core banking system ដែលប្រើ ប្រាស់ Oracle DB . ក្នុងកូដនេះខ្ញុំប្រើ Big Data Technology stack ដូចជា 
Apache Hadoop, Apache Spark 
Sclal programming 

![_config.yml]({{ site.baseurl }}/images/Temenos.png)

```
package com.company.projects.app.T24

import java.text.SimpleDateFormat

import org.apache.spark.sql.SparkSession

/*
 1. Extract the header from FileLayout (<c1>, <c2>, <c3>) : done
 2. Extract each row data of the table (Oracle at DR site) , there are 2 rows (RECID, XMLRECORD) : done
 3. Transform the row into header + row data (xml record) : doing (80%)
 4. Load the extracted into csv file or RDBMS :  todo
* */
object ATMBranches {
  def main(args: Array[String]): Unit = {
    import org.apache.spark.sql.functions.udf
    val toString = udf((payload: Array[Byte]) => new String(payload))
    val format = new SimpleDateFormat("d-M-y")

    val spark = SparkSession.builder()
      .appName("ConnectingOracleDatabase")
      .master("local")
      .getOrCreate()

    //ORACLE
    val jdbcUrl = "jdbc:oracle:thin:@DR-CBS-CDB01:1422:drcbs"
    val jdbcUsername = "username"
    val jdbcPassword = "password"

    // Check connectivity to ORACLE Server
    import java.sql.DriverManager
    val connection = DriverManager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)
    connection.isClosed()

    val query =
      s"""(SELECT
         |RECID as RECID,
         |extractvalue(XMLRECORD,'/row/c2') as BRANCH_CODE,
         |extractvalue(XMLRECORD,'/row/c3') as DEF_CR_ACCT,
         |extractvalue(XMLRECORD,'/row/c4') as PROC_CODE,
         |extractvalue(XMLRECORD,'/row/c5') as CR_CCY,
         |extractvalue(XMLRECORD,'/row/c6') as CR_ACCT,
         |extractvalue(XMLRECORD,'/row/c7') as RESERVED_5,
         |extractvalue(XMLRECORD,'/row/c8') as RESERVED_4,
         |extractvalue(XMLRECORD,'/row/c9') as RESERVED_3,
         |extractvalue(XMLRECORD,'/row/c10') as RESERVED_2,
         |extractvalue(XMLRECORD,'/row/c11') as RESERVED_11,
         |extractvalue(XMLRECORD,'/row/c12') as USE_DEF_ACCT,
         |extractvalue(XMLRECORD,'/row/c13') as LOCAL_REF,
         |extractvalue(XMLRECORD,'/row/c14') as RESERVED_10,
         |extractvalue(XMLRECORD,'/row/c15') as RESERVED_9,
         |extractvalue(XMLRECORD,'/row/c16') as RESERVED_8,
         |extractvalue(XMLRECORD,'/row/c17') as RESERVED_7,
         |extractvalue(XMLRECORD,'/row/c18') as RESERVED_6,
         |extractvalue(XMLRECORD,'/row/c19') as RECORD_STATUS,
         |extractvalue(XMLRECORD,'/row/c20') as CURR_NO,
         |extractvalue(XMLRECORD,'/row/c21') as INPUTTER,
         |extractvalue(XMLRECORD,'/row/c22') as DATE_TIME,
         |extractvalue(XMLRECORD,'/row/c23') as AUTHORISER,
         |extractvalue(XMLRECORD,'/row/c24') as CO_CODE,
         |extractvalue(XMLRECORD,'/row/c25') as DEPT_CODE,
         |extractvalue(XMLRECORD,'/row/c26') as AUDITOR_CODE,
         |extractvalue(XMLRECORD,'/row/c27') as AUDIT_DATE_TIME
         |FROM CBSPROD.F_ATM_BRANCH ) tmp """.stripMargin


    val DF = spark.read
      .format("jdbc")
      .option("url", jdbcUrl)
      .option("dbtable", query)
      .option("user", jdbcUsername)
      .option("password", jdbcPassword)
      .option("driver", "oracle.jdbc.driver.OracleDriver")
      .load()
    // DF.createOrReplaceTempView("v_categ_entry")
    DF.show(100, truncate = false)

    print("TOTAL: "+DF.count())

    /* WRITE TO SQL IF NEED */
    val url = "jdbc:sqlserver://AHODKT0193;databaseName=ASS;integratedSecurity=true";
    import java.util.Properties
    val connectionProperties = new Properties()
    connectionProperties.put("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver" )
    DF.write.jdbc(url, "ATM_Terminal", connectionProperties)

    DF.unpersist()
    spark.stop()

  }
}
```
