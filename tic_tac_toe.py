import random
board=[0,1,2,
	3,4,5,
	6,7,8]
def show():
 print board[0],'|',board[1],'|',board[2]
 print '---------'
 print board[3],'|',board[4],'|',board[5]
 print '---------'
 print board[6],'|',board[7],'|',board[8]
 print '---------'
show()
while True:
 input=int(raw_input("enter the place"))
 if board[input]!='x' and board[input]!='o':
  board[input]='x'
#check for winner
  comp=random.choice(range(9))
  find=True
  while find:
   if board[comp]!='x' and board[comp]!='o':
    board[comp]='o'
#check for winner
    find=False
    
 else:
  print "this spot is already taken..!" 
 show()

