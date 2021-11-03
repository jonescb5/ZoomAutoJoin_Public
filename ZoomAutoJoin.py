# Zoom Auto Join
# Christopher Jones
#
# Shout-out to Sam Westby for the basis of this code!
# His original video can be found here:
# https://www.youtube.com/watch?v=4cDYF0F4VsI


import schedule
import time
import webbrowser

print("Starting ZoomAutoJoin.py ...\n")

# BEGIN: MEETING FUNCTION DEFINITIONS

# Note: These are just example meetings to show an easy way to structure your schedule.
#       You can use this format to schedule your own meeting and remove these.

# Example A Meeting Function Defs


def example_a_meeting_join():
    print("Joining Example A Meeting ...\n")
    webbrowser.open('https://zoom.us/test')  # Put your meeting link in here i.e. https://vcu.zoom.us/j/xxxxxxxx


def example_a_meeting_schedule():
    schedule.every().monday.at("13:55").do(example_a_meeting_join)
    schedule.every().wednesday.at("13:55").do(example_a_meeting_join)
    print("Scheduled Example A Meeting for Monday and Wednesday at 13:55 ...\n")


# Example B Meeting Function Defs

def example_b_meeting_join():
    print("Joining Example B Meeting ...\n")
    webbrowser.open('https://zoom.us/test')  # Put your meeting link in here i.e. https://vcu.zoom.us/j/xxxxxxxx


def example_b_meeting_schedule():
    schedule.every().monday.at("07:55").do(example_b_meeting_join)
    schedule.every().wednesday.at("07:55").do(example_b_meeting_join)
    schedule.every().friday.at("07:55").do(example_b_meeting_join)
    print("Scheduled Example B Meeting for Monday, Wednesday, and Friday at 07:55 ...\n")

# END: MEETING FUNCTION DEFINITIONS

# BEGIN: ADD MEETINGS TO SCHEDULE
# Add your meetings to the schedule by defining them above and running the "xxx_schedule" function
# in this section.


example_a_meeting_schedule()  # Add Example A Meeting to the Schedule
example_b_meeting_schedule()  # Add Example B Meeting to the Schedule

# END: ADD MEETINGS TO SCHEDULE


# This section runs continuously, checking your computer's system time and
# running the pending operation.
while True:
    schedule.run_pending()
    time.sleep(60)

