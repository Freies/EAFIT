
from parameters import segment_query




def make_SQ_string(record:list,k:int)->str:
    list = record[k+1:]
    SQ_string = "".join(list)
    SQ_string = SQ_string.replace(" ","")
    SQ_string = SQ_string.replace("\n","")
    return(SQ_string)


def fasta_check(record,query_parts):
    matches = 0

    #at this point, a unique record is in the 'record' structure
    #nice to apply any filters here 
    #Goes through each filter requirement, each requirement has 2 values, and therefore i increase by 2.
    for i in range(0,len(query_parts),2):
        
        k = 0
        #Checks if the query field is SQ, because the file structure means it should get speciel treatment.
        if query_parts[i+1] == "SQ":
        #Then goes trough the whole record to find the place where SQ starts
            for line in record:
                if line[0:2] == "SQ":
                    #Makes the actual sequence into a string
                    SQ_string = make_SQ_string(record,k)
                    #Checks if the query vaalue is in string, and adds a match if it is.
                    if query_parts[i] in SQ_string:
                        matches = matches + 1
                        #If right amount of matches are present, then prints the FASTA
                        if matches == len(query_parts)/2:
                            print_relevant_fasta(record,query_parts)
       
            k = k+1
                

        #For other filters goes through every line
        for line in record:
            
            #Finds the line with the filter name, and checks if the filter value is in it.
            if line[0:2] == query_parts[i+1] and query_parts[i] in line:
                #WARNING: Make tests, 

                #Adds a match to the amount of queries that are matching.
                matches = matches + 1
                if matches == len(query_parts) / 2:
                    print_relevant_fasta(record,query_parts)
                break

    return


def show_file_fasta(data:str,query:str)->None:
    file = open(data)
    record = []

    #Splits the filter up, into value and name
    query_parts = prepare_filter(query)

    #Creates a record for each of the proteins.
    for line in file:
        
        if line[:2] == "ID":
            record.clear()

        elif line[:2] == "//":         
            fasta_check(record,query_parts)

        record.append(line)
        
    file.close()

    return(None)


def print_relevant_fasta(record:list,query_parts:list)->None:
    #i is initialized to know at which line the sequene starts.
    i = 0
    OS_has_been = False
    for line in record:
        if line[0:2] == "ID":
            #Prints the id line, with the correct id afterwards
            print(">id={}".format(line.split()[1]),end=";")
        if line[0:2] == "AC":
            #Print all different AC numbers there may bee
            print("acc=",end="")
            print(*line.split()[1:],end="")
        if line[0:2] == "OS":
            #Prints all different OS numbers there might be.
            if OS_has_been == False:
                print("name=",end="")
                print(*line.split()[1:],sep=" ",end="")
                OS_has_been = True
            else:
                print(*line.split()[1:],sep=" ",end="")

            
        
        if line[0:2] == "SQ":
            #Takes all of the lines from from the sequence, that contains the actual aminoacid letters.
            list = record[i+1:]

            #Makes the list to a string, and removes all spaces and newlines.
            SQ_string = "".join(list)
            SQ_string = SQ_string.replace(" ","")
            SQ_string = SQ_string.replace("\n","")

            #Prints the SQ string, with 80 characters pr line.
            print("")
            for k in range(0,len(SQ_string),80):
                print(SQ_string[k:k+80])
           


        i = i + 1
            
            
            
    return

def prepare_filter(filter)->list:
    #Splits the filter into a list
    split_filter = filter.split(".")
    #Removes "and" and "in" so only the actual queries are left
    try:
        while True:
            split_filter.remove("and")
    except ValueError:
        pass

    try:
        while True:
            split_filter.remove("in")
    except ValueError:
        pass
    
    return(split_filter)


