package ru.hse.bigdata.researchseminar.extractors

import org.apache.spark.sql.{Dataset, SQLImplicits, SaveMode}
import ru.hse.bigdata.researchseminar.entities.Tweet

object TopHashTags extends Extractor {

  override def saveFeatures(tweets: Dataset[Tweet], target: String)(implicit implicits: SQLImplicits): Unit = {
    import implicits._

    tweets
      .filter(_.entities != null)
      .flatMap(_.entities.hashtags)
      .map(t => (t.text, 1))
      .groupByKey(_._1)
      .reduceGroups((a, b) => (a._1, a._2 + b._2))
      .map(_._2)
      .sort($"_2".desc)
      .repartition(1)
      .write
      .mode(SaveMode.Overwrite)
      .csv(target)
  }

  override def postfix: String = "top_hash_tags"
}
