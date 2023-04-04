started=False
while True:
    x=input('>')
    if(x=='help'):
        print(''' 
start --to start car
stop --to stop car
quit --to exit''')
    elif (x=='start'):
        if(started):
            print('car already started')
        else:
            print('car started')
            started=True
    elif(x=='stop'):
        if(not started):
            print('car already stopped')
        else:
            print('car stopped')
            started=False
    elif(x=='quit'):
        break
    else:
        print('invalid command')










