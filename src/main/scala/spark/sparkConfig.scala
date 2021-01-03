package spark

import java.util.Properties

class sparkConfig(private val props: Properties) extends Properties {

  val dataPath = "src/main/python/src/data/telco_churn.csv"

  val appName = "sparkSQL"

  val saveData = "src/main/python/src/data/parquet"
}