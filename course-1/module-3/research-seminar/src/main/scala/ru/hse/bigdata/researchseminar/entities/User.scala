package ru.hse.bigdata.researchseminar.entities

case class User(contributors_enabled: Boolean,
                created_at: String,
                description: String,
                favourites_count: BigInt,
                followers_count: BigInt,
                friends_count: BigInt,
                id_str: String,
                screen_name: String,
                statuses_count: BigInt,
                verified: Boolean)
