import random
print("WELCOME")
print("TO")
print("THE FORTUNE TELLER!")
name = input("What is your name? ")
month = input("What month is it? ")
early = ["You are going to code more this year","This year, you are going to achieve great things.","Your birthday is going to be/was a great one.","You will know coding as one of your basic languages.","Tommorow it will be a great day.","You will reccomend coding to somebody in the next 5 years."]
early_middle = ["You will have a great winter.","You will code all the time","Summer is going to be great.","It is going to be very hot in the next few days.","You will have a lot of fun during the summer."]
middle = ["You will learn a new coding language next year.","Your grades will go up.","Today will be a great day.","You will have a shy start on the school year.","You will have fun during you winter break.","You will read a new book next week.","You will take a test in the following weeks."]
last = ["It will be very cold at night.","The days will grow longer!","You will celebrate the new years in the next month(s).","You will watch a christmas movie or christmas game","You will code more next year.","You will get to see at least a photo of snow or real snow. Maybe a video or a painting.","You will read a book today.","You will get bored."]
if month == "January" or month == "February" or month  == "March":
        print(name+", "+random.choice(early))
elif month == "April" or month == "May" or month == "June":
        print(name+", "+random.choice(early_middle))
elif month == "July" or month == "August" or month == "September":
        print(name+", "+random.choice(middle))
elif month == "October" or month == "November" or month == "December":
        print(name+", "+random.choice(last))
print("THANK YOU!")