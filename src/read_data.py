from pyspark import SparkConf, SparkContext, SQLContext

sc = SparkContext(appName="cnpj")

sqlContext = SQLContext (sc)

df = sqlContext.read.load ("/tmp/data/teste_Spark.csv",
        format='com.databricks.spark.csv',
        header='true',
        inferSchema='true').select("key1")

df.show()
