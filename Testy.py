import requests
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='./') 

@app.route('/', methods=['GET', 'POST'])  # for requesting form data 
# defining a function name which returns the rendered html code 
def name():
    if request.method == 'POST':
        zippy = request.form.get('zipcode')
        newCity = findCity(zippy)
        print(type(findCity(zippy)))
        #for key in newCity:
            #print("key -" + key)
        return render_template("./name.html", zipcode=zippy, findCity=newCity) 
    else:
        return render_template("./name.html") 

def findCity(zipcode):
    zipcode = 78758
    url = "http://api.zippopotam.us/us/" + str(zipcode)

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.json())
    return response.json()


# for running the app 
if __name__ == "__main__": 
    app.run(debug=True) 