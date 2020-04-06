package ru.hse.bigdata.researchseminar.entities

case class User(contributors_enabled: Option[Boolean],
                created_at: Option[String],
                description: Option[String],
                favourites_count: Option[BigInt],
                followers_count: Option[BigInt],
                friends_count: Option[BigInt],
                id_str: Option[String],
                name: Option[String],
                screen_name: Option[String],
                statuses_count: Option[BigInt],
                lang: Option[String],
                geo_enabled: Option[Boolean],
                verified: Option[Boolean])
