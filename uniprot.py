
from cgi import print_arguments, test
from dataclasses import fields
from inspect import Parameter
import sys
import os
import os.path
from xmlrpc.client import Boolean



#Task 1
#Need to make it so the when you print a whole record it prints a line break instead of \n
#Need to add a counter for amount of matches and amount of records it looked through


#Task 2


#Extracts parameters given in command line
def get_parameters()->tuple:
    path = sys.argv[1]
    filter = sys.argv[2]
    fields_to_extract = sys.argv[3:]
    
    return(path,filter,fields_to_extract)


#splits up the query
def segment_query(query)-> list:
    seg_query = query.split(".")

    return(seg_query)


#Prints the parts of the record asked for if the record matches the query.
def print_relevant_records(record:list, query_parts:list,list_of_fields)->None:

    filter_name = query_parts[2]
    filter_value = query_parts[0]
    #Variable used to count number of matches
    match = False
    for field in record:
        #Finds the field of interest in record and checks if the value we are searching for is in this field
        if field[0:2] == filter_name and filter_value in field:
            #Here you are able to add more requirements
            #Also write here what will happen when the filter is correct
            match = True
            #Prints the whole record if there are no specific fields to show (under here could be own function)
            if len(list_of_fields) == 0:
                for line in record:
                    print(line[:-1])
            
            #Else, if a list of fields has been given prints only the information from these fields
            else:
                for line in record:
                    if line[:2] in list_of_fields:
                        print(line[:-1])
            print("//")
                        
    return(match)


            

#Creates a variable with a unique record for all proteins
def show_file(data:str,query:str,list_of_fields:list)->None:
    file = open(data)
    record = []
    #Splits the filter up, into value and name
    query_parts = segment_query(query)
    #Set up variables to count number of records and number of matches
    n_records = 0
    matches = 0
    #Creates a record for each of the proteins.
    for line in file:
        if line[:2] == "ID":
            record.clear()

        elif line[:2] == "//":  
            #at this point, a unique record is in the 'record' structure
            #nice to apply any filters here 
            match = print_relevant_records(record,query_parts,list_of_fields)
            #Counts the amount of matches and records
            if match == True:
                matches = matches + 1
            n_records = n_records + 1
            
            
        record.append(line)
    print("match records = ",matches,"\nrecords processed =",n_records)
            
    file.close()

    return()

#Input validation
def input_validation()->Boolean:

    #Tests if a file name has been given (if a first argument has been given)
    if len(sys.argv) < 2:
        print("\033[1m","You have not provided a file name. Please provide a file name","\033[0m")
        return(False)


    #Tests if the file exists in the working directory
    if os.path.exists(sys.argv[1]) == False:
        print("\033[1m","The file does not exist. Please enter a valid file.","\033[0m")
        exit()

    #Tests if a query has been given (if a second argument has been given)
    if len(sys.argv) < 3:
        print("\033[1m","No query was given. Please give a query in the form of field_name.in.value_to_match","\033[0m")
        exit()
        

def main()->None:
    #Checks if input is valid
    input_validation()


    #Receives the different parameters from the input
    data, filter, fields = get_parameters()

    
    show_file(data, filter,fields)

    return()

main()



