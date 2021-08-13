# Timer-python

Traceback (most recent call last):
  File "C:/Users/asus/PycharmProjects/untitled3/Hellotimer.py", line 31, in <module>
    timer = plc.read_area(areas["TM"], 1, 5, S7WLTimer)
  File "C:\Users\asus\PycharmProjects\untitled3\venv\lib\site-packages\snap7\client.py", line 393, in read_area
    raise ValueError(f"{area} is not implemented in snap7.types")
ValueError: 29 is not implemented in snap7.types

  this si the error code. i will try and use a write memory function that will help me enable the sps code to run as soon as i start the program
