package com.yakapayer.yakascanner

import android.Manifest
import android.content.Context.MODE_PRIVATE
import android.content.Intent
import android.content.SharedPreferences
import android.content.SharedPreferences.Editor
import android.content.pm.PackageManager
import android.os.Bundle
import android.support.v4.app.ActivityCompat
import android.support.v4.app.Fragment
import android.support.v4.app.FragmentManager
import android.support.v4.content.ContextCompat
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import kotlinx.android.synthetic.main.fragment_choose_event.*


class ChooseEventFragment : Fragment() {
    var data : ArrayList<AttendMember>
    init {
        data = ArrayList()
        Log.d("TESTINGS", "init")
    }
    val dataBundle = Bundle()
    private val ZBAR_CAMERA_PERMISSION = 1

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_choose_event, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        fragment_choose_event_sendTokenButton.setOnClickListener{
            if (event_choose_token_editText.text.isEmpty()) {
                Toast.makeText(context, "Please choose an event token.", Toast.LENGTH_LONG).show()
                return@setOnClickListener
            }
            dataBundle.putString("token", event_choose_token_editText.text.toString())
            launchFragment(EventMembersListFragment())
        }

        fragment_choose_event_scan_button.setOnClickListener {
            if (ContextCompat.checkSelfPermission(context!!, Manifest.permission.CAMERA)
                    != PackageManager.PERMISSION_GRANTED) {
                val permissions = arrayOf(Manifest.permission.CAMERA)
                ActivityCompat.requestPermissions(activity!!,
                        permissions, ZBAR_CAMERA_PERMISSION)
            } else {
                launchFragment(ScanQRCodeFragment())
            }
        }
    }

    private fun launchFragment(fragment: Fragment) {
        dataBundle.putSerializable("data", data)
        fragment.arguments = dataBundle
        Log.d("TESTINGS", data.toString())

        val fragmentTransaction = fragmentManager!!.beginTransaction()
        fragmentTransaction.replace(R.id.main_container, fragment).addToBackStack(null)
        fragmentTransaction.commit()
    }
}
