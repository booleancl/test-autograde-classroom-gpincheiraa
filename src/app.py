from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/info')
def country_info():
  args = request.args
  country_code = args.get('country_code')

  try:
    if country_code is None:
      print("ERROR")
      raise Exception("Error country_code is required in URL")

    #Agrega la URL de la api de países
    api_url = f"https://restcountries.com/v3.1/alpha/{country_code}?fields=name,capital,currencies,flags"

    response = requests.get(api_url)

    if response.status_code != requests.codes.ok:
      print("ERROR")
      raise Exception(response.error)

    data = response.json()
      
    country_name = data["name"]["common"]
    currency_codes = list(data['currencies'].keys())
    capital_names = data["capital"]
    flag_url = data["flags"]["png"]
    
    info={
      "name": country_name,
      "currency": currency_codes[0],
      "capital": capital_names[0],
      "flag_url": flag_url
    }
    
    return render_template('info.html', info=info)
      
  except Exception as error:
    return render_template('error.html', error=error)

@app.route('/login', methods=['GET'])
def login_form():
  return render_template('login.html')
  
@app.route('/login', methods=['POST'])
def login_post():
  print(request.form)

  return redirect('/')
