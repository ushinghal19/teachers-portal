from models import Error

# Req: teacher_id = 100, assignment_id = 50 Give me Stats
# assignment = Assignment()

# Aggregate Errors:
def aggregateErrors(assignment: int) -> int:
    """ Takes an assignment id (int) and returns the total
        number of errors made by all students for that
        assignment

    """
    return len(Error.objects.filter(assignment_id = assignment))
    # return sum(len(problem.errors) for problem in assignment.problems)


# Per Problem Error:
def problemErrors(assignment: int) -> dict:
    """ Takes an assignment id (int) and returns a
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
def typeOfErrors(assignment: Assignment) -> dict:
    """ Takes an assignment object and returns a 
        dictionary of each of the types of errors 
        made in the assignment, and how often they
        were made by all students. 
    """

    errors = {}
    for problem in assignment.problems:
        for error in problem.errors:
            if error in errors:
                errors[error] += 1
            else:
                errors[error] = 1
    return errors

# Best Students and Worst Students:
def studentsByErrors(assignment: Assignment) -> list:
    """ Takes an assigment object and creates a
        sorted list of students ranked by how few
        to how many errors they made based on the #
        of calls.
    """
    students = {}
    for problem in assignment.problems:
        for error in problem.errors:
            if error.student_name in students:
                students[error.student_name] += 1
            else:
                students[error.student_name] = 1

    sorted_students = sorted(students, key= lambda x: students[x])
    return sorted_students
