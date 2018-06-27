package com.yakapayer.yakascanner

import java.util.*

data class AttendMember(
        val entry_date : Date?,
        val email : String,
        val firstname : String,
        val lastname : String,
        val ticket_number : String,
        val token : String
)