import tkinter as tk
from Calc import Calc
import datetime
Timing = datetime.datetime.now()

if __name__ == '__main__':
    root = tk.Tk()
    main = Calc(root)
    main.start()
    Log = open("LogReport/log.txt", 'a+')
    Log.write(
        f"\n Timing :{'Day : ' + str(Timing.day), 'Month : ' + str(Timing.month)}\t {'Hour : ' + str(Timing.hour), 'Min : ' + str(Timing.minute), 'Sec : ' + str(Timing.second)}\t : Calcualator Successfully Exited...")
    Log.close()