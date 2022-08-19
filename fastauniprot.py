from parameters import input_validation, get_parameters, segment_query
from fasta_data_handling import show_file_fasta


def main():
    
    #Validates input
    input_validation()

    #Puts the parameters into variables
    data, filter, fields = get_parameters()
 
    show_file_fasta(data,filter)

if __name__ == "__main__":
    main()









    
    









