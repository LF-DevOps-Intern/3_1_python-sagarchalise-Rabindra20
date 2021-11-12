import requests

class CliAppRun():
    def __init__(self):
        self.url = "https://google.com"
   #pull data 
    def pull_data(self):
        self.response = requests.get(self.url).text
        self.save_data()
    #save data in txt file
    def save_data(self):
        file = open('data.txt', 'w')
        file.write(self.response)
        file.close()
        print("Data saved to data.txt")
        
    def run(self):
        self.pull_data()

app = CliAppRun()
app.run()



