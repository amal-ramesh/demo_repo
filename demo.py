import csv
f = open("Data.csv","r")
file_reader = csv.reader(f)

basic_dict = {}
basic_dict_cleaned = {}


headers = next(file_reader)

basic_dict = {col : [] for col in headers}
basic_dict_cleaned = {col : [] for col in headers}

for row in file_reader:
    for col_index , value in enumerate(row):
        heading_name = headers[col_index]
        basic_dict[heading_name].append(value)


for key,value in basic_dict.items():
    for i in basic_dict[key]:
        if i == "":
            basic_dict[key].remove(i)
        else:
            i = i.strip("· ")
            i = i.strip("*")
            basic_dict_cleaned[key].append(i)

#print(basic_dict_cleaned)

# Function for creating edible and non-edible items dictionary!
def filter_edible_nonedible(basic_dict_cleaned):
    filtered_dict = {"edible":{},"non_edible":{}}

    edible_list = ["Fresh vegetables","Condiments / Sauces","Baked goods","Fresh fruits"]
    non_edible_list = ["Personal care","Cleaning products","Baby stuff"]

    for key,value in basic_dict_cleaned.items():
        if key in edible_list:
            filtered_dict["edible"][key] = value
        elif key in non_edible_list:
            filtered_dict["non_edible"][key] = value

    return (filtered_dict)



# Function for displaying the whole list of items
def view_complete_list(basic_dict_cleaned):
    for key,value in basic_dict_cleaned.items():
        print(key)
        print("-----------------")
        for i in basic_dict_cleaned[key]:
            print(i)
        print("###############################")

# Calling the function here

#view_complete_list(basic_dict_cleaned)



def abcd:
    print ("aaa")