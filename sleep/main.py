'''
Source: https://realpython.com/python-sleep/

Python time.sleep() halts the entire thread

Conclusion
Now you know how to make Python wait, sleep, and add time delays across a range of contexts. 
Whether you need a quick pause between API calls or a non-blocking delay in async code, Python has you covered.

In this tutorial, you have learned how to:

 - Pause execution with time.sleep() for any duration
 - Retry failed operations using a sleep-based decorator
 - Add delays in threads with time.sleep() and Event.wait()
 - Use asyncio.sleep() for non-blocking async delays
 - Avoid freezing GUIs with .after() in Tkinter and wx.CallLater() in wxPython
'''

from time import sleep

print("brewing coffee, it would take 3 seconds")
sleep(3)
print("coffee is ready!")


