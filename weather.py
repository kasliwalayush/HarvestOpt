# import requests

# def generate_weather_html(city_name):
#     response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid=660127cdb1897d3465189a8b73640bb9')
#     weather_data = response.json()

#     city = weather_data['city']['name']
#     combined_string = f"<center><h1 style = `font-family : Arial`>Weather Summary for {city}</h1></center><br>"
    

#     for entry in weather_data['list'][:3]:
#         main_data = entry['main']
#         weather = entry['weather'][0]
#         cloud_data = entry['clouds']
#         wind_data = entry['wind']
#         visibility_data = entry['visibility']

#         temperature_kelvin = main_data['temp']
#         temperature_celsius = temperature_kelvin - 273.15

#         combined_string += "<center><div style = `Arial, Helvetica, sans-serif`>"
#         combined_string += f"<b>Temperature:</b> {temperature_celsius:.2f} °C<br>"
#         combined_string += f"<b>Weather:</b> {weather['main']} ({weather['description']})<br>"
#         combined_string += f"<b>Clouds:</b> {cloud_data['all']}% coverage<br>"
#         combined_string += f"<b>Wind:</b> {wind_data['speed']} m/s<br>"
#         combined_string += f"<b>Visibility:</b> {visibility_data} meters<br>"
#         combined_string += "</div></center><br>"


#     return combined_string





import requests

def generate_weather_html(city_name):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid=660127cdb1897d3465189a8b73640bb9')
    weather_data = response.json()

    city = weather_data['city']['name']
    combined_string = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f2f2f2; /* Light gray background */
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 800px;
                margin: 0 auto;
                background-color: #fff; /* White background for the content */
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Soft shadow effect */
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }}
            th, td {{
                padding: 8px;
                text-align: left;
                border-bottom: 1px solid #ddd; /* Gray border between rows */
            }}
            th {{
                background-color: #f2f2f2; /* Light gray background for table headers */
                color: #333; /* Dark text color */
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9; /* Light gray background for even rows */
            }}
            tr:hover {{
                background-color: #f5f5f5; /* Darker gray background on hover */
            }}
        </style>
    </head>
    <body style="background-color: #e9ecef;"> <!-- Light blue-gray background for the entire page -->
        <div class="container">
            <center><h1 style="color: #007bff;">Weather Summary for {city}</h1></center>
    """

    for entry in weather_data['list'][:3]:
        main_data = entry['main']
        weather = entry['weather'][0]
        cloud_data = entry['clouds']
        wind_data = entry['wind']
        visibility_data = entry['visibility']

        temperature_kelvin = main_data['temp']
        temperature_celsius = temperature_kelvin - 273.15

        combined_string += f"""
            <table>
                <tr style="background-color: #f2f2f2; color: #333;">
                    <th colspan="2">{entry['dt_txt']}</th>
                </tr>
                <tr>
                    <td><b>Temperature:</b></td>
                    <td>{temperature_celsius:.2f} °C</td>
                </tr>
                <tr>
                    <td><b>Weather:</b></td>
                    <td>{weather['main']} ({weather['description']})</td>
                </tr>
                <tr>
                    <td><b>Clouds:</b></td>
                    <td>{cloud_data['all']}% coverage</td>
                </tr>
                <tr>
                    <td><b>Wind:</b></td>
                    <td>{wind_data['speed']} m/s</td>
                </tr>
                <tr>
                    <td><b>Visibility:</b></td>
                    <td>{visibility_data} meters</td>
                </tr>
            </table>
        """

    combined_string += """
        </div>
    </body>
    </html>
    """

    return combined_string


 









