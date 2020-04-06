package ru.hse.bigdata.researchseminar.entities

case class Tweet(created_at: String,
                 entities: Entities,
                 full_text: String,
                 geo: Option[String],
                 place: Option[String],
                 source: Option[String],
                 lang: Option[String],
                 id_str: String,
                 quoted_status: QuotedStatus,
                 retweet_count: Option[BigInt],
                 user: User)