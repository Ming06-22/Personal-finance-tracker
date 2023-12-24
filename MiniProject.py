import datetime
import csv
import pandas as pd
from IPython.display import display
import collections

# with open("MiniProject1.csv", "w", newline = "") as f:
#     writer = csv.writer(f)
#     writer.writerow(["id", "category", "date", "description", "amount"])

# with open("MiniProject2.csv", "w", newline = "") as f:
#     writer = csv.writer(f)
#     writer.writerow(["id", "name", "limit"])

class Budget():
    # initialize the budget
    def __init__(self, budget_record):
        self.budget_record = budget_record
    
    # adding new budget
    def add(self, budget_id, budget_name, budget_limit):
        with open("MiniProject2.csv", "a", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow([budget_id, budget_name, budget_limit])
            
        self.budget_record[budget_id] = [budget_name, budget_limit]
            
    # display all the budget information
    def display(self):
        print("")
        for id, b in budget_record.items():
            print(f"({id}) Budget name: {b[0]}, budget limit: {b[1]}")
            
    # delete a existed budget by id
    def delete(self, n):
        for nn in range(n + 1, len(budget_record) + 1):
            self.budget_record[nn - 1] = self.budget_record[nn]
        del self.budget_record[len(budget_record)]
        with open("MiniProject2.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "limit"])
            for i, b in self.budget_record.items():
                writer.writerow([i, b[0], b[1]])
    
    # update a budget by id
    def update(self, n, budget_name, budget_limit):
        self.budget_record[n] = [budget_name, budget_limit]
        with open("MiniProject2.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "limit"])
            for i, b in self.budget_record.items():
                writer.writerow([i, b[0], b[1]])
        
class Record():
    # initialize record
    def __init__(self, record1, record2):
        self.record_base_on_id = record1
        self.record_base_on_category = record2
    
    # add record
    def add(self, budget_name, date, description, amount):
        # get the id of the insert record
        if (len(self.record_base_on_category[budget_name]) >= 1):
            id = max(self.record_base_on_category[budget_name].keys()) + 1
        else:
            id = len(self.record_base_on_id) + 1
        if (id < len(self.record_base_on_id) + 1):
            # change all the record id after new record
            for i in range(len(self.record_base_on_id) + 1, id, -1):
                category = self.record_base_on_id[i - 1][0]
                self.record_base_on_category[category][id + 1] = self.record_base_on_category[category][id]
            del self.record_base_on_category[category][id]
            
            for i in range(len(self.record_base_on_id) + 1, id, -1):
                self.record_base_on_id[i] = self.record_base_on_id[i - 1]
            
            self.record_base_on_id[id] = [budget_name, date, description, amount]
            self.record_base_on_category[budget_name][id] = [date, description, amount]
        else:
            self.record_base_on_id[id] = [budget_name, date, description, amount]
            self.record_base_on_category[budget_name] = [id, date, description, amount]
        
        with open("MiniProject1.csv", "w", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "category", "date", "description", "amount"])
            writer.writerow([0])
            for i in range(1, len(self.record_base_on_id) + 1):
                r = self.record_base_on_id[i]
                writer.writerow([i, r[0], r[1], r[2], r[3]])
    
    # display all the record
    def display(self):
        temp = ""
        print("")
        for i in range(1, len(self.record_base_on_id) + 1):
            r = self.record_base_on_id[i]
            if (self.record_base_on_id[i][0] != temp):
                print(f"{r[0]}")
                temp = r[0]
            print(f"    id: {i}, date: {r[1]}, description: {r[2]}, amount: {r[3]}")
    
    # delete an existed record by id
    def delete(self, id):
        for i in range(id, len(self.record_base_on_id)):
            category = self.record_base_on_id[i][0]
            self.record_base_on_category[category][i - 1] = self.record_base_on_category[category][i]
            del self.record_base_on_category[category][i]
            
            self.record_base_on_id[i] = self.record_base_on_id[i + 1]
        category = self.record_base_on_id[len(self.record_base_on_id)][0]
        del self.record_base_on_category[category][len(self.record_base_on_id)]
        del self.record_base_on_id[len(self.record_base_on_id)]
    
        with open("MiniProject1.csv", "w", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "category", "date", "description", "amount"])
            writer.writerow([total])
            for i in range(1, len(self.record_base_on_id) + 1):
                r = self.record_base_on_id[i]
                writer.writerow([i, r[0], r[1], r[2], r[3]])
    
    # update an existed record by id
    def update(self, id, budget_name, date, description, amount):
        temp = self.record_base_on_id[id][0]
        if (temp == budget_name):
            self.record_base_on_id[id] = [budget_name, date, description, amount]
            
            del self.record_base_on_category[temp][id]
            self.record_base_on_category[budget_name][id] = [date, description, amount]
        else:
            self.delete(id)
            self.add(budget_name, date, description, amount)
        
        with open("MiniProject1.csv", "w", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "category", "date", "description", "amount"])
            writer.writerow([total])
            for i in range(1, len(self.record_base_on_id) + 1):
                r = self.record_base_on_id[i]
                writer.writerow([i, r[0], r[1], r[2], r[3]])
    
