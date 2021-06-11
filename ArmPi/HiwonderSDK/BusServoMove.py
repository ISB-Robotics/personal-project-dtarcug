import time
import Board

angles = [0, 0, 0, 0]
Board.setBusServoPulse(1, 500, 500)
time.sleep(.5)
Board.setBusServoPulse(2, 500, 500)
time.sleep(.5)
Board.setBusServoPulse(3, 500, 500)
time.sleep(.5)
Board.setBusServoPulse(5, 500, 500)
time.sleep(.5)
Board.setBusServoPulse(4, 500, 500)
time.sleep(.5)
Board.setBusServoPulse(6, 500, 500)
time.sleep(2)
    
for i in range(5):
    Board.setBusServoPulse(5-i, 875-angles[i]/.24, 500)
    time.sleep(0.5)
    
