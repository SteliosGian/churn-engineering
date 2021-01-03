package spark

import org.apache.spark.sql._
import org.apache.spark.sql.functions.{avg, stddev}

class spark(spark: SparkSession, config: sparkConfig) {

  def readData(): DataFrame = {
    import spark.implicits._
    spark.read
      .option("header", "true")
      .option("inferSchema", "true")
      .csv(config.dataPath)
}

  def computeAvg(df: DataFrame): DataFrame = {
    df.groupBy("PaymentMethod").agg(
      avg("TotalCharges") as "TotalChargesAvg"
    )
  }

  def computeStd(df: DataFrame): DataFrame = {
    df.groupBy("PaymentMethod").agg(
      stddev("TotalCharges") as "TotalChargesStd"
    )
  }

  def joinDf(leftDf: DataFrame, rightDf: DataFrame): DataFrame = {
    leftDf.join(rightDf, "PaymentMethod")
  }
}