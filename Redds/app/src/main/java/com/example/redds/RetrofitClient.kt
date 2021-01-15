package com.example.redds

import java.util.*
import retrofit2.Call
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Query


object RetrofitClient {

    val instance : Api by Lazy {

        val retrofit = Retrofit.Builder()
            .baseUrl("<enter base url here>")
            .addConverterFactory(GsonConverterFactory.create())
            .build()

        retrofit.create((Api::class.java))
    }
}