package com.yakapayer.yakascanner

import retrofit2.Call
import retrofit2.http.GET

interface WSInterface {
    @GET("event_members")
    fun getAttendingMembers() : Call<List<AttendMember>>
}