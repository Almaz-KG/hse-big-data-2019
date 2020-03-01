package ru.hse.bigdata.researchseminar.extractors

import org.apache.spark.sql.{Dataset, SQLImplicits}
import ru.hse.bigdata.researchseminar.entities.Tweet

trait Extractor {

  def saveFeatures(dataset: Dataset[Tweet], target: String)(implicit implicits: SQLImplicits): Unit

    def postfix: String
  }