if (__name__ == "__main__"):
    limit = {}
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
            
    # load budget information
    with open("MiniProject2.csv", "r") as f:
        next(f)
        reader = csv.reader(f, delimiter = ",")
        budget_record = {}
        for row in reader:
            # budget based on id
            budget_record[int(row[0])] = [row[1], int(row[2])]
            limit[row[1]] = int(row[2])
            
    # use calss Budget and class Record to deal with operations
    budget = Budget(budget_record)
    record = Record(record1, record2)
    
    while (True):
        # display three category of operation
        print("-" * 20)
        print("(1) Budget")
        print("(2) Record")
        print("(3) Exit")
        print("-" * 20)
        choice = input("Please enter the number of service: ")
        
        while (choice not in [str(n) for n in range(1, 4)]):
            print("\nPlease enter 1 to 3!!!\n")
            choice = input("Please enter the number of service: ")
        
        # doing budget operations
        if (choice == "1"):
            # five operations of budget
            print("-" * 20)
            print("(1) Add")
            print("(2) Delete")
            print("(3) Modify")
            print("(4) Display")
            print("(5) Exit")
            print("-" * 20)
            
            # check for valid choice
            choice = input("Please enter the number of service: ")
            while (choice not in [str(n) for n in range(1, 6)]):
                print("\nPlease enter 1 to 5!!!\n")
                choice = input("Please enter the number of service: ")
                
            # add new budget
            if (choice == "1"):
                # get the name of budget
                name = input("Please enter the budget name: ")
                # get valid integer limit
                limit = input("Please enter the budget limit: ")
                while (not limit.isnumeric() or int(limit) != float(limit) or int(limit) <= 0):
                    print("\nPlease enter an positive integer!")
                    limit = input("\nPlease enter the budget limit: ")
                    
                # call for adding and display
                budget.add(len(budget.budget_record) + 1, name, limit)
                print("\nAfter adding...")
                budget.display()
            # delete an existed budget
            elif (choice == "2"):
                # display all the budget information and get valid id to delete
                budget.display()
                n = input("Please enter the number of budget you want to delete: ")
                while (not n.isnumeric() or int(n) != float(n) or n not in [str(nn) for nn in range(1, len(budget.budget_record) + 1)]):
                    print(f"\nPlease enter a integer between 1 and {len(budget.budget_record)}!\n")
                    n = input("Please enter the number of budget you want to delete: ")
                    
                # call for deleting and display
                budget.delete(int(n))
                print("\nAfter deleting...")
                budget.display()
            # modify an existed budget
            elif (choice == "3"):
                # display all the budget information and get valid id to modify
                budget.display()
                n = input("Please enter the number of budget you want to modify: ")
                while (not n.isnumeric() or int(n) != float(n) or n not in [str(nn) for nn in range(1, len(budget.budget_record) + 1)]):
                    print(f"\nPlease enter a integer between 1 and {len(budget.budget_record)}!\n")
                    n = input("Please enter the number of budget you want to modify: ")
                    
                # get new budget name
                name = input("Please enter the new name of the budget: ")
                # get new budget limit
                limit = input("Please enter the new limit of the budget: ")
                while (not limit.isnumeric() or int(limit) != float(limit) or int(limit) <= 0):
                    print("\nPlease enter an positive integer!\n")
                    limit = input("Please enter the budget limit: ")
                    
                # call for modifying and display
                budget.update(int(n), name, int(limit))
                print("\nAfter modifying...")
                budget.display()
            # display all the budget information
            elif (choice == "4"):
                budget.display()
            # back to choose three basic category
            elif (choice == "5"):
                continue
        # doing record operations
        elif (choice == "2"):
            # five operation of record
            print("-" * 20)
            print("(1) Add")
            print("(2) Delete")
            print("(3) Modify")
            print("(4) Display")
            print("(5) Exit")
            print("-" * 20)
            
            # check for valid choice
            choice = input("Please enter the number of service: ")
            while (choice not in [str(n) for n in range(1, 6)]):
                print("\nPlease enter 1 to 5!!!\n")
                choice = input("Please enter the number of service: ")
                
            # add new record
            if (choice == "1"):
                # display budget
                budget.display()
                # get category of budget to the record
                choice = input("Please enter which kind of budget you want to add: ")
                while (not choice.isnumeric() or int(choice) != float(choice) or choice not in [str(n) for n in range(1, len(budget.budget_record) + 1)]):
                    print(f"\nPlease enter a integer between 1 and {len(budget_record)}!\n")
                    choice = input("Please enter which kind of budget you want to add: ")
                budget_name = budget.budget_record[int(choice)][0]
                
                # get record date
                date = input("Please enter the date(ex: 2023-01-01): ")
                while (True):
                    try:
                        temp = date.split("-")
                        temp = datetime.date(int(temp[0]), int(temp[1]), int(temp[2]))
                        break
                    except:
                        print("\nPlease enter a valid date format(ex: 2023/01/01)!\n")
                        date = input("Please enter the date(ex: 2023/01/01): ")
                # get record description
                description = input("Please enter some description: ")
                # get record amount
                amount = input("Please enter the amount: ")
                while (not amount.isnumeric() or int(amount) != float(amount) or int(amount) < 0):
                    print("\nPlease enter a positive integer!\n")
                    amount = input("Please enter the amount: ")
                amount = int(amount)
                    
                # call for adding and display
                record.add(budget_name, date, description, amount)
                print("\nAfter adding...")
                record.display()
            # delete an existed record
            elif (choice == "2"):
                # display all the record information and get valid id to modify
                record.display()
                n = input("Please enter the number of the record you want to delete: ")
                while (not n.isnumeric() or int(n) != float(n) or n not in [str(nn) for nn in range(1, len(record.record_base_on_id) + 1)]):
                    print(f"\nPlease enter a positve integer between 1 and {len(record.record_base_on_id) + 1}\n")
                    n = input("Please enter the number of the record you want to delete: ")
                
                # call for deleting and display
                record.delete(int(n))
                print("\nAfter deleting...")
                record.display()
            # modify an existed record
            elif (choice == "3"):
                # display all the record information and get valid id to modify
                record.display()
                n = input("Please enter the id of the record you want to modify: ")
                while (not n.isnumeric() or int(n) != float(n) or n not in [str(nn) for nn in range(1, len(record.record_base_on_id) + 1)]):
                    print(f"\nPlease enter a positve integer between 1 and {len(record.record_base_on_id)}\n")
                    n = input("Please enter the id of the record you want to modify: ")
                    
                # get new budget id
                budget.display()
                choice = input("Please enter which kind of budget you want to add: ")
                while (not choice.isnumeric() or int(choice) != float(choice) or choice not in [str(n) for n in range(1, len(budget.budget_record) + 1)]):
                    print(f"\nPlease enter a integer between 1 and {len(budget.budget_record)}!\n")
                    choice = input("Please enter which kind of budget you want to add: ")
                budget_name = budget.budget_record[int(choice)][0]
                
                # get new date
                date = input("Please enter the date(ex: 2023-01-01): ")
                while (True):
                    try:
                        temp = date.split("-")
                        temp = datetime.date(int(temp[0]), int(temp[1]), int(temp[2]))
                        break
                    except:
                        print("\nPlease enter a valid date format(ex: 2023-01-01)!\n")
                        date = input("Please enter the date(ex: 2023-01-01): ")
                # get new description
                description = input("Please enter some description: ")
                # get new amount
                amount = input("Please enter the amount: ")
                while (not amount.isnumeric() or int(amount) != float(amount) or int(amount) < 0):
                    print("\nPlease enter a positive integer!\n")
                    amount = input("Please enter the amount: ")
                amount = int(amount)
                
                # call for modifying and display
                print("\nAfter modifying...")
                record.update(int(n), budget_name, date, description, amount)
                record.display()
            # display all the record information
            elif (choice == "4"):
                record.display()
            # back to choose three basic category
            elif (choice == "5"):
                continue
        # leave the program
        else:
            print("\nThank you! Have a nice day!")
            break