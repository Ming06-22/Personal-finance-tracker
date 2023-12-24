import requests
import json
import csv
import collections
from flask import Flask, request
from flask_restful import Api, Resource
import MiniProject as MP

app = Flask(__name__)
api = Api(app)

class Conversion(Resource):
    def get(self):
        # check argument
        try:
            base = request.args.get("base")
            name = request.args.get("name")
            date = request.args.get("date")
            description = request.args.get("description")
            amount = eval(request.args.get("amount"))
        except:
            return "Not enough arguments."
        
        # connect exchange rate API
        try:
            API_KEY = "6c0397d286c882527a143003"
            url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}"
            rate = requests.get(url).text
            rate = json.loads(rate)["conversion_rates"]["TWD"]
            
            amount *= rate
        except:
            return "API connection error!"
                
        # initial remaining budget
        record = collections.defaultdict(int)
        
        # get budget limit
        with open("MiniProject2.csv") as f:
            next(f)
            reader = csv.reader(f, delimiter = ",")
            for row in reader:
                record[row[1]] += int(row[2])
            
        # budget limit minus record amount
        with open("MiniProject1.csv") as f:
            next(f)
            reader = csv.reader(f, delimiter = ",")
            total = int(f.readline())
            
            reader = csv.reader(f, delimiter = ",")
            for row in reader:
                record[row[1]] -= int(row[4])
                
        # check remaining budget
        if (name != "income" and (name not in record or record[name] < amount)):
            return "The remaining budget is not enough!"
        
        # load record information
        with open("MiniProject1.csv", "r") as f:
            next(f)
            reader = csv.reader(f, delimiter = ",")
            total = int(f.readline())
            
            reader = csv.reader(f, delimiter = ",")
            record1, record2 = {}, collections.defaultdict(dict)
            for row in reader:
                # record based on id
                record1[int(row[0])] = [row[1], row[2], row[3], int(row[4])]
                # record based on category
                record2[row[1]][int(row[0])] = [row[2], row[3], int(row[4])]
        
        # create Record and add new record
        record = MP.Record(record1, record2)
        record.add(name, date, description, int(amount))
        
        return "Success"
        
class Budget(Resource):
    def get(self):
        record = collections.defaultdict(int)
        
        # get budget limit
        with open("MiniProject2.csv") as f:
            next(f)
            reader = csv.reader(f, delimiter = ",")
            for row in reader:
                record[row[1]] += int(row[2])
            
        # budget limit minus record amount
        with open("MiniProject1.csv") as f:
            next(f)
            reader = csv.reader(f, delimiter = ",")
            total = int(f.readline())
            
            reader = csv.reader(f, delimiter = ",")
            for row in reader:
                record[row[1]] -= int(row[4])
        
        if ("income" in record):
            del record["income"]
        
        return record

api.add_resource(Conversion, "/conversion")
api.add_resource(Budget, "/budget")

if (__name__ == "__main__"):
    app.run()