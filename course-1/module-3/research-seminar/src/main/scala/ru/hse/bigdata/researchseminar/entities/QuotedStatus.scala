package ru.hse.bigdata.researchseminar.entities

case class QuotedStatus(created_at: String,
                        entities: Entities,
                        favorite_count: BigInt,
                        full_text: String,
                        lang: String,
                        retweet_count: BigInt,
                        user: User)
