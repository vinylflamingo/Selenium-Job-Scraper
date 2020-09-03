from selenium import webdriver
import time
import smtplib
import text
#define the path for the chrome webdriver
chrome_path = r"C:/web/jobListing/Selenium-Job-Scraper/chromedriver.exe"

#create a instance of the webdriver
driver = webdriver.Chrome(chrome_path)

# In here enter the URL you would like to search. This script is designed to scrape only hirebridge websites. 
driver.get("https://recruit.hirebridge.com/v3/CareerCenter/v2/?cid=7724")
time.sleep(7)
jobs = driver.find_elements_by_class_name("col-md-8.jobtitle")

print("starting keyword search")

results = []
match = []
keywords = ['QA',
            'QUALITY',
            'ASSURANCE',
            'ANALYST'.
            'DEVELOPER',
            'ENGINEER',
            'SOFTWARE'
            ]



for job in jobs:
    #print(job.text)
    results.append(job.text)
results = [word.upper() for word in results]
print(results)
time.sleep(2)
for result in results:
    print(result)
    for keyword in keywords:
        if keyword in result:
            print("Match Found")
            match.append(result)
        else:
            print(f"No match for {keyword}")
    print('\n\n')
print(match)

text.sendSms(f"{match}")


#comments about comments
