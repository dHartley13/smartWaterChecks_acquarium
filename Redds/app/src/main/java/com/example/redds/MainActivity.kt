package com.example.redds

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.widget.Toast
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import java.text.DateFormat

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

    RetrofitClient.instance.readTemp(
        degreesFarenheit = Float,
        degreesCelsius = Float,
        ts = DateFormat.FULL
    )
        .enqueue(object: Callback<DefaultResponse> {

            override fun onFailure(call: Call<DefaultResponse>, t: Throwable) {
                Toast.makeText(applicationContext, t.message, Toast.LENGTH_LONG).show()
            }

            override fun onResponse(call: Call<DefaultResponse>, response: Response<DefaultResponse>) {
                //Toast.makeText(applicationContext, response.body()?.ts, Toast.LENGTH_LONG).show()
            }
        })
        }

    }

}