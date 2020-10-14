import pytest
import System


username = 'luke'
password =  '#yeet'
username2 = 'Jason'
username3 = 'yted91'
course = 'software engineering'
assignment = 'assignment7'
profUser = 'goggins'
profPass = 'augurrox'

#Tests if the program can handle a wrong username
def test_login(grading_system):
    username = 'luke'
    password =  '#yeet'
    grading_system.login(username,password)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

###2 password###

def test_check_password(grading_system):
    test = grading_system.check_password(username,password)
    test2 = grading_system.check_password(username,'#yeet')
    test3 = grading_system.check_password(username,'#YEET')
    if test == test3 or test2 == test3:
        assert False
    if test != test2:
        assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem


###3 Change grade###
def test_change_grade(grading_system):
    grading_system.change_grade(profUser)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

###4 create_assignment ###
def test_creat_assignment(grading_system):
    grading_system.create_assignment(staff, duedate, course)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

###5 Add_student ###
def test_add_student(grading_system):
    grading_system.add_student(username,course)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

###6 drop_student ###
def test_drop_student(grading_system):
    grading_system.drop_student(username,course)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

###7 submit assignment ###
def test_submit_assignment(grading_system):
    grading_system.submit_assignment(username, password, course)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

### 8 check_ontime ###
def test_check_ontime(grading_system):
    grading_system.check_ontime(username,due)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

### 9 check_grade ###
def test_check_grade(grading_system):
    grading_system.check_grade(grade,course, username)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

### 10 view_assignment ###
def test_view_assignment(grading_system):
    grading_system.view_assignment(assignment, course)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

### 11 midterm_score
def test_midterm_score(grading_system):
    grading_system.midterm_score(profUser, username, grade, course)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

### 12 final_score ###
def test_final_score(grading_system):
    grading_system.final_score(profUser, username, grade, course)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

### 13 quiz_score ###
def test_quiz_score(grading_system):
    grading_system.quiz_score(profUser, grade, course)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

### 14 group_score ###
def test_group_score(grading_system):
    grading_system.group_score(profPass, grade, course, username)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

### 15 project_score ###
def test_project_score(grading_system):
    grading_system.project_score(profUser, grade, course)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem