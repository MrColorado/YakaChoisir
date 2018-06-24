package com.yakapayer.yakascanner

import android.os.Bundle
import android.support.v4.app.Fragment
import android.support.v7.widget.LinearLayoutManager
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.google.gson.GsonBuilder
import kotlinx.android.synthetic.main.fragment_event_members_list.*
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory


class EventMembersListFragment : Fragment(), TextWatcher {

    private val data = ArrayList<AttendMember>()
    private var adapter: EventMembersListRecyclerAdapter? = null

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_event_members_list, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        // init ListView (basically optimizations and orientation)
        event_members_list_recycler_view.setHasFixedSize(true)
        event_members_list_recycler_view.layoutManager = LinearLayoutManager(
                activity,
                LinearLayoutManager.VERTICAL,
                false
        )

        fillDataList()

        adapter = EventMembersListRecyclerAdapter(context!!, data)
        event_members_list_recycler_view.adapter = adapter

        // Search Bar
        event_members_list_search_bar.addTextChangedListener(this)
    }

    /**
     * Makes Retrofit GET request to get all EventMembers items
     */
    private fun fillDataList() {
        // TODO Retrofit request
        val jsonConverter = GsonConverterFactory.create(GsonBuilder().create())
        val retrofit = Retrofit.Builder().baseUrl("http://127.0.0.1:8000/api/v1/").addConverterFactory(jsonConverter).build()
        val service: WSInterface = retrofit.create(WSInterface::class.java)
        val callback = object : Callback<List<AttendMember>> {
            override fun onFailure(call: Call<List<AttendMember>>?, t: Throwable?) {
                Log.d("Retrofit", "GET Request error")
            }

            override fun onResponse(call: Call<List<AttendMember>>?, response: Response<List<AttendMember>>?) {
                if (response != null) {
                    if (response.code() == 200) {
                        val responseData = response.body()
                        if (responseData != null) {
                            for (member in responseData) {
                                Log.d("GET REQUEST", member.toString())
                                data.add(AttendMember(
                                        member.entry_date,
                                        member.email,
                                        member.firstname,
                                        member.lastname,
                                        member.ticket_number,
                                        member.token))
                            }
                        }
                    }
                }
            }
        }
        service.getAttendingMembers().enqueue(callback)
    }

    override fun afterTextChanged(s: Editable?) {
        // TODO filter list with search bar.
    }


    override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
        // do nothing
    }

    override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
        // do nothing
    }
}
