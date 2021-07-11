import os
import numpy as np
from azureml.core import Model
from pyspark.ml import PipelineModel
from pyspark.sql import SparkSession

def init():
    global model, columnsToBeRenamed, spark
    spark = SparkSession.builder.getOrCreate()
    model_path = Model.get_model_path('pyspark-batch-leads-model')
    model= PipelineModel.load(model_path)
    columnsToBeRenamed = {'emp.var.rate':'emp_var_rate','cons.price.idx':'cons_price_idx','cons.conf.idx':'cons_conf_idx','nr.employed':'nr_employed'}

def run(mini_batch):
    # This runs for each batch
    resultList = []
    # process each file in the batch
    for f in mini_batch:
        df = spark.read.csv(path=f,header="true",inferSchema="true",sep=",").drop('_c0')
        for key in columnsToBeRenamed.keys():
            df = df.withColumnRenamed(key, columnsToBeRenamed[key]) 
        prediction = model.transform(df).select('prediction').toPandas().prediction.map({0.0:"no",1.0:"yes"}).to_numpy()
        resultList.append("{}: {}".format(os.path.basename(f), prediction))
    return resultList
