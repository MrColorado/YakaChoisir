package com.yakapayer.yakascanner

/**
 * Django REST API contains META and OBJECTS fields in JSON response instead of raw list.
 */
data class EventMembersFullRequest (
        val meta : Any, // this is the field which we want to ignore
        val objects : List<AttendMember> // and this is the list we would like to get without doing all of this adapter data class.
)