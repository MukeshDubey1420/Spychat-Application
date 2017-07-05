# By using hash sign"#"  <-----We are Introducing Comments in Python------->
from spydetails import spy, Spy, ChatMessage, friends        # Importing spy files in main programme ..
from steganography.steganography import Steganography        # Importing steganography so as to encoding or decoding the secret text inside the image ...
from datetime import datetime                                # Importing date time so as to notify the timing for chats and date on which message is sent...
from termcolor import colored                                # Importing Term color to make text colored....

STATUS_MESSAGES = ['Hey Whats Up ,Its Mukesh Here, Mukesh Dubey', 'Busy', 'User Is Available..']          # List of the status messages already stored..
special = ['SOS','sos','help','HELP','save','SAVE']                                                       # List containing special words like SOS HELP SAVE included in Extras part ..

print colored("<----- Hello! Let's get started ----->","green")    # Printing hello to start application-->

question = colored("Do you want to continue as ",'blue') + colored(spy.salutation,'red') + " " + colored(spy.name,'red') + " (Y/N)? "  # Asking about if it is admin or new user or spy..
existing = raw_input(question)


def add_status():                                           #Function Regarding status messages ....

    updated_status_message = None

    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print colored("You don't have any status message currently \n",'red')

    default = raw_input(colored("Do you want to select from the older status (y/n)? ",'blue'))    # Default case if he want to select the status from older status messages.

    if default.upper() == "N":
        new_status_message = raw_input(colored("Write the status message do you want to set? ",'blue'))


        if len(new_status_message) > 0:                                      # Checking status is empty or not....
            STATUS_MESSAGES.append(new_status_message)                       # adding the newly updated status to the status message list. append function will add the status in the last index position of the list..
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1                             # To make it user Friendly as user does not know about zero indexing ..

        message_selection = int(raw_input(colored("\nChoose from the above messages ",'green')))    # Selecting the status from older statuses...


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]  # Updating again zero indexing so as to understand by python . to make it language friendly..

    else:
        print colored('The choice you Entered is not valid! Press either y or n.','red')

    if updated_status_message:
        print colored('Your updated status message is: %s','blue') % (updated_status_message)
    else:
        print colored("You current don't have a status update",'red')
    return updated_status_message


def add_friend():                                                           # Defining the add_friend function...>

    new_friend = Spy('','',0,0.0)                                           # Blank details initially..after giving details by user ,details are stored in this..

    new_friend.name = raw_input(colored("Please add your friend's name: ",'green'))
    new_friend.salutation = raw_input(colored("what would u like to call Mr. or Ms.?: ",'blue'))

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)                    # Taking age as input in string and then converting it into int data type ..

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)           # Taking rating as input in string forn and then converting it into float data type ..

    if len(new_friend.name) > 0 and new_friend.age > 19 and new_friend.rating >= 4:    # To be a Valid user as a spy following parameters or conditions are set here..
        friends.append(new_friend)                                                     # Appending the friend in the List of friend lists.
        print colored('Your Friend Is Added!','green')
    else:
        print colored("Sorry! Invalid entry. Your Friend is Not Eligible to be a Spy",'red')

    return len(friends)                                                         # It returns the total number of friends in ur friend list-->


def select_a_friend():                                                         # Selecting a friend function is defined here. in case we wanna to talk or to read chat then we call this function..
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name, friend.age,friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input(colored("Choose from your friends Lists",'blue'))

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position                                             # Returns the position of the friend or simply we can say this returns the index of the friend selected by u..


def send_message():                                                 # Here we defining the send_message function..which basically selects the friend & sending the secret message in form of text in a image..

    friend_choice = select_a_friend()

    original_image = raw_input(colored("Please Enter the name of the image?",'blue'))  # Name of the image in which u wanna to hide the text..
    output_path = "output.jpg"                                                         # Output path or name which is basically totally different from initial original image .and format changes here ..
    text = raw_input(colored("What's the secret message u wan't to Convey? ",'blue'))  # Secret text u wanna to hide in that image ..
    Steganography.encode(original_image, output_path, text)                            # Encoding the text in image via function..

    temp = text.split(' ')
    for i in special:
        if i in temp:
            temp[temp.index(i)] = colored('Please Help Me !! I Am in Danger..','red')  # Replacing special words with a special type of emergency message ...
    text = str.join(' ',temp)
    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)                                      # Appending the secret code in the chat list of that particular friend-->

    print colored("Your secret message in the image is ready!",'green')


