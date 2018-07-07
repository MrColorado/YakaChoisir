package com.yakapayer.yakascanner

import java.time.LocalDateTime
import java.util.*

data class AttendMember(
        var entry_date : Date?,
        val email : String,
        val firstname : String,
        val lastname : String,
        val ticket_number : String,
        val token : String
)