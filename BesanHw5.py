# Homework 5

# Problem 1
def read_file(name):
    '''
    Read in the file with the given name and print out its contents

    Inputs:
        name: file name
    '''
    # FILL IN YOUR CODE HERE
    with open(name,"r")as f:
        for row in f:
            print (row)

read_file("problem1.txt")   

# Problem 2
def read_dict(name):
    '''
    Read in the file with the given name and convert the contents
    into a dictionary with the appropriate key/value pairs.
    Return the dictionary from the function

    Inputs:
        name: file name

    Returns:
        dictionary with keys/values 
    '''
    # FILL IN YOUR CODE HERE
    new_dict={}
    with open (name, "r") as f:
        for row in f:
            mylist=row.strip().split(" ") #["adam", "3"]
            key=mylist[0].strip()
            value=mylist[1].strip()
            if(key not in new_dict.keys()):
                new_dict[key]=value
    return new_dict
print("\n",read_dict("problem2.txt"))


# Problem 3
def find_longest_word(name):
    '''
    Read in the file with the given name, in which a series of words are printed out on each line.
    The find and return the longest word.
    
    Inputs:
        name: file name
        
    Returns:
        string with the largest word
    '''
    # FILL IN YOUR CODE HERE
    with open(name,"r") as f:
        longest_word=""
        for row in f:
            word=row.strip()
            if len(word)>len(longest_word):
                longest_word=word

    return longest_word
print("\n"+find_longest_word("problem3.txt"))

# Problem 4
def count_word_freq(name):
    '''
    Read in the file with the given name, in which a series of words are separated either by spaces or new lines.
    Count the frequencies of each word in the file and return a dictionary with the words
    as the keys and the frequencies as the values.
    
    Inputs:
        name: file name
    
    Returns:
        dictionary in which keys are words and values are their frequencies (the number
        of times that they appear in the file)
    '''
    # FILL IN YOUR CODE HERE
    dict_words={}
    with open(name ,"r") as f:
        for row in f:
            sentence=row.strip().split(' ')  #it becomes list
            for word in sentence:
                if word in dict_words.keys():
                    dict_words[word]+=1
                else:
                    dict_words[word]=1
    return dict_words


print("\n",count_word_freq("problem4.txt"))
# Problem 5
def convert_csv_txt(input_name, output_name):
    '''
    Convert a .csv into a .txt file. First, read in the contents of the csv file. Then, separate out
    the contents by the delimiter (which is ',' for a .csv). Write out and save the contents
    to the output file in which each element is separated by a new line.
    
    So you essentially convert a .csv (which has a ',' delimiter) into a text file
    with a '\n' (newline) delimiter.
    
    Inputs:
        input_name: name of input file (.csv)
        output_name: name of output file that you will write (.txt)
    '''
    # FILL IN YOUR CODE HERE
    # first way 
    with open(input_name,"r") as f:
        for row in f:
            my_list=row.strip().split(',')
            with open(output_name,"w")as txtfile:
                for item in my_list:
                    txtfile.write(item+"\n")
    print("\na new file with .txt extension is created")
convert_csv_txt("problem5.txt","new5.txt")


# second way
#     with open(input_name,"r") as f, open(output_name,"w")as txtfile:
#         for row in f:
#             newrow=row.replace(',','\n')
#             txtfile.write(newrow)
#     print("a new file with .txt extension is created")
# convert_csv_txt("\nproblem5.txt","new5.txt")