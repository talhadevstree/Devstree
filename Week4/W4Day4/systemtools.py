import os
import datetime  
import platform


operating_system = os.name            
current_user = os.getlogin()
current_dir = os.getcwd()

print(f"Current Operating system: {operating_system}")
print(f"Current User : {current_user}")
print(f"Current Directory : {current_dir}")
print("System:", platform.system() , platform.release())    

current_date_time = datetime.datetime.now()
print(f"Current Time : {current_date_time.strftime('%Y-%m-%d %H:%M:%S')}")