import datetime
import pytz
import pandas as pd

class User:
    
    data = [['Amount', 'Catagory', 'Day', 'Month', 'Year', 'Comment']]
    
    def __init__(self, user_name, data):
        self.user_name = user_name
        self.data = data
        print("User created for {}".format(self.user_name))
        self.df = pd.DataFrame(data[1::], columns = data[0])
    
    def add_item(self, entry):
        self.data.append(self.entry)
        
    def entry(self):
        now = datetime.datetime.now()
        amount = input("Please enter the amount spent: ")
        catagory = input("Please enter the catagory: ")
        comment = str(input("Comment on item: "))
        date = input("Current day? ").upper()
        if date == "YES" or date == "Y" or date == "YE" or date == "YEAH" or date == "YA" or date == "YH":
            self.data.append([amount, catagory, now.day, now.month, now.year, comment])
        else:
            day = input("Please enter the date in the form of DD/MM/YYYY")
            self.data.append([amount, catagory, day.split('/')[0], day.split('/')[1], day.split('/')[2], comment])
            
    def total_amount(self):
        df1 = self.df.drop_duplicates(subset = ['month', 'year'])
        the_list = df1[['month', 'year']].values.tolist()
        for i in the_list:
            print("You have spent {} in the month {}-{}".format(df.loc[(df["month"] == i[0]) & (df["year"] == i[1]), "Amount"].sum(), i[0], i[1]))
    
    def look_up(self):
        