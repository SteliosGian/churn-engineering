package spark

import org.apache.spark.sql._

object sparkDriver {
  def main(args: Array[String]): Unit = {
    implicit val config: sparkConfig = new sparkConfig(System.getProperties)

    implicit val sparkSession: SparkSession = SparkSession
          .builder
          .appName(config.appName)
          .master("local[*]")
          .getOrCreate()

    val df = new spark(sparkSession, config).readData()

    val df_avg = new spark(sparkSession, config).computeAvg(df)

    val df_std = new spark(sparkSession, config).computeStd(df)

    val df1 = new spark(sparkSession, config).joinDf(df, df_avg)

    val df2 = new spark(sparkSession, config).joinDf(df1, df_std)

    df2.write.parquet(config.saveData)
  }
}