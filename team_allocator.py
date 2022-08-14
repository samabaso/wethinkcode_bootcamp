# Samkhele Beranrdo Mabaso  Email:mabaso16v@gmail.com bootcampEmail:110093 

def student_list():
    return ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'BusiJHB2022 - 2 May - Durban Virtual',
    'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1', 'CebiJHB2022 - 2 May - Durban Virtual',
    'lukhona - 4 April - Phokeng Virtual', 'ddhaalJHB2022 - 2 May - Durban Physical - seat 4',
    'gabiDBN2022 - 4 April - Phokeng Virtual', 'ngakithilJHB2022 - 2 May - Durban Physical - seat 5',
    'zimthembilehDBN2022 - 4 April - Phokeng Virtual', 'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2',
    'zimlindilehDBN2022 - 4 April - Phokeng Virtual', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3',
    'zimthandilehDBN2022 - 4 April - Johannesburg Virtual','kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1',
    'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual','hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3',
    'zizonkehDBN2022 - 4 April - Johannesburg Virtual','sibusisohDBN2022 - 4 April - Durban Physical - seat 2',
    'kholekileDBN2022 - 4 April - Johannesburg Virtual','vusiDBN2022 - 4 April - Durban Physical - seat 9',
    'kholelwahDBN2022 - 4 April - Johannesburg Virtual','zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10',
    'thembelahDBN2022 - 4 April - Johannesburg Virtual','babazileDBN2022 - 4 April - Durban Physical - seat 11',
    'thembisileDBN2022 - 4 April - Johannesburg Virtual','owenkosiDBN2022 - 4 April - Durban Physical - seat 8',
    'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5', 'nobuhleJHB2022 - 2 May - Cape Town physical',
    'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'nonkonzoJHB2022 - 2 May - Cape Town Physical',
    'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 'nombusoJHB2022 - 2 May - Cape Town Virtual',
    'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'nozizweJHB2022 - 2 May - capetownvirtual']

# gets all the students in durban
def dbn_campus_students(student_list): 
    dbn_students = []
    dbn_unique_students = set(student_list)
    for number in dbn_unique_students:
        split_char = number.split("-")
        index_number = split_char[0:][2]
        if index_number.startswith("d" ) or index_number.startswith("D"):
            dbn_students.append(number)
        elif "Durban" in number :
            dbn_students.append(number)
    return dbn_students

# gets all the students in cape town
def cpt_campus_students(student_list): 
    cpt_students = []
    cpt_unique_students = set(student_list)
    for number in cpt_unique_students:
        split_char = number.split("-")
        index_number = split_char[0:][2]
        if index_number.startswith("c" ) or index_number.startswith("C"):
            cpt_students.append(number)
        elif "Cape Town" in number :
            cpt_students.append(number)
    return cpt_students

# gets all the students in johannesburg
def jhb_campus_students(student_list): 
    jhb_students = []
    jhb_unique_students = set(student_list)
    for number in jhb_unique_students:
        split_char = number.split("-")
        index_number = split_char[0:][2]
        if index_number.startswith("j" ) or index_number.startswith("J"):
            jhb_students.append(number)
        elif "Johannesburg" in number :
            jhb_students.append(number)
    return jhb_students

# gets all the students in north west
def nw_campus_students(student_list): 
    nw_students = []
    nw_unique_students = set(student_list)
    for number in nw_unique_students:
        split_char = number.split("-")
        index_number = split_char[0:][2]
        if index_number.startswith("p" ) or index_number.startswith("P"):
            nw_students.append(number)
        elif "Phokeng" in number :
            nw_students.append(number)
    return nw_students


# gets all the students in durban and are physical
def dbn_physical_students(dbn_campus_students):
    dbn_physical_students = []
    for i in dbn_campus_students:
        if "Physical"  in i:
            dbn_physical_students.append(i)
        elif "physical" in i:
            dbn_physical_students.append(i)
    return dbn_physical_students

# groups the dbn_physical_students by teams of 4
def dbn_physical_teams(dbn_physical_students):
    a = str(dbn_physical_students[0:4])
    b = str(dbn_physical_students[4:8])
    c = str(dbn_physical_students[8:])
    d = [a, b, c]
    return d

# saves the data to dbn_physical_students.txt file
def dbn_teams_file(durban_physical_teams): 
    textfile = open("dbn_physical_teams.txt", "w")
    for element in durban_physical_teams:
        textfile.write(element + "\n")
    textfile.close()

