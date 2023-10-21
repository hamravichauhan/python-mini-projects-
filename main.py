import tkinter as tk
from time import time
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    speed = len(userinput) / time_r
    return round(speed)

time_1 = 0
test1 = ""
def start_typing_test() :
    global test1 , time_1  # Declare test1 and time_1 as global
    test1 = r.choice ( tests )
    display_text.set ( test1 )
    input_entry.delete ( 0 , 'end' )  # Clear the input field
    time_1 = time ()


def submit_typing_test() :
    global time_1  # Declare time_1 as global
    user_input = input_entry.get ()
    time_2 = time ()
    speed = speed_time ( time_1 , time_2 , user_input )
    error = mistake ( test1 , user_input )
    result_text.set ( f'Speed: {speed} w/sec\nErrors: {error}' )


root = tk.Tk()
root.title("TYPING TEST")
root.geometry('800x600')  # Adjusted the window size
root.configure(background='white')  # Changed the background color

tests = [
    "my name is ravi chauhan",
    "my name is mithil roll no 32 ",
    "happy birthday sahil ",
    "welcome to our python project "]

display_text = tk.StringVar()
result_text = tk.StringVar()

test_label = tk.Label(root, text="***************************THIS IS A TYPING TEST*************************** ", fg='blue')
test_label.pack(pady=(20, 20))
test_label.configure(background='white')
test_label.config(font=('verdana', 20))

test_text = tk.Label(root, textvariable=display_text)
test_text.pack(pady=(20, 20))
test_text.config(font=('verdana', 16))

input_entry = tk.Entry(root, width=60)
input_entry.pack(pady=(20))
input_entry.config(font=(16))

start_button = tk.Button(root, bg='green', fg='white', text="Start Typing Test", command=start_typing_test)
start_button.pack(pady=(10, 20))
start_button.config(font=(16))

submit_button = tk.Button(root, text="Submit", command=submit_typing_test)
submit_button.pack(pady=(20, 20))
submit_button.config(font=(20))

result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

root.mainloop()
