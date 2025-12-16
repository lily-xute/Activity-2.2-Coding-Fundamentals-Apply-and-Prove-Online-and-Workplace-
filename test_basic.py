from db import add_project, get_all_projects

def func(name, description, status):
	add_project(name, description, status)
	return get_all_projects()


def test_answer():
	assert func("Project 1", "Description 1", "Active") != []