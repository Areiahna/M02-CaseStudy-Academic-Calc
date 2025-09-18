#SDEV220 
# Areiahna Cooks
# academic_calc.py

# This app accepts input for student's first & last names, & a float for student's GPA's. Using the input the app determines if the student is eligable for the Deans List or Honor Roll. If the student is not eligible for either an encouraging message will print on the screen.

import random

words_of_encouragment = ["Don't give up! There's always next semsester🤘","Stay resilient and determined⭐","BUT...I know you can do it!🤗","Don't watch the clock; do what it does. Keep going!!"]


# ask for and accept a student's last name.
last_name = input("Enter the student's LAST name: ").title()   

# quit processing student records if the last name entered is 'ZZZ'
while last_name != "ZZZ":
    
    try:
        # ask for and accept a student's first name.
        first_name = input("Enter the student's FIRST name: ").title()
        student_name = first_name+"_"+last_name
            
        # ask for and accept the student's GPA as a float.
        gpa = float(input("Enter student GPA: "))

        # test if the student's GPA is 3.5 or greater and, if so, print a message 
        if gpa >= 3.5:
            print(f"{" ".join(student_name.split('_'))} has made the Dean's List with a {gpa} GPA🥳")

        # test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.
        elif gpa >=3.25 and gpa <3.5:
            print(f"{" ".join(student_name.split('_'))} has made Honor Roll with a {gpa} GPA😎")

        else:
            print(f"\nSorry {first_name}, you did not make the Dean's list or Honor roll this semester.")
            print(f"""
            - {random.choice(words_of_encouragment)}
                """)
        
        #Prompting user to a last name. If last_name does not meet requirements for while loop, the loop will break
        last_name = str(input("\nEnter the student's last name: ")).title()

    except ValueError as e:
        print({e})

print("\nGoodbye Scholar🤓")






