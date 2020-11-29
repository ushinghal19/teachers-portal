# Data Gathering:

## Incoming Data Points:
  - Assignment ID
  - Student Name
  - Type of Error (broken)
  - The # of Errors
  - Question #
 
## Statistics to gather:
   1. Total # of errors by student over the assignment. **(Priority Statistic)**
      * Aggregated into the total # of all student errors in the assignment. (Scalar)
   2. Total # of errors by students on a question
      * Aggregated into the total # of all student errors for that question. (Bar Graph) IV: Question, DV: # of Errors
   3. Average total time taken to complete the assignemnt
      * Use k-clustering analysis for the time between check math server calls.
   4. Type of error made by student
      * Aggregated into total error counts for all students. (Pie Chart / Bar Graph)
   5. Best students (Top 3-5)
      * Least # of Errors per Server Call
   6. Students who need to improve most (Bottom 3-5)
      * Most # of Errors per Server Call


## Known Issues and Fixes:
* An upcoming release of Djongo will fix this, but for now, navigate to your pipenv and find the 
file `\.virtualenvs\<your-pipenv>\Lib\site-packages\djongo\models\fields.py`. Go to line 1014 and 
change `def from_db_value(self, value, expression, connection, context):` to 
`    def from_db_value(self, value, expression, connection, context=None):`
