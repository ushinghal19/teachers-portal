

def aggregate_errors(assignment) -> int:
    """ Takes an assignment object and returns the total
        number of errors made by all students for that
        assignment

    """
    return sum(len(problem.errors.all()) for problem in assignment.problems.all())


def problem_errors(assignment) -> dict:
    """ Takes an assignment object and returns a
        dictionary of each of the problems in the
        assignment and the number of errors all
        students made on that problem.
    """

    problems = {}
    problem_number = 1

    for problem in assignment.problems.all():
        problems[problem_number] = len(problem.errors.all())
        problem_number += 1
    return problems


def type_of_errors(assignment) -> dict:
    """ Takes an assignment object and returns a
        dictionary of each of the types of errors
        made in the assignment, and how often they
        were made by all students.
    """

    errors = {}
    for problem in assignment.problems.all():
        for error in problem.errors.all():
            if error.error_type in errors:
                errors[error.error_type] += 1
            else:
                errors[error.error_type] = 1
    return errors


def students_by_errors(assignment) -> dict:
    """ Takes an assignment object and creates a
        sorted list of students ranked by how few
        to how many errors they made based on the #
        of calls.
    """

    students = {}
    for problem in assignment.problems.all():
        for error in problem.errors.all():
            if error.student_name in students:
                students[error.student_name] += 1
            else:
                students[error.student_name] = 1

    students = {key: value for key, value in sorted(students.items(), key=lambda item: item[1])}
    return students
