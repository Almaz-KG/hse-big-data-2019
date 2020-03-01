package ru.hse.bigdata.researchseminar.entities

case class Tweet(created_at: String,
                 entities: Entities,
                 full_text: String,
                 id_str: String,
                 lang: String,
                 quoted_status: QuotedStatus,
                 retweet_count: BigInt,
                 user: User)