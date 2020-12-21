from gql import Client, gql
import requests
from gql.transport.requests import RequestsHTTPTransport
from requests import Response

# with open('schema.graphql') as f:
#     schema_str = f.read()


def create_assignment(url: str, assignment_id: str, teacher_id: str, assignment_name: str) -> Response:
    # transport = RequestsHTTPTransport(url="https://countries.trevorblades.com/",
    #                                   verify=True, retries=3)

    # client = Client(transport=transport, schema=schema_str)

    mutation_string = """
      mutation newAssignment($assignmentId: String, $teacherId: String, $assignmentName: String){
      createNewAssignment(assignmentId: $assignmentId, teacherId: $teacherId,
                            assignmentName: $assignmentName){
         assignment{
          assignmentId,
          assignmentName
        }
    }
    }
    """

    # mutation = gql(mutation_string)

    variables = {'assignmentId': assignment_id, 'teacherId': teacher_id,
                 'assignmentName': assignment_name}

    body = {"query": mutation_string, "variables": variables}

    # result = client.execute(mutation, variable_values=params)
    r = requests.post(url, json=body)
    return r


def create_error(url: str, assignment_id: str, error_id: str, error_type: str,
                 problem_number: int, student_name: str) -> Response:
    mutation_string = """
     mutation newError($assignmentId:String, $errorId:String, $errorType:String, $problemNumber:Int,
      $studentName:String){
      createNewError(assignmentId: $assignmentId, errorId:$errorId,
        errorType:$errorType, problemNumber: $problemNumber, studentName:$studentName){
        error{
          errorId,
          errorType
        }
      }
    }
        """

    variables = {'assignmentId': assignment_id, 'errorId': error_id,
                 'errorType': error_type, 'problemNumber': problem_number,
                 'studentName': student_name}

    body = {"query": mutation_string, "variables": variables}
    print(f"id: {error_id}")
    r = requests.post(url, json=body)
    return r


if __name__ == "__main__":
    pass
    # print(create_assignment(r'http://127.0.0.1:8000/graphql', "601",
    #                         "5fb6d6ce00c239d5bffb4b15", "TLI Demo Math Assignment"))
    #
    # print(create_error(r'http://127.0.0.1:8000/graphql', "123", "error4", "UnknownError", 1,
    #                    "Omri"))
