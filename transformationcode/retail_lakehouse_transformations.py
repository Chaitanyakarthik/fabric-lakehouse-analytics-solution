#!/usr/bin/env python
# coding: utf-8

# ## Notebook_2
# 
# New notebook

# In[12]:


# Welcome to your new notebook
# Type here in the cell editor to add code!
from pyspark.sql.functions import *
from pyspark.sql.types import DoubleType 

# Microsoft Fabric Lakehouse Transformation Pipeline
# Bronze → Silver → Gold Processing

bronze_path = "abfss://be329cad-a559-4528-9b6b-5d972ef15bb3@onelake.dfs.fabric.microsoft.com/dfe7614f-2f06-4ac2-a1e6-1d616a436ec4/Files/BronzeLayer/ck/retail_raw_data_560.parquet"


# In[13]:


# Reading raw Parquet dataset into Spark DataFrame
df_bronze=spark.read.parquet(bronze_path)


# In[14]:


display(df_bronze)


# In[15]:


# STEP 3: Silver Layer Transformation

df_silver = (
    df_bronze
        .withColumnRenamed("Order ID", "OrderID")
        .withColumnRenamed("order_date", "OrderDate")
        .withColumnRenamed("cust_ID", "CustomerID")
        .withColumnRenamed("Cust Segment", "CustomerSegment")
        .withColumnRenamed("region", "Region")
        .withColumnRenamed("prodct_ID", "ProductID")
        .withColumnRenamed("Prodct category", "ProductCategory")
        .withColumnRenamed("prod_Name", "ProductName")
        .withColumnRenamed("QTY", "Quantity")
        .withColumnRenamed("price_unit", "UnitPrice")
        .withColumnRenamed("cost_unit", "CostPrice")
        .withColumnRenamed("channel", "Channel")
        .withColumnRenamed("new customer", "IsNewCustomer")
        .withColumnRenamed("store type", "StoreType")
 # ---------------- Schema Standardization ----------------
        # Renaming columns for consistency & analytics usability
        .withColumn("OrderDate", to_date("OrderDate", "dd-mm-yyyy"))

        .withColumn(
            "Quantity",
            when(col("Quantity") == "ten", "10")
            .otherwise(col("Quantity")).cast("int")
        )
   # Cast pricing fields to numeric types
        .withColumn("UnitPrice", col("UnitPrice").cast(DoubleType()))
        .withColumn("CostPrice", col("CostPrice").cast(DoubleType()))
  # Normalize categorical fields
        .withColumn("CustomerSegment", initcap(trim(col("CustomerSegment"))))
        .withColumn("Region", initcap(trim(col("Region"))))
        .withColumn("ProductCategory", initcap(trim(col("ProductCategory"))))
        .withColumn("ProductName", trim(col("ProductName")))
        .withColumn("Channel", lower(trim(col("Channel"))))
        .withColumn("IsNewCustomer", lower(trim(col("IsNewCustomer"))))
        .withColumn("StoreType", lower(trim(col("StoreType"))))
        .withColumn("SalesAmount", col("Quantity") * col("UnitPrice"))
        .withColumn("Year", year("OrderDate"))
        .withColumn("Quarter", quarter("OrderDate"))
        .withColumn("Month", month("OrderDate"))
)


display(df_silver)

#invalid_records = df_silver.filter(col("Quantity") <= 0)

#print(f"Invalid Quantity Records: {invalid_records.count()}")





# In[16]:


# Save Silver Table
# Store cleaned & transformed dataset for analytics usage
df_silver.write.mode("overwrite").saveAsTable("silver_retail_cleaned")


# In[17]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# select *
# from silver_retail_cleaned


# In[19]:


#aggregate Table

#Gold Layer Aggregations

df_gold = (
    df_silver.groupBy(
        "CustomerSegment", "ProductCategory", "Region", "StoreType",
        "Channel", "Year", "Quarter", "Month"
    ).agg(
        sum("SalesAmount").alias("TotalSales"),
        avg("UnitPrice").alias("AvgUnitPrice"),
        avg("CostPrice").alias("AvgCostPrice"),
        sum("Quantity").alias("TotalQuantity"),
        countDistinct("CustomerID").alias("UniqueCustomers"),
        countDistinct("OrderID").alias("TotalOrders")
    )
)

display(df_gold)




# Save Gold Table
df_gold.write.mode("overwrite").saveAsTable("gold_retail_segment_metrics")



