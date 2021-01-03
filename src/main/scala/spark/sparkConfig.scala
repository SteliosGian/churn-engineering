package spark

//import java.util.Properties

class sparkConfig {

  // Path of the CSV file
  val dataPath: String = "src/main/python/src/data/telco_churn.csv"

  // Spark app name
  val appName: String = "sparkSQL"

  // Path to save the parquet data
  val saveData: String = "src/main/python/src/data/parquet"
}