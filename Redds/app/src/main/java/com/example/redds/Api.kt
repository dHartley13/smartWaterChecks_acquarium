package com.example.redds

import retrofit2.http.GET;
import retrofit2.http.Query


interface Api {

    fun <T> lazy(
        mode: LazyThreadSafetyMode,
        initializer: () -> T
    ): Lazy<T>

    @GET("readTemp")
    fun readTemp(
        @Query("degreesCelsius") degreesCelsius: Float.Companion,
        @Query("degreesFarenheit") degreesFarenheit: Float.Companion,
        @Query("ts") ts: Int
    ):retrofit2.Call<DefaultResponse>
}