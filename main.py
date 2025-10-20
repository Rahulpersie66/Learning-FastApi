from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field

from fastapi import FastAPI, HTTPException
app = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    name : str = Field(..., min_length=3, max_length=512, description="Task name")
    description : str = Field(...,description='description abbout the task' )
    priority : Priority = Field(default=Priority.LOW, description='priority of the task')
    
class TodoBaseCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int = Field(..., description='Unique value id for todo tasks')
    
class TodoUpdate(BaseModel):
    name : Optional[str] = Field(None, min_length=3, max_length=512, description="Task name")
    description : Optional[str] = Field(None,description='description abbout the task' )
    priority : Optional[Priority] = Field(None, description='priority of the task')
    
    

#todo_list -- think of ot as DB 
todos = [
    {"id": 1, "task": "Buy groceries", "completed": False},
    {"id": 2, "task": "Read a book", "completed": True},
    {"id": 3, "task": "Write code", "completed": False},
    {"id": 4, "task": "Go for a walk", "completed": True},
    {"id": 5, "task": "Cook dinner", "completed": False},
    {"id": 6, "task": "Clean the house", "completed": True},
    {"id": 7, "task": "Pay bills", "completed": False},
    {"id": 8, "task": "Exercise", "completed": True},
    {"id": 9, "task": "Call a friend", "completed": False},
    {"id": 10, "task": "Plan a trip", "completed": True},{"id": 11, "task": "Attend meeting", "completed": False},
    {"id": 12, "task": "Write blog post", "completed": True},
    {"id": 13, "task": "Watch a movie", "completed": False}
]

all_todos = [
    Todo(id=1, name="Gym work", description="Gym schedule", priority=Priority.LOW),
    Todo(id=2, name="Buy groceries", description="Get fruits and vegetables", priority=Priority.MEDIUM),
    Todo(id=3, name="Write blog", description="Write about FastAPI", priority=Priority.HIGH),
    Todo(id=4, name="Read book", description="Read Clean Code", priority=Priority.LOW),
    Todo(id=5, name="Cook dinner", description="Prepare pasta tonight", priority=Priority.MEDIUM),
]


# # get call api 
# @app.get("/")
# async def index_page():
#     return {"message": "hello world"}

# to show all todos get endpoint
@app.get('/todos/all', response_model=List[Todo])
async def all_todos_func():
    if all_todos:
        return all_todos
    else:
        raise HTTPException(status_code=404, detail='Lost dtaa')
    
# get calll to get data from todo all list using `path paramter`
@app.get('/todos/{todo_id}', response_model=Todo)
async def get_todo_by_id(todo_id: int):
    for todo in all_todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=420, detail="Todo not found")


# get call to get data from todo all list using `query paramter`
@app.get("/todos", response_model=List[Todo])
async def get_todo_by_query(first_n:int):
    todo_list =[]
    for todo in all_todos:
        todo_list.append(todo)
    if todo_list and first_n:
        return todo_list[:first_n]
    raise HTTPException(status_code=404, detail='Not found todos of the list')

#post method api end point
@app.post('/todos/', response_model=TodoBaseCreate)
def add_todo(todo_task:TodoBaseCreate):
    new_t_id = max([int(todo.id) for todo in all_todos])+1
    task = Todo(id=new_t_id, name=todo_task.name, description= todo_task.description, priority=todo_task.priority)
    print(type(task))
    if task:
        all_todos.append(task)
        return task
    else:
        raise HTTPException(status_code=404, detail='Crashed while savving post')

# put metod to update the resoource at server
@app.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id:int, update_todo: TodoUpdate):
    for todo in all_todos:
        if todo.id == todo_id:
            if update_todo.name:
                todo.name = update_todo.name
            if update_todo.description:
                todo.description = update_todo.description
            if update_todo.priority:
                todo.priority = update_todo.priority
            return todo
    raise HTTPException(status_code=404, detail='erro in updating')

# to delete specific todo
@app.delete('/todos/{todo_id}', response_model=Todo)
def delete_todo(todo_id:int):
    for index, todo in enumerate(all_todos):
        if todo.id == todo_id:
            delete_todo = all_todos.pop(index)
            return delete_todo
    raise HTTPException(status_code=404, detail='Not deleted exception')