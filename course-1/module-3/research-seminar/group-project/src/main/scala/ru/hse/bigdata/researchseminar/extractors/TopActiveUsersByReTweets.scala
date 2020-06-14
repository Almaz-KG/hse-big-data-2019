package ru.hse.bigdata.researchseminar.extractors

import org.apache.spark.sql.{Dataset, SQLImplicits, SaveMode}
import ru.hse.bigdata.researchseminar.entities.Tweet

object TopActiveUsersByReTweets extends Extractor {

  override def saveFeatures(tweets: Dataset[Tweet], target: String)(implicit implicits: SQLImplicits): Unit = {
    import implicits._

    tweets
      .filter(t => t.quoted_status != null)
      .map(t => (t.user.screen_name, t.quoted_status.retweet_count))
      .groupByKey(_._1)
      .reduceGroups((a, b) => (a._1, a._2 + b._2))
      .map(_._2)
      .sort($"_2".desc)
      .repartition(1)
      .write
      .mode(SaveMode.Overwrite)
      .csv(target)
  }

  override def postfix: String = "top_users_by_retweets"
}