# get all the students in cape town and are physical
def cpt_physical_students(cpt_campus_students):
    cpt_physical_students = []
    for i in cpt_campus_students:
        if "Physical"  in i:
            cpt_physical_students.append(i)
        elif  "physical" in i:
            cpt_physical_students.append(i)
    return cpt_physical_students

# groups the cpt_physical_students by teams of 4
def cpt_physical_teams(cpt_physical_students):
    a = str(cpt_physical_students[0:4])
    d = [a]
    return d

# saves the data to cpt_physical_students.txt file
def cpt_teams_file(cpt_physical_teams): 
    textfile = open("cpt_physical_teams.txt", "w")
    for element in cpt_physical_teams:
        textfile.write(element + "\n")
    textfile.close()

# get all the students in johannesburg and are physical
def jhb_physical_students(jhb_campus_students):
    jhb_physical_students = []
    for i in jhb_campus_students:
        if "Physical"  in i:
            jhb_physical_students.append(i)
        elif  "physical" in i:
            jhb_physical_students.append(i)
    return jhb_physical_students

# groups the jhb_physical_students by teams of 4
def jhb_physical_teams(jhb_physical_students):
    a = str(jhb_physical_students[0:4])
    b = str(jhb_physical_students[4:])
    c = [a, b]
    return c

# saves the data to jhb_physical_students.txt file
def jhb_teams_file(jhb_physical_teams): 
    textfile = open("jhb_physical_teams.txt", "w")
    for element in jhb_physical_teams:
        textfile.write(element + "\n")
    textfile.close()


# get all the students in north west and are physical
def nw_physical_students(nw_campus_students):
    nw_physical_students = []
    for i in nw_campus_students:
        if "Physical"  in i:
            nw_physical_students.append(i)
        elif  "physical" in i:
            nw_physical_students.append(i)
    return nw_physical_students

# groups the nw_physical_students by teams of 4
def nw_physical_teams(nw_physical_students):
    a = str(nw_physical_students[0:])
    b = [a]
    return b

# saves the data to nw_physical_students.txt file
def nw_teams_file(nw_physical_teams): 
    textfile = open("nw_physical_teams.txt", "w")
    for element in nw_physical_teams:
        textfile.write(element + "\n")
    textfile.close()
    
# gets all the students that are virtual
def get_virtual_students(student_list): 
    virtual_campus = []
    virtual_unique_students = set(student_list)
    for number in virtual_unique_students:
        if "Virtual" in number:
            virtual_campus.append(number)
        elif "virtual" in number:
            virtual_campus.append(number)
    return virtual_campus

# groups the get_virtual_students by teams of 4
def virtual_teams(get_virtual_students):
    a = str(get_virtual_students[0:4])
    b = str(get_virtual_students[4:8])
    c = str(get_virtual_students[8:12])
    d = str(get_virtual_students[12:])
    e = [a, b, c , d]
    return e

# saves the data to virtual_teams.txt file
def virtual_teams_file(virtual_teams): 
    textfile = open("virtual_teams.txt", "w")
    for element in virtual_teams:
        textfile.write(element + "\n")
    textfile.close()

if __name__ == '__main__':
    # functions to get the students location
    dbn_campus_students(student_list())
    cpt_campus_students(student_list())
    jhb_campus_students(student_list())
    nw_campus_students(student_list())
      
    # functions for durban
    dbn_physical_students(dbn_campus_students(student_list()))
    dbn_physical_teams(dbn_physical_students(dbn_campus_students(student_list())))
    dbn_teams_file(dbn_physical_teams(dbn_physical_students(dbn_campus_students(student_list()))))
      
    # functions for cape town
    cpt_physical_students(cpt_campus_students(student_list()))
    cpt_physical_teams(cpt_physical_students(cpt_campus_students(student_list())))
    cpt_teams_file(cpt_physical_teams(cpt_physical_students(cpt_campus_students(student_list()))))
    
    # functions for johannesburg
    jhb_physical_students(jhb_campus_students(student_list()))
    jhb_physical_teams(jhb_physical_students(jhb_campus_students(student_list())))
    jhb_teams_file(jhb_physical_teams(jhb_physical_students(jhb_campus_students(student_list()))))
    
    # functions for northwest
    nw_physical_students(nw_campus_students(student_list()))
    nw_physical_teams(nw_physical_students(nw_campus_students(student_list())))
    nw_teams_file(nw_physical_teams(nw_physical_students(nw_campus_students(student_list()))))
    
    # functions for virtual students
    get_virtual_students(student_list())
    virtual_teams(get_virtual_students(student_list()))
    virtual_teams_file(virtual_teams(get_virtual_students(student_list())))
    
    pass
    

