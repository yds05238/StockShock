
from flask import Flask, request, render_template, url_for
import json
from os import path
from algoliasearch import algoliasearch


app = Flask(__name__)

# ADD MORE ROUTES :)
stock_id_count = 0
stocks = {
}

client = algoliasearch.Client("JURH1YKWL1", "9911f4e9f4dfe6ccca41dae0a9421d76")

index = client.init_index('company_data')
index.clear_index()
data = json.load(open('companies.json'))
index.add_objects(data)

index.set_settings({"searchableAttributes":["Company"]})

def algsearch(name):
    res = {}
    result = index.search('"' + str(name) + '"')
    for hit in result["hits"]:
        res["Company"] = hit["Company"]
        res["Ticker"] = hit["Ticker"]
        res["Price"] = hit["Price"]
        res["Dividend Yield"] = hit["Dividend Yield"]
        res["Market Cap ($M)"] = hit["Market Cap ($M)"]
        res["P/E Ratio"] = hit["P/E Ratio"]
        res["Payout Ratio"] = hit["Payout Ratio"]
        
    return json.dumps(res)

@app.route('/')
def home():
  return render_template("home.html"), 200

  
@app.route('/requests', methods=["GET", "POST"])
def result():
  if request.method == 'POST':
    company_name = request.form.get('name')
    com = json.loads(algsearch(company_name))
    return render_template("result.html", result = com), 201
  else:
    return '''<form method = "POST">
          Company Name: <input type="text" name="name"><br>
          <input type="submit" value="Submit">
          </form>
          ''', 200


  
if __name__ == '__main__':
   app.run(debug = True)