import sys
import os
import os.path

#Input validation
def input_validation()->bool:

    #Tests if a file name has been given (if a first argument has been given)
    if len(sys.argv) < 2:
        print("\033[1m","File name is required.","\033[0m")
        exit()


    #Tests if the file exists in the working directory
    if os.path.exists(sys.argv[1]) == False:
        print("\033[1m","File does not exist.","\033[0m")
        exit()

    #Tests if a query has been given (if a second argument has been given)
    if len(sys.argv) < 3:
        print("\033[1m","Query is required.","\033[0m")
        exit()
        


#splits up the query
def segment_query(query)-> list:
    seg_query = query.split(".")

    return(seg_query)



    #Extracts parameters given in command line
def get_parameters()->tuple:
    path = sys.argv[1]
    filter = sys.argv[2]
    fields_to_extract = sys.argv[3:]
    
    return(path,filter,fields_to_extract)


