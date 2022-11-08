def try_catch():
    try:
        x = input(print("please enter number: "))
        y = int(x)
        y=y*2
    except IOError as err:
        print("IOError ", err)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
    else: 
        print("No err: ",y)
    return
        
try_catch()
