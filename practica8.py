import re
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("contar palabras")
sc = SparkContext(conf=conf)

verbose = "ERROR"

if verbose == "info":
	logleveltype = "INFO"
elif verbose == "warning":
	logleveltype = "WARN"
else:
	logleveltype = "ERROR"
sc.setLogLevel(logleveltype)


###################################
#####		poner codigo aqui #####
###################################

for act_dict in ACCION:
	print act_dict[0] + ":", act_dict[1]
