#DoomsDay Algorithm
import math #need this libary for math.floor()
#NOTES-------------------------------------------------------------------
#we ascribe a numerical integer value to each day
#0 = sunday, 1 = monday, 2 = tuesday, 3 = wednesday, 4 = thursday, 5 = friday, 6 = saturday
#END OF NOTES-----------------------------------------------------------


#calcules the anchor day of a century given a number 
def century_anchor_day(year): #parameters are int (correct)
    #firstly we get the century we are in
    century = math.floor(year / 100) #note: math.floor rounds down (nearest int)
    temp = (century % 4) * 2 #account for 4 century cyclesss
    day = (9 - temp) % 7 #modulus 7 to get the weekday
    return day

#calculates the anchor day of a year (works?)
def year_anchor_day(year): #parameters are int 
    century_anchor = century_anchor_day(year) #calls above function
    year = year % 100 #gets the year in the century i.e. 1697 -> 97
    leap_years = math.floor(year /4) #gets the number of leap years
    temp = year + leap_years + century_anchor #gets the total number of days 
    day = temp % 7 #now we get the day in the week
    return day

#determins if our year is a leap year, returns a boolean
def leap_year(year): #parameters are int
    if(year % 4 == 0): #checks if evenly divisible by 4
        if(year % 100 == 0): #a year that is divisible by 100 is only a leap year if it is also divisible by 400
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
            
    
    

def nearest_doomsday(year, month):
    
    is_leap_year = leap_year(year) #uses above function

    #returns the nearest dommsday based on the month (jan/feb also depend on if the year is a leap year)
    if(month == 1):
        if(is_leap_year):
            return 3
        else:
            return 4
    if(month == 2):
        if(is_leap_year):
            return 29
        else:
            return 28
    if(month == 3):
        return 0
    if(month == 4):
        return 4
    if(month == 5):
        return 9
    if(month == 6):
        return 6
    if(month == 7):
        return 11
    if(month == 8):
        return 8
    if(month == 9):
        return 5
    if(month == 10):
        return 10
    if(month == 11):
        return 7
    if(month == 12):
        return 12

        print("ERROR, CLOSESET DOOMSDAY FUNCTION") #this should never happen, month should be a number from 1-12 (inclusive) 
        return 0
                
    
    
    


#function that calculates the day from the day/month/year input
def get_day(day, month, year): #paramaters are int int int
    print("starting calculation")
    nearest_d = nearest_doomsday(year, month)
    anchor = year_anchor_day(year)

    difference = day - nearest_d
    temp = anchor + difference + 35
    new_day = temp % 7

    return new_day

#just prints the day to console given the day as a numerical value 
def print_day(day):
    if(day == 0):
        print("Sunday")
    if(day == 1):
        print("Monday")
    if (day == 2):
        print("Tuesday")
    if (day == 3):
        print("Wednesday")
    if(day == 4):
        print("Thursday")
    if(day == 5):
        print("Friday")
    if(day == 6):
        print("Saturday") 
    

            
    
    
    
    



#MAIN----------------------------------------------------------------------------------------------
print("Please enter the date in the format dd/mm/yyyy")
input_string = input() #no input checking so it will crash if you put in something wrong 
#get the day from the input 
day_string = str(input_string[0] + input_string[1])
day = int(day_string)
#get the month 
month_string = str(input_string[3] + input_string[4])  
month = int(month_string)
#get the year
year_string = str(input_string[6] + input_string[7]  + input_string[8] + input_string[9])  
year = int(year_string)
#end of input formatting
#start of actual calculations 
day_num = get_day(day, month, year) #calculates the day_num of that day/month/year (see notes for what numerical value is what day)
print_day(day_num) #prints the day out in a human-understandable way 
#END_MAIN----------------------------------------------------------------------------------------




