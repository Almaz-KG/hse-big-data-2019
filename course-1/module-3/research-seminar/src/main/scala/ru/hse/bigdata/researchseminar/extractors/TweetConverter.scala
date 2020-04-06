package ru.hse.bigdata.researchseminar.extractors

import java.text.SimpleDateFormat
import java.util.Locale

import org.apache.spark.sql.{Dataset, SQLImplicits, SaveMode}
import ru.hse.bigdata.researchseminar.entities.Tweet

import scala.util.Try

object TweetConverter extends Extractor {

  override def saveFeatures(tweets: Dataset[Tweet], target: String)(implicit implicits: SQLImplicits): Unit = {
    import implicits._

    tweets
      .map(t => TweetShort(t))
      .repartition(1)
      .write
      .mode(SaveMode.Overwrite)
      .json(target)
  }

  override def postfix: String = "tweeter_short"
}

case class TweetShort(created_at: String,
                      hashtags: Seq[String],
                      user_mentions: Seq[String],
                      full_text: String,
                      geo: Option[String],
                      lang: Option[String],
                      place: Option[String],
                      retweet_count: Option[BigInt],
                      source: Option[String],
                      user_created_at: Option[String],
                      user_default_profile: Option[String],
                      user_description: Option[String],
                      user_favourites_count: Option[BigInt],
                      user_followers_count: Option[BigInt],
                      user_friends_count: Option[BigInt],
                      user_geo_enabled: Option[Boolean],
                      user_lang: Option[String],
                      user_name: Option[String],
                      user_screen_name: Option[String],
                      user_statuses_count: Option[BigInt],
                      user_verified: Option[Boolean])

object TweetShort {

  val format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.US)

  def apply(t: Tweet): TweetShort = new TweetShort(
    created_at = parseDate(t.created_at),
    hashtags = if (t.entities == null) Seq() else t.entities.hashtags.map(_.text),
    user_mentions = if (t.entities == null) Seq() else t.entities.user_mentions.map(_.screen_name),
    full_text = t.full_text,
    geo = t.geo,
    lang = t.lang,
    place = t.place,
    retweet_count = t.retweet_count,
    source = t.source,

    user_created_at = if (t.user == null) None else t.user.created_at.map(d => parseDate(d)),
    user_default_profile = if (t.user == null) None else t.user.description,
    user_description = if (t.user == null) None else t.user.description,
    user_favourites_count = if (t.user == null) None else t.user.favourites_count,
    user_followers_count = if (t.user == null) None else t.user.followers_count,
    user_friends_count = if (t.user == null) None else t.user.friends_count,
    user_geo_enabled = if (t.user == null) None else t.user.geo_enabled,
    user_lang = if (t.user == null) None else t.user.lang,
    user_name = if (t.user == null) None else t.user.name,
    user_screen_name = if (t.user == null) None else t.user.screen_name,
    user_statuses_count = if (t.user == null) None else t.user.statuses_count,
    user_verified = if (t.user == null) None else t.user.verified
  )


  def parseDate(date: String): String = {
    if (date == null || date.isEmpty) ""
    else Try {
      import org.joda.time.format.DateTimeFormat
      val formatter = DateTimeFormat.forPattern("EEE MMM dd HH:mm:ss yyyy")
      val formatter1 = DateTimeFormat.forPattern("yyyy-MM-dd HH:mm:ss")
      val dt = formatter.parseDateTime(date.replace(" +0000", ""))

      dt.toString(formatter1)
    }.getOrElse("")
  }
}
