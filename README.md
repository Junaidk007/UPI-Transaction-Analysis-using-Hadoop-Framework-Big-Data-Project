# 📊 UPI Transaction Analysis using Hadoop Framework

<p align="center">
  <b>Big Data Fundamentals Project</b><br>
  <i>Implemented using Hadoop Ecosystem (HDFS, MapReduce, Hive)</i>
</p>

---

## 👨‍🏫 Batch / Group / Members

* **University:** Babu Banarasi Das University
* **Batch:** BCADS23
* **Group:** A
* **Submitted To:** MR. Vikas
* **Members:**
  * Junaid Khan (1240258209)
  * Apoorv Sharma (1240258116)
  * Jai Prakash (1240258)
  * Bipendra Kumar Pandey (1240258)

---

## 🎯 Problem Statement

Digital payment systems generate large volumes of UPI transaction data every day. Traditional systems can struggle to process and analyze this kind of data efficiently.

This project uses the Hadoop ecosystem to process UPI transaction records and extract useful insights such as:

* transaction status distribution
* transaction type distribution
* peak transaction activity
* fraud-related usage trends

---

## 📁 Dataset Description

The project uses UPI transaction CSV files stored in the `datasets/` folder:

* `upi_transactions_2024.csv` - raw dataset
* `upi_transactions_2024_cleaned.csv` - cleaned dataset used for analysis

### Key Attributes

* transaction ID
* timestamp
* transaction type
* merchant category
* amount
* transaction status
* sender age group
* receiver age group
* sender state
* sender bank
* receiver bank
* device type
* network type
* fraud flag
* hour of day
* day of week
* is weekend

The cleaned CSV is used for Hadoop Streaming and Hive-based analysis.

---

## 🏗️ Architecture

```
Raw CSV Dataset
        ↓
HDFS (Storage Layer)
        ↓
MapReduce (Processing Layer)
        ↓
Processed Output
        ↓
Hive (Analysis Layer)
        ↓
Insights and Summary Results
```

---

## ⚙️ Technologies Used

* Hadoop HDFS
* Hadoop MapReduce
* Hadoop Streaming
* Hive
* Python
* SQL
* CSV dataset
* Cloudera VM / Linux terminal

---

## 🔄 Workflow Explanation

* The cleaned dataset is uploaded to HDFS for distributed storage.
* Hadoop Streaming runs Python-based mapper and reducer scripts.
* One MapReduce job counts transaction statuses.
* Another MapReduce job counts transaction types.
* Hive is used to run SQL queries for deeper analysis.
* The results are used to generate final insights.

---

## 🤖 Use of Generative AI

Generative AI tools such as ChatGPT were used during the development of this project for:

* code generation for mapper and reducer scripts
* debugging and Python version compatibility support
* Hive query assistance
* understanding Big Data workflow concepts

---

## 📌 Conclusion

This project shows how the Hadoop ecosystem can be used to process and analyze UPI transaction data efficiently.

By combining **HDFS, MapReduce, and Hive**, the project transforms raw payment data into useful insights for understanding digital transaction patterns.
