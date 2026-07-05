tasks=input("Type down today's tasks and put a comma after each one. ").split(",")
done_tasks=[]
ongoing_tasks=[]
for ok in tasks:
    print(f"\n {ok} \n" )
    finish=input(f"Have you finished {ok}?(yes/no)\n").lower()
    if finish=="yes":
        print("Nice job")
        done_tasks.append(ok)
    elif finish=="no":
        print("Try not to put it off")
        ongoing_tasks.append(ok)
    else:
        print("Please type yes or no")   
    print("--------")        
progress=input("Do you like to see today's progress?(yes/no)").lower()
if progress=="yes":
    print(f"""
        **********Done Tasks**********
        {" ".join(done_tasks)}
        *********Ongoing Tasks********
        {" ".join(ongoing_tasks)}  
    """)    