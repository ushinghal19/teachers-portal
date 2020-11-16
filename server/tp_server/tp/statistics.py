from models import Error

# Req: teacher_id = 100, assignment_id = 50 Give me Stats
# assignment = Assignment()

# Aggregate Errors:
<<<<<<< HEAD
def aggregate_errors(assignment: Assignment) -> int:
    """ Takes an assignment object and returns the total
=======
def aggregateErrors(assignment: int) -> int:
    """ Takes an assignment id (int) and returns the total
>>>>>>> 47362f8a80065a3e0da81a38b95f2674ae2a57d0
        number of errors made by all students for that
        assignment

    """
    return len(Error.objects.filter(assignment_id = assignment))
    # return sum(len(problem.errors) for problem in assignment.problems)


# Per Problem Error:
<<<<<<< HEAD
def problem_errors(assignment: Assignment) -> dict:
    """ Takes an assignment object and returns a
=======
def problemErrors(assignment: int) -> dict:
    """ Takes an assignment id (int) and returns a
>>>>>>> 47362f8a80065a3e0da81a38b95f2674ae2a57d0
        dictionary of each of the problems in the 
        assignment and the number of errors all
        students made on that problem.
    """
    problems = {}
    for i in Error.objects.filter(assignment_id = assignment):
        if i.problem_number in problems:
            problems[i.problem_number] += 1
        else:
            problems[i.problem_number] = 1
    return problems

    # problems = {}
    # countError = 0
    # problemNumber = 1

    # for problem in assignment.problems:
    #     for error in problem.errors:
    #         countError += 1
    #     problems[problemNumber] = countError
    #     problemNumber += 1
    # return problems

# Type of Error:
<<<<<<< HEAD
def type_of_errors(assignment: Assignment) -> dict:
    """ Takes an assignment object and returns a 
=======
def typeOfErrors(assignment: int) -> dict:
    """ Takes an assignment id (int) and returns a 
>>>>>>> 47362f8a80065a3e0da81a38b95f2674ae2a57d0
        dictionary of each of the types of errors 
        made in the assignment, and how often they
        were made by all students. 
    """
    errors = {}
    for i in Error.objects.filter(assignment_id = assignment):
        if i.error_type in errors:
            errors[i.error_type] += 1
        else:
            errors[i.error_type] = 1

    # errors = {}
    # for problem in assignment.problems:
    #     for error in problem.errors:
    #         if error in errors:
    #             errors[error] += 1
    #         else:
    #             errors[error] = 1
    # return errors

# Best Students and Worst Students:
<<<<<<< HEAD
def students_by_errors(assignment: Assignment) -> list:
    """ Takes an assigment object and creates a
=======
def studentsByErrors(assignment: int) -> list:
    """ Takes an assigment id (int) and creates a
>>>>>>> 47362f8a80065a3e0da81a38b95f2674ae2a57d0
        sorted list of students ranked by how few
        to how many errors they made based on the #
        of calls.
    """
    students = {}
    for i in Error.objects.filter(assignment_id = assignment):
        if i.student_name in students:
            students[i.student_name] += 1
        else:
            students[i.student_name] = 1
    sorted_students = sorted(students.items(), key=lambda item: item[1])
    return sorted_students

    # students = {}
    # for problem in assignment.problems:
    #     for error in problem.errors:
    #         if error.student_name in students:
    #             students[error.student_name] += 1
    #         else:
    #             students[error.student_name] = 1

    # sorted_students = sorted(students, key= lambda x: students[x])
    # return sorted_students
