# Databricks notebook source
# DBTITLE 1,Read Bing_covid-19_data.csv in a pandas dataframe
import pandas as pd
pdf = pd.read_csv('https://pandemicdatalake.blob.core.windows.net/public/curated/covid-19/bing_covid-19_data/latest/bing_covid-19_data.csv', low_memory=False)

# COMMAND ----------

# DBTITLE 1,From pandas dataframe create a spark dataframe
sdf = spark.createDataFrame(pdf)

# COMMAND ----------

# DBTITLE 1,Display results
sdf.display()
