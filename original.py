import praw, sys
import datetime
from random import shuffle


# PRAW stands for Python Reddit API Wrapper


def getOrders():

    # Hard coded list of reddit usernames

    # List of users who opted into the bot
    #users = ["SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE"];
    users = ["SAMPLE", "REMOVED2 SAMPLE", "GONE2 SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE", "REMOVED SAMPLE", "GONE SAMPLE"];
    # List of users who opted into the bot but then have not voted for > 3 days
    deserters = ["GONE2 SAMPLE", "REMOVED2 SAMPLE"];
    # List of users who have opted out of the bot after being opted in. While we attempt to remove them from users
    # this list will catch any that fall through the cracks
    blacklist = ["REMOVED2 SAMPLE"];

    # We want to remove the blacklisted users from our user pool
    for user in blacklist:
        try:
            users.remove(user);
            print("Removed " + user + " from users due to blacklist.")
        except:
            # Except clause will be thrown if the user is not in the list which is fine
            sys.stdout.write('')

    # We want to remove the deserters from our orders pool, since those will not be reliable votes and would
    # skew distributions
    for user in deserters:
        try:
            users.remove(user);
            print("Removed " + user + " from users due to deserter.")
        except:
            # Except clause will be thrown if the user is not in the list which is fine
            sys.stdout.write('')

    # And now we should remove the blacklisted users from the deserter list
    for deserter in blacklist:
        try:
            deserters.remove(deserter);
            print("Removed " + user + " from users due to blacklist.")
        except:
            # Except clause will be thrown if the user is not in the list which is fine
            sys.stdout.write('')

    orderPercentages = {
        # Commented out percentages are old orders that have the format for the picture so they don't
        # Need to be re-typed
        # Format for Python: "text": ##,
        # Format for Reddit: [text to be hyperlinked](URL)

        # "Attack [Ball State](https://i.imgur.com/lAxiSBB.png)": 0,
        # "Attack [Notre Dame](https://i.imgur.com/YFvW1em.png)": 0,
        # "Attack [Marshall](https://i.imgur.com/bH7mPZE.png)": 0,
        # "Attack [Bowling Green](https://i.imgur.com/FfazePS.png) : 0,
        # "Attack [Purdue](https://i.imgur.com/vWGBObr.png) : 0,
        # "Attack [NorthWestern](https://i.imgur.com/0B9AV1W.png):0,
        # "Attack [Norther Illinois University](https://i.imgur.com/CPk2Ced.png):0,
        # "Defend [Michigan](https://i.imgur.com/4C5A7Tf.png): 0,
        # "Defend [Toledo](https://i.imgur.com/bHume5d.png)": 0,
        # "Defend [Michigan State University](https://i.imgur.com/mubn99X.png)": 0,
        # "Defend [Western Virginia University](https://i.imgur.com/WQL3H01.png)": 0,
        # "Defend [Western Michigan University](https://i.imgur.com/EkA0hCn.png)": 0,
        # "Defend [Eastern Michigan University](https://i.imgur.com/TL6UCdv.png)": 0,
        # "Defend [Akron](https://i.imgur.com/NtlMIFI.png)": 0,
        # "Attack [Virginia Tech](https://i.imgur.com/oHCPwUF.png)": 0,
        # "Attack [Virginia](https://i.imgur.com/L0kz5ec.png)": 0,
        # "Defend [Temple](https://i.imgur.com/kZdn5YD.png)": 3,
        # "Attack [Minnesota](https://i.imgur.com/doTF3Qj.png)": 14,
        # "Attack [Central Michigan University](https://i.imgur.com/vDDXbpX.png)": 14,
        # "Defend [Madison](https://i.imgur.com/fXtGYTu.png)": 30,
        # "Attack [Rutgers](https://i.imgur.com/0B9AV1W.png)": 0,
        # "Attack [Buffalo](https://i.imgur.com/opydgmb.png)": 0,
        # "Attack [Kent State](https://i.imgur.com/3reUhZ7.png)" : 0,
        # "Attack [Pittsburgh](https://i.imgur.com/axLukh7.png)": 0,
        # "Defend [Penn State](https://i.imgur.com/5zqtmh9.png)": 0,
        # "Attack [Navy](https://i.imgur.com/zfDGqrV.png)": 0,

        "Attack [Syracuse](https://i.imgur.com/J7X1yud.png)": 20,
        "Attack [Maryland](https://i.imgur.com/aEbTJki.png)": 30,
        "Attack [University of Massachusetts](https://i.imgur.com/L9vaAQ0.png)": 20,
        "Defend [Army](https://i.imgur.com/CrC0qRq.png)": 30,
    }

    # Shuffle what order the orders are in so we are not providing the same user hte same order for consecutive days

    # empty array
    shuffledOrderPercentages = {}

    # shuffle the orders around
    shuffledOrders = list(orderPercentages.keys())
    shuffle(shuffledOrders)

    # create a key of order and percentage
    for key in shuffledOrders:
        shuffledOrderPercentages[key] = orderPercentages[key]

    # Counter of percentages of the orders
    total = 0;

    # Sum the percentages of the orders
    for order, orderPercentage in shuffledOrderPercentages.items():
        total += orderPercentage

    # If we aren't using 100% of our users go adjust the percentages
    if total != 100:
        raise Exception("Total order percentages do not equal 100, instead they equal " + str(total))

    print("\r\ntotal percentage allocation is 100%")

    # Create the dictionary to store user-order pairs
    ordersDictionary = {}

    # Counter to traverse orders
    currentLocation = 0

    # Fills out the dictionary with user-order pairs
    # If the number of users does not divide cleanly into the percentages, the first percentage gets the extra
    for order, orderPercentage in shuffledOrderPercentages.items():
        numberOfUsersForCurrentOrder = (len(users)*orderPercentage) // 100
        ordersDictionary[order] = users[currentLocation:(numberOfUsersForCurrentOrder + currentLocation)]
        currentLocation += numberOfUsersForCurrentOrder

    # Print out the keys to terminal
    print(list(ordersDictionary.keys())[0])

    # Here some appending occurs between order keys and users
    ordersDictionary[list(ordersDictionary.keys())[0]].extend(users[currentLocation:])

    totalUsersOrdered = 0

    # Print number of users assigned to each order
    for order, orderedUsers in ordersDictionary.items():
        totalUsersOrdered += len(orderedUsers)
        print("\nnumber of users that should " + order + " " + str(len(orderedUsers)))

    # totalUsersOrdered should be equal to users
    print("\nOrders Generated for " + str(totalUsersOrdered) + " out of a maximum of " + str(len(users)))

    return ordersDictionary

# Credentials for the Reddit API
r = praw.Reddit( client_id="N/A",
                 client_secret="N/A",
                 user_agent="N/A",
                 password="N/A",
                 username="N/A");


# MAIN

# Flag for determing wether to just put to terminal or to also send out official orders in PM's
# True is for testing, false if for live
dryRun = True

# Calls the getOrders method above
orders = getOrders()

title = "Reddit Message Title"

# For every order
for order, orderedUsers in orders.items():
    # For every user
    for user in orderedUsers:
        message = "**Message I want to include!** \n\n Can format different in Python. \n\nOn Wisconsin!"
        try:
            if not dryRun:
                # Send the PM
                r.redditor(user).message(title, message)
                # Print order sent for record keeping purposes
                print("Sent message to " + user)
                print(user + " should " + order)
            else:
                # Print out order for testing purposes
                print(user + " should " + order)
        except:
            # Means either the username is wrong or reddit is down
            print("Could not send orders to " + user)