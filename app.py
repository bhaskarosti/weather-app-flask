from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    weather={
        "city":"",
        "temperature":"",
        "humidity":"",
        "minTemp":"",
        "maxTemp":"",
        "pressure":"",
        "feelslike":"",
        "country":"",
        "logo":"",
        "description":"",
        "visibility":"hidden",
        "errorPrompt":"hidden"
    }
    if request.method == 'POST':
        try:
            cityName = request.form.get('city')
            data = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + cityName + '&appid=f82167d6353cdc9495dc2149195ecdda&units=metric')
            jsonData = data.json()
            
            weather['city']=cityName.title()
            weather['temperature'] = float(jsonData['main']['temp'])
            weather['humidity'] = float(jsonData['main']['humidity'])
            weather['minTemp'] = float(jsonData['main']['temp_min'])
            weather['maxTemp'] = float(jsonData['main']['temp_max'])
            weather['pressure'] = float(jsonData['main']['pressure'])
            weather['feelsLike'] = float(jsonData['main']['feels_like'])
            weather['country'] = jsonData['sys']['country'].lower()
            weather['logo'] = jsonData['weather'][0]['icon']
            weather['description'] = jsonData['weather'][0]['description'].title()
            weather['visibility']=""

        except Exception as e:
            weather['errorPrompt']=""
            return render_template('testModule.html',weather=weather)            
    return render_template('testModule.html',weather=weather)


if __name__ == "__main__":
    app.run(debug=True)