def read_message():                               # Here we defining the read_chat_message function which basically decodes the specail secret message and stores it..

    sender = select_a_friend()

    output_path = raw_input(colored("Enter the name of the file In which secret Text is Hidden ?",'blue'))
    try:
        secret_text = Steganography.decode(output_path)
    except ValueError:
        print colored("No secret message is coded in the image!!", 'red')
        exit()

                          # Decoding the secret text hidden in the image ...i.e. we are extracting the secret code from the particular image ..and stores it..
    secret_text = str(secret_text)
    if secret_text == 'None':
        print colored("No secret message is coded in the image!!",'red')         # Case of error handling in case user does not writes the secret code to encode in the image ..
    else:
        temp = secret_text.split(' ')
        for i in special:
            if i in temp:
                temp[temp.index(i)] = colored('Please Help Me,I am in Danger!!','red')
        secret_text = str.join(' ',temp)
        if len(secret_text)>100:                                                     # Handling a special case in which a friend is annoying u by sending a long text message then u have a option to delete that friend or not..
            print colored("As ur friend Annoying u ,Do u Want to Delete him or her From your Friend lists.",'red')
            choice = raw_input(colored("If u want to Delete ur friend choose:--> 'Y' , If not choose:--> 'N' ",'blue'))
            if choice == "Y":
                del [sender]                              # That particular friend is deleted from the friend lists..
                print colored("Now your Friend is no More in Your Friend List",'green')
                print colored("Select your choice shown Below..",'blue')
            else:
                print colored(secret_text,'blue')

        else:
            new_chat = ChatMessage(secret_text, False)

            friends[sender].chats.append(new_chat)

            print colored("Your secret message has been saved!",'green')


def read_chat_history():                          # We wanna to read the older chat messages which are stored in chat lists..

    read_for = select_a_friend()                  # selecting that particular friend whose chat u wanna to read....

    print '\n'

    for chat in friends[read_for].chats:
        time = chat.time.strftime("%A, %b %d %Y %H:%M:%S")    # Assigning the date ( date month year ), and time ( hour minute second) parameter ..
        if chat.sent_by_me:
            print '[%s] %s: %s' % (colored(time,'blue'), colored('Sent By Me:','red'), chat.message)    # Message sent by user at that date and time ..
        else:
            print '[%s] %s read: %s' % (colored(time,'blue'), colored(friends[read_for].name,'red'), chat.message)   # Message read by user's friend at the particular date and time ..


def start_chat(spy):                              # Starting the application by defining chat function..

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 18 and spy.age < 50:           # Setting the validity parameter to be a spy..


        print colored("Authentication complete. Welcome ",'blue') + colored(spy.name,'red') + colored(" age: ",'blue') \
              + str(spy.age) + colored(" and rating of: ",'blue') + str(spy.rating) + colored(" Good To See U",'blue')          # After Verifying the your details u r able to use the application and choose further what u wanna to do..

        show_menu = True                      # Showing the menu lists of items what the spychat offers to the user..

        while show_menu:                      # Applying the loop here so as to whenever the condition of show menu is true lists items are shown when it becomes false lists items disappears..
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"  # Lists of things offered by spychat application..
            menu_choice = raw_input(colored(menu_choices,'green'))

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:     # If choosing 1 status messages will comes ..
                    spy.current_status_message = add_status()
                elif menu_choice == 2:  # Selecting 2 will shown friends lists..
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()       # 3 for sending the message to a particular friend ..
                elif menu_choice == 4:
                    read_message()       # 4 for reading the chats of a particular friend ..
                elif menu_choice == 5:
                    read_chat_history()   # 5 for reading previous chats history of diffrent diffrent friends..
                else:                     # If user selects option number 6 , then show menu becomes false and items were disappeared.. and exit from the application..
                    show_menu = False
    else:
        print colored('Sorry you are not of the correct age to be a spy','red')    # Age parameters IF NOT SATISFIES the condition..

if existing.upper() == "Y":      # If user enters "Y" then admin details are passed to spychat function ..and application starts ...
    start_chat(spy)
else:                    # If the user selects "N" Then a new user have to pass the details to verify it and the he is able to start the application..

    spy = Spy('','',0,0.0)    # Initially user has no data ..it is blank. after getting details is is to be filled.


    spy.name = raw_input(colored("<---Welcome to spy chat, To Further proceed you must tell me your spy name first: --->",'red'))

    if len(spy.name) > 0:      # checking Validation of empty name ..
        spy.salutation = raw_input(colored("Should I call you Mr. or Ms.?: ",'blue'))

        spy.age = raw_input(colored("Enter your age?",'blue'))
        spy.age = int(spy.age)             # Converting Age of spy into int data type ..

        spy.rating = raw_input(colored("What is your spy rating?",'blue'))
        spy.rating = float(spy.rating)      # Converts the rating into float .bcz Raw_input returns string type .

        start_chat(spy)
    else:
        print colored('Please Mention a valid spy name','red')     # U Must have to Mention valid details ..

  # End of the coding .........