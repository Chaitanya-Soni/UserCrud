# UserCrud
```

APIs for Auth 
for signup http://127.0.0.1:8000/api/v1/auth/register/ with body as {email="email@email.com" username="USERNAME" password="PASSWORD" password2="PASSWORD"}
for login  http://127.0.0.1:8000/api/v1/auth/token/  with body as {email="email@email.com" username="USERNAME"}
```
# for CRUD  operations

```
Get all tasks
http http://127.0.0.1:8000/api/v1/task/ "Authorization: Bearer {YOUR_TOKEN}" 
Get a single task
http GET http://127.0.0.1:8000/api/v1/task/{task id}/ "Authorization: Bearer {YOUR_TOKEN}" 
Create a new task
http POST http://127.0.0.1:8000/api/v1/task/ "Authorization: Bearer {YOUR_TOKEN}" taskdetail="temp" 
Full update a task
http PUT http://127.0.0.1:8000/api/v1/task/{task id}/ "Authorization: Bearer {YOUR_TOKEN}" taskdetail="temp" 
Partial update a task
http PATCH http://127.0.0.1:8000/api/v1/task/{task id}/ "Authorization: Bearer {YOUR_TOKEN}" taskdetail="temp" 
Delete a task
http DELETE http://127.0.0.1:8000/api/v1/task/{task_id}/ "Authorization: Bearer {YOUR_TOKEN}"
```
