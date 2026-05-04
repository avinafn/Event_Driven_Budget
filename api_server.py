from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Event_driven_budget import ExpenseRequest, HeapManagment

#web server initialization
app = FastAPI(title="Event Budget Allocator API")

program = HeapManagment()

TOTAL_BUDGET = 5000.00
STARTING_BUDGET = 5000.00

#BaseModel from Pydantic library assures the correctness of datatypes of JSON data
#in this case gives an error message instead of crashing the application
class expenseChecker(BaseModel):
    description: str
    department: str
    amount: float
    priority: int


#when a user sends a request run the function below it
@app.post("/submit_expense")
def submit_expense(payload: expenseChecker):
    global TOTAL_BUDGET

    if TOTAL_BUDGET < (STARTING_BUDGET * 0.10) and payload.priority < 7:
        raise HTTPException(status_code = 400, detail = "CANNOT MOVE ON...")
    request = ExpenseRequest(payload.description, payload.department, payload.amount, payload.priority)
    program.insert(request)

    return {"status" : "success" }

@app.get("/process_program")
def process_program():
    global TOTAL_BUDGET
    approved = []
    denied = []

    while len(program.heap) > 0:
        expense = program.removeMax()

        if expense.amount <= TOTAL_BUDGET:
            TOTAL_BUDGET -= expense.amount
            approved.append(expense)
        else:
            denied.append(expense)

    return {"budget_remaining" : TOTAL_BUDGET}