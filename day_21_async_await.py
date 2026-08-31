# ============================Async programming in pytonn===============================================
import time
import asyncio

# ====================sync programming===============
# In synchorous programming python see i first complete task 1 then move next first everything of task 1 first complete then run to other task 2.
def task1():
    print("Task 1 is started....")
    time.sleep(3)
    print("Task 1 finished...")


def task2():
    print("Task 2 is started....")
    time.sleep(2)
    print("Task 2 finished...")

#this take 3+2 seconds of time means first task take 3 second and 2nd task take 2 second it take total time 5 seconds...
                                                                    # Task 1 → start downloading
                                                                    #         ↓
                                                                    #         waiting...
                                                                            
                                                                    # Task 2 → start downloading
                                                                    #         ↓
                                                                    #         waiting...

                                                                    # Task 2 → finished
                                                                    # Task 1 → finished
# task1()
# task2()





# ===========================================================ASYNCHOROUS PROGRAMMING IN PYTONE================================================    

async def hello():
    print("Hello! this is async function...")


# hello()  we cannot call it like this like a normal function 

# async def main():
#     await hello()



# asyncio.run(main())


                        #  EXAMPLE 
#Now this is async not both task complete parallel in 3 seconds not take 5 second

# in async if wait come in task 3 then it go in this time go and complete other work when it complete the comback to this task ok..
async def task3():
    print("Task 3 started")
    await asyncio.sleep(3)
    print("Task 3 finished")

async def task4():
    print("Task 4 started")
    await asyncio.sleep(2)
    print("Task 4 finished")

async def main():
    await asyncio.gather(
        task3(),
        task4()
    )

# asyncio.run(main())



# EXAMPLE EXERCISE

async def first():
    print("step 1 is started")

    await asyncio.sleep(6)

    print("step 1 is ended...")

async def second():
    print("step 2 is started,,,...")

    await asyncio.sleep(4)

    print("step 2 ended ....")

async def calling():
    start_time = time.perf_counter()

    await asyncio.gather(
        first(),
        second()
    )

    end_time = time.perf_counter()
    print(f"The start time is: {start_time} and end time is: {end_time} and total count of time it take is: {end_time-start_time}")


asyncio.run(calling())