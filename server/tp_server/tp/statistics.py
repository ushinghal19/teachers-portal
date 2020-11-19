from .models import Error, Problem, Assignment, Teacher

# Req: _id = 100, assignment_id = 50 Give me Stats
# assignment = Assignment()


# Aggregate Errors:
def aggregate_errors(assignment: Assignment) -> int:
    """ Takes an assignment object and returns the total
        number of errors made by all students for that
        assignment

    """
    return sum(len(problem_id.errors) for problem_id in assignment.problems)
    # return len(Error.objects.filter(assignment_id = assignment))


# Per Problem Error:
def problem_errors(assignment: Assignment) -> dict:
    """ Takes an assignment object and returns a
        dictionary of each of the problems in the
        assignment and the number of errors all
        students made on that problem.
    """

    problems = {}
    problemNumber = 1

    for problem in assignment.problems:
        problems[problemNumber] = len(problem.errors)
        problemNumber += 1
    return problems

    # problems = {}
    # for i in Error.objects.filter(assignment_id = assignment):
    #     if i.problem_number in problems:
    #         problems[i.problem_number] += 1
    #     else:
    #         problems[i.problem_number] = 1
    # return problems


# Type of Error:
def type_of_errors(assignment: Assignment) -> dict:
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

    # errors = {}
    # for i in Error.objects.filter(assignment_id = assignment):
    #     if i.error_type in errors:
    #         errors[i.error_type] += 1
    #     else:
    #         errors[i.error_type] = 1


# Best Students and Worst Students:
def students_by_errors(assignment: Assignment) -> list:
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

    sorted_students = sorted(students, key=lambda x: students[x])
    return sorted_students

    # students = {}
    # for i in Error.objects.filter(assignment_id = assignment):
    #     if i.student_name in students:
    #         students[i.student_name] += 1
    #     else:
    #         students[i.student_name] = 1
    # sorted_students = sorted(students.items(), key=lambda item: item[1])
    # return sorted_students
