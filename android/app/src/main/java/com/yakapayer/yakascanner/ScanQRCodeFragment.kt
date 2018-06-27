package com.yakapayer.yakascanner

import android.os.Bundle
import android.support.v4.app.Fragment
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import com.google.zxing.BarcodeFormat
import com.google.zxing.Result
import me.dm7.barcodescanner.zxing.ZXingScannerView

class ScanQRCodeFragment : Fragment(), ZXingScannerView.ResultHandler {

    private var data : ArrayList<AttendMember>? = null

    private var scannerView : ZXingScannerView? = null

    private val FLASH_STATE = "FLASH_STATE"
    private val AUTO_FOCUS_STATE = "AUTO_FOCUS_STATE"
    private val SELECTED_FORMATS = "SELECTED_FORMATS"
    private val CAMERA_ID = "CAMERA_ID"

    private var flash: Boolean = false
    private var autoFocus: Boolean = false
    private var selectedIndices: ArrayList<Int>? = null
    private var cameraId = -1

    /**
     * ZXing Scan result function
     */
    override fun handleResult(rawResult: Result?) {
        if (rawResult == null) {
            Toast.makeText(context, "Scan failed!", Toast.LENGTH_LONG).show()
            return
        }
        Log.d("TESTINGS", "result is %s".format(rawResult.text))
        val member : AttendMember? = getMatchingAttendMember(rawResult.text)
        val message =
                if (member == null)
                    "INVALID TICKET!"
                else
                    "VALID TICKET: %s %s!".format(member.firstname, member.lastname)
        Toast.makeText(context, message, 2 * Toast.LENGTH_LONG).show()
    }

    private fun getMatchingAttendMember(ticket_number: String): AttendMember? {
        Log.d("TESTINGS", data.toString())
        for (member in data!!) {
            if (ticket_number == member.ticket_number)
                return member
        }
        return null
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setHasOptionsMenu(true)
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              state: Bundle?): View? {
        data = arguments!!.getSerializable("data") as ArrayList<AttendMember>
        Log.d("QRCODE", data.toString())

        scannerView = ZXingScannerView(activity)
        if(state != null) {
            flash = state.getBoolean(FLASH_STATE, false)
            autoFocus = state.getBoolean(AUTO_FOCUS_STATE, true)
            selectedIndices = state.getIntegerArrayList(SELECTED_FORMATS)
            cameraId = state.getInt(CAMERA_ID, -1)
        } else {
            flash = false
            autoFocus = true
            selectedIndices = null
            cameraId = -1
        }
        val formats = ArrayList<BarcodeFormat>()
        formats.add(BarcodeFormat.QR_CODE)
        scannerView!!.setFormats(formats)
        scannerView!!.setAspectTolerance(0.5f) // for Huawei phone compatibility (see lib README)
        return scannerView
    }

    override fun onResume() {
        super.onResume()
        scannerView!!.setResultHandler(this) // Register ourselves as a handler for scan results.
        scannerView!!.startCamera()          // Start camera on resume
    }

    override fun onPause() {
        super.onPause()
        scannerView!!.stopCamera()           // Stop camera on pause
    }
}
