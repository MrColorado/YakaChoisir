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
import android.widget.Toast
import com.google.gson.GsonBuilder
import kotlinx.android.synthetic.main.fragment_event_members_list.*
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory


class EventMembersListFragment : Fragment(), TextWatcher {

    private var data : ArrayList<AttendMember>? = null
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

        // Search Bar
        event_members_list_search_bar.addTextChangedListener(this)
    }

    /**
     * Makes Retrofit GET request to get all EventMembers items
     * If GET Request succeed, this.data is filled up and given to RecyclerView adapter
     */
    private fun fillDataList() {
        val jsonConverter = GsonConverterFactory.create(GsonBuilder().create())
        val retrofit = Retrofit.Builder().baseUrl("https://yaka-choisir.herokuapp.com/api/v1/").addConverterFactory(jsonConverter).build()
        val service: WSInterface = retrofit.create(WSInterface::class.java)
        val callback = object : Callback<EventMembersFullRequest> {
            override fun onFailure(call: Call<EventMembersFullRequest>?, t: Throwable?) {
                Log.d("Retrofit", "GET Request error")
            }

            override fun onResponse(call: Call<EventMembersFullRequest>?, response: Response<EventMembersFullRequest>?) {
                if (response != null) {
                    if (response.code() == 200) {
                        val responseData = response.body()
                        if (responseData != null) {
                            val objectsList = responseData.objects
                            data = arguments!!.getSerializable("data") as ArrayList<AttendMember>
                            data!!.clear()
                            val token = arguments!!.getString("token")
                            for (member in objectsList) {
                                if (token == "" || member.token == token) {
                                    data!!.add(AttendMember(
                                            member.entry_date,
                                            member.email,
                                            member.firstname,
                                            member.lastname,
                                            member.ticket_number,
                                            member.token))
                                }
                            }
                            adapter = EventMembersListRecyclerAdapter(context!!, data!!)
                            event_members_list_recycler_view.adapter = adapter
                        }
                    }
                }
            }
        }
        service.getAttendingMembers().enqueue(callback)
    }

    override fun afterTextChanged(editable: Editable?) {
        filter(editable.toString())
    }

    private fun filter(text: String) {
        //new array list that will hold the filtered data
        val filteredMembers = ArrayList<AttendMember>()

        //looping through existing elements
        for (member in data!!) {
            //if the existing elements contains the search input
            val textToCompareWith = text.toLowerCase()
            if (member.firstname.toLowerCase().contains(textToCompareWith)
                    || member.lastname.toLowerCase().contains(textToCompareWith)) {
                //adding the element to filtered list
                filteredMembers.add(member)
            }
        }
        //calling a method of the adapter class and passing the filtered list
        this.adapter!!.filterList(filteredMembers)
    }


    override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
        // do nothing
    }

    override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
        // do nothing
    }
}
