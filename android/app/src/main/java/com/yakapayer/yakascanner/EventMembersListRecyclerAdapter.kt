package com.yakapayer.yakascanner

import android.content.Context
import android.support.v7.widget.RecyclerView
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView

class EventMembersListRecyclerAdapter (
        private val context: Context,
        var data: MutableList<AttendMember>) :
    RecyclerView.Adapter<EventMembersListRecyclerAdapter.ViewHolder>() {

        // the new RecyclerAdapter enforces the use of
        // the ViewHolder class performance pattern
        class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
            val eventMemberName: TextView = itemView.findViewById(R.id.event_members_list_item_name)
            val eventMemberTicket: TextView = itemView.findViewById(R.id.event_members_list_item_ticket)
        }

        override fun getItemCount(): Int {
            return data.size
        }

        // called when a new view holder is required to display a row
        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int)
                : ViewHolder {
            // create the row (list item) from a layout inflater
            var layout = R.layout.event_members_list_item
            if (data.isEmpty()) {
                Log.d("TESTINGS", "DATA EST VIDE")
                layout = R.layout.event_members_empty_list
            }
            val rowView = LayoutInflater
                    .from(context)
                    .inflate(layout, parent, false)

            // create a ViewHolder using this row view
            // return this ViewHolder. The system will make sure view holders
            // are used and recycled
            return ViewHolder(rowView)
        }

        // called when a row is about to be displayed
        override fun onBindViewHolder(holder: ViewHolder, position: Int) {
            // retrieve the item at the specified position
            val currentItem = data[position]

            // put the data
            holder.eventMemberName.text =
                    "%s %s (%s) @%s"
                    .format(currentItem.firstname, currentItem.lastname, currentItem.email, currentItem.token)
            holder.eventMemberTicket.text = currentItem.ticket_number
        }

        //This method will filter the list
        //here we are passing the filtered data
        //and assigning it to the list with notify dataset changed method
        fun filterList(filteredItems: ArrayList<AttendMember>) {
            this.data = filteredItems
            notifyDataSetChanged()
        }
    }