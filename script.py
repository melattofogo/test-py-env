# script.py
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

project_env = env_vars["PROJECT_ENV"]
key_word = env_vars["KEY_WORD"]

print('Your env is {}'.format(project_env))
print('Your key word is {}'.format(key_word))