# smartWaterChecks_acquarium
check water conditions through the use of sensors connecting to raspberry pi

Current build reads temperature from DS18B20 waterproof temperature sensor to a raspberry Pi. 
readTemp python scripts then navigates to the directory on the raspberry Pi that the sensor writes to and exposes it to an API endpoint using Flask
Redds is the app name for the product, and will call the API endpoint and display a graph of the water temperature the DS18B20 sensor is emersed in. Currently using Retrofit2 and Gson converter to call and deserialise the API response. 
The app will also push notify/ alarm when the temperature is too high or too low


