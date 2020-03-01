package ru.hse.bigdata.researchseminar

import org.apache.spark.sql.SparkSession
import ru.hse.bigdata.researchseminar.entities.Tweet
import ru.hse.bigdata.researchseminar.extractors.{Extractor, TopActiveUsersByPosts, TopActiveUsersByReTweets, TopHashTags}

object HW02 {
  def buildSparkSession(appName: String): SparkSession = {
    val spark = SparkSession
      .builder()
      .master("local[2]")
      .config("spark.sql.warehouse.dir", "./target")
      .config("spark.ui.enabled", "false")
      .config("spark.sql.catalogImplementation", "in-memory")
      .config("spark.driver.host", "localhost")
      .appName(appName)
      .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    spark
  }

  def extractors: Seq[Extractor] = Seq(
    TopHashTags,
    TopActiveUsersByPosts,
    TopActiveUsersByReTweets
  )

  def main(args: Array[String]): Unit = {
//    if (args.length != 2)
//      throw new RuntimeException("Please, provide 2 params: source file_path (json file), and target file path (to store the results)")
//    val sourceFilePath = args(0)
//    val targetFilePath = args(1)

    val sourceFilePath = "src/test/resources/winter_olympics.json"
    val targetFilePath = "src/test/resources/winter_olympics_short_result"

    val session = buildSparkSession("Research seminar: HW 02")
    import session.implicits._

    val tweets = session.read.json(sourceFilePath).as[Tweet]

    extractors.foreach(ex => ex.saveFeatures(tweets, s"${targetFilePath}_${ex.postfix}")(session.implicits))
  }
}
