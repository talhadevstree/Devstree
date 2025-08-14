# Parse log files, extract error messages, and generate summary reports

print("-------------------------------------------------")

# parse log file (Reading)
with open('file/server.log','r') as r:
    for line in r:
        print(line)

print("-------------------------------------------------")
#Extract error messages
with open ('file/server.log','r')as error:
    for line in error:
        if "ERROR" in line:
            print(line)

#total no of lines  
#no of error found  
#types of error and their count 
#types of warning and their count

error_types= {}
warning= {}

print("-------------------------------------------------")

with open('file/server.log' , 'r') as nolines:
    #total no of lines  
        content = nolines.readlines()
        lent = len(content)
        print("No of Lines in Log:",lent)
        print("\n")

        # print("-------------------------------------------------")

        #no of error found
        error_count = 0
        for error in content:
            if "ERROR" in error:
                error_count+=1
                print("No of error are:",error)
        print("-------------------------------------------------")
        
        #types of error and their count 
with open('file/server.log' , 'r') as nolines:
        print("ERRORS")
        for errorr in nolines:
            if "ERROR" in errorr:
                error_msg = errorr.split("ERROR")[1].strip()
                if error_msg in error_types:
                    error_types[error_msg] +=1
                else:
                    error_types[error_msg] =1
        
        for errorname , count in error_types.items():
               print(f"{errorname} : {count} times")

        print("-------------------------------------------------")
with open('file/server.log' , 'r') as nolines:
        print("WARNING")
        #no of warninng
        for warn in nolines:
            if "WARNING" in warn:
                warnmsg = warn.split("WARNING")[1].strip()
                if warnmsg in warning:
                    warning[warnmsg] = +1
                else:
                    warning[warnmsg] =1
    
        for warnname , count in warning.items():
              print(f"{warnname} :{count} times") 
