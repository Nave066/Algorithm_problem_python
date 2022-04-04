from datetime import date
import  re


def regex_func(fn, ln, mob, today):
    """
    :param fn: Firstname which user entered
    :param ln: Lastname entered
    :param mob: Mobile number of the user
    :param today: Today's date automatically taken by system
    :return: The required Statement with the changed details of the user
    """
    print("Hello {0}, We have your full name as {0} {1} in our system.".format(fn, ln))
    print("Your Contact number is 91-{}".format(mob))
    print("Please let us know, in case of any clarification. Thank you BridgeLabz {}".format(today))


if __name__ == "__main__":
    re_fname = input("PLease enter First name: ")
    firstname = re.findall("^[A-Z][a-z]+[ ]?[A-z]*$", re_fname)
    if firstname:
        print("Valid Firstname")
    else:
        print("Invalid Firstname")
    re_lname = input("Please Enter Last name: ")
    lastname = re.findall("^[A-Z][a-z]+[ ]?[A-z]*$", re_lname)
    if lastname:
        print("Valid Lastname")
    else:
        print("Invalid Lastname")
    re_mob = input("Enter Your Mobile Number: ")
    mobile = re.findall("^[6789][0-9]{9}$", re_mob)
    if mobile:
        print("Valid Mobile Number")
    else:
        print("Invalid Mobile Number")
    dt_input = date.today()
    todayinput = dt_input.strftime("%d/%m/%Y")
    if firstname and lastname and mobile:
        regex_func(re_fname, re_lname, re_mob, todayinput)
    else:
        print("Error in user input format")
