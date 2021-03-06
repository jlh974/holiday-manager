import datetime
import json
from os import remove
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
import html 


# # -------------------------------------------
# # Modify the holiday class to 
# # 1. Only accept Datetime objects for date.
# # 2. You may need to add additional functions
# # 3. You may drop the init if you are using @dataclasses
# # --------------------------------------------
class Holiday:
      
    def __init__(self,name, date):
        #Your Code Here
        self._name = name
        self._date = datetime.datetime.strptime(date, '%m-%d-%Y')        
    
    def __str__ (self):
        # String output
        # Holiday output when printed.

        return f'{self._name} {self._date.strftime("%m-%d-%Y")}' 

aHoliday = Holiday('Pirate Day','02-23-2022')
a2Holiday = Holiday('Easter','04-17-2022')
print(aHoliday)  
# # -------------------------------------------
# # The HolidayList class acts as a wrapper and container
# # For the list of holidays
# # Each method has pseudo-code instructions
# # --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []
   
    def addHoliday(self, holidayObj):
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday
        type(holidayObj)
        addHoliday = self.innerHolidays.append(holidayObj)
        print('Holiday has been added.')

    def findHoliday(self, HolidayName, Date):
    # Find Holiday in innerHolidays
    # Return Holiday
        for holiday in self.innerHolidays:
            if holiday._name == HolidayName and holiday._date.strftime("%m-%d-%Y") == Date:
                return holiday
        print('Holiday not found.')
                
    def removeHoliday(self, HolidayName, Date):
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday
        for i in range(len(self.innerHolidays)):
            holiday = self.innerHolidays[i]
            if holiday._name == HolidayName and holiday._date.strftime("%m-%d-%Y") == Date:
                del self.innerHolidays[i]
            else:
                print('Holiday not found2')        

    def read_json(holidays.json):
        # Read in things from json file location
        with open('holidays.json') as json_file:
            holidays = json.load(json_file)
            # for i in holidays['holidays']:
                #json.loads(holidays.read())
            #Use addHoliday function to add holidays to inner list.
            addHoliday(*holidays).self.innerHoliday.append(HolidayObj)
            return [self.innerHolidays]
            


        
        
# aHolidayList = HolidayList()
# aHolidayList.addHoliday(aHoliday)
# aHolidayList.addHoliday(a2Holiday)
# print(aHolidayList.innerHolidays)
# tempHoliday = aHolidayList.findHoliday('Pirate Day','02-23-2022')
# print(tempHoliday)
# bHoliday = aHolidayList.removeHoliday('Easter','04-17-2022')
# print(aHolidayList.innerHolidays)

        # def save_to_json(filelocation):
        # # Write out json file to selected file.
        #     with open("holidays.json", "w") as writeJSON:
        #         json.dump(holiday, writeJSON)


#             def scrapeHolidays(url):
#                 # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
#                 # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
#                 # Check to see if name and date of holiday is in innerHolidays array
#                 # Add non-duplicates to innerHolidays
#                 # Handle any exceptions.  
#                 response = requests.get(url)
#                 return response.text
                    
#             response = requests.get("https://www.timeanddate.com/holidays/us/2020")
#                 for i 
#             print(response.status_code)

#             html = scrapeHolidays("https://www.timeanddate.com/holidays/us/2020")
#             soup = BeautifulSoup(html,'html.parser')
#             table = soup.find('table',attrs = {'class':'table'})
#             holidays = []
#             for row in table.find_all_next('tr'):
#                     cells = row.find_all_next('a')
#                     holiday = {}
#                     #holiday['Date'] = cells[0].string
#                     holiday['Holiday'] = cells[0].string
#                     holidays.append(holiday)

#             list(holidays)
#             print(holidays)

            
# def numHolidays():
#         # Return the total number of holidays in innerHolidays
    
#         def filter_holidays_by_week(year, week_number):
#         # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
#         holidays = list(map(lambda x: dt.strptime(x,weekNum), innerHolidays))
#         # Week number is part of the the Datetime object
#         # Cast filter results as list
#         list(holidays)
#         # return your holidays
#         return holidays

#             def displayHolidaysInWeek(holidayList):
#         # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
#         # Output formated holidays in the week. 
#         # * Remember to use the holiday __str__ method.

#     #def getWeather(weekNum):
#         # Convert weekNum to range between two digits
#         # Use Try / Except to catch problems
#         # Query API for weather in that week range (uso definition rather than rolling 7 day week)
#         # Format weather information and return weather string.

#                 def viewCurrentWeek():
#                     # Use the Datetime Module to look up current week and year
#                     # Use your filter_holidays_by_week function to get the list of holidays 
#                     # for the current week/year
#                     # Use your displayHolidaysInWeek function to display the holidays in the week
#                     # Ask user if they want to get the weather
#                     # If yes, use your getWeather function and display results



#                     def main():
#                         # Large Pseudo Code steps
#                         # -------------------------------------
#                         # 1. Initialize HolidayList Object
#                         # 2. Load JSON file via HolidayList read_json function
#                         # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
#                         # 3. Create while loop for user to keep adding or working with the Calender
#                         # 4. Display User Menu (Print the menu)
#                         # 5. Take user input for their action based on Menu and check the user input for errors
#                         # 6. Run appropriate method from the HolidayList object depending on what the user input is
#                         # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


#                         if __name__ == "__main__":
#                             main()

# # Additional Hints:
# # ---------------------------------------------
# # You may need additional helper functions both in and out of the classes, add functions as you need to.
# #
# # No one function should be more then 50 lines of code, if you need more then 50 lines of code
# # excluding comments, break the function into multiple functions.
# # You can store your raw menu text, and other blocks of texts as raw text files 
# # and use placeholder values with the format option.
# # Example:
# # In the file test.txt is "My name is {fname}, I'm {age}"
# # Then you later can read the file into a string "filetxt"
# # and substitute the placeholders 
# # for example: filetxt.format(fname = "John", age = 36)
# # This will make your code far more readable, by seperating text from code.