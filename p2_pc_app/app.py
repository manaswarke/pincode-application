from bottle import *
import requests
from bottle import Bottle, request, template

application = Bottle()

@application.route("/", method=["POST", "GET"])
def home():
    if request.method == "POST":
        try:
            pc = int(request.forms.get("pc"))
        except ValueError:
            return template("home.tpl", msg="please enter integers only")

        try:
            url = f"https://api.postalpincode.in/pincode/{pc}"
            res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
            data = res.json()
            if data and isinstance(data, list) and data[0]["Status"] == "Success":

                offices = data[0].get("PostOffice")
                
                if offices and len(offices) > 0:

                    first_office = offices[0]
                    name = first_office.get("Name", "N/A")
                    state = first_office.get("State", "N/A")
                    country = first_office.get("Country", "N/A")
                    
                    msg = f"Name = {name} | State = {state} | Country = {country}"
                else:
                    msg = "Location details missing in API response"
            else:
                msg = "Location not found or invalid pincode"

            return template("home.tpl", msg=msg)

        except Exception as e:
            return template("home.tpl", msg="Server or Network issue: " + str(e))
            
    else:
        return template("home.tpl", msg="")

run(application, host="localhost", port=4050, debug=True, reloader=True)