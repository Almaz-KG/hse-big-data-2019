package ru.hse.bigdata.researchseminar.entities

case class UserShort(id: Long,
                     id_str: String,
                     indices: Seq[Long],
                     name: String,
                     screen_name: String)

