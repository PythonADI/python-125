import time

conditioning_state = 0


while True:
    start = time.time()
    temperature = float(input(">>> "))

    if 24 < temperature:
        conditioning_state = 1
    
    elif temperature < 18:
        conditioning_state = 2
    else:
        conditioning_state = 0
    
    print(f"{conditioning_state = }")
    print(time.time() - start)
    time.sleep(10)

