Feature: Task List
  Testing task list

  Scenario: Adding task to the tasklist
    Given tasklist exists
     When user says "Add task do homework"
      And assistant processes input
     Then task is added
      And assistant replies "Task Added"

  Scenario: Adding task fails because of invalid input
    Given tasklist exists
     When user says "horyamba-moryamba"
      And assistant processes input
     Then assistant asks to repeat

