from fastapi import FastAPI

app = FastAPI()

students = [
	{'name': 'S1', 'age': 20},
	{'name': 'S2', 'age': 18},
	{'name': 'S3', 'age': 16}
]

@app.get('/students')
def user_list():
	return {'students': students}
