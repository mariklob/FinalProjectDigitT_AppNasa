from flask import Flask, render_template #import
import requests #REST zaprosi
import json
app = Flask(__name__) #sozdaetsa prilojenie




@app.route("/")      #decorator otslejivaet marshrotizaciu v lask
def mars_fotos():   #function kotoryu zapuskaet decorator
    r = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/Perseverance/latest_photos?api_key=DEMO_KEY")
    jsondata = json.loads(r.text)
    photos = jsondata['latest_photos']  # sozdaem spisoj izvlekaem iz jsona etot spisok latest photos  # i etot spisok peredadim prilojeniu
    return render_template('index.html', photos=photos )

app.run(debug=True)    #zapusk aplicacii v debug rejimi otslejivat' oshibki
