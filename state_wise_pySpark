from pyspark.sql.functions import *
from pyspark.sql import SparkSession

spark = SparkSession.builder\
                    .appName("State Wise Cleansing") \
                    .getOrCreate()

state_wise_data = spark.read.csv("dbfs:/FileStore/State_Wise.csv", header=True)

# Data cleansing
def cleaning(df):
    df = df.dropna()
    return df

    
state_wise_data_cleaned = cleaning(state_wise_data)
state_wise_data_cleaned.show()


