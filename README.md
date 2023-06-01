```
activate tools
mkdir test-py-env
cd test-py-env
git init
git config alias.czf "cz --name=cz_fogoprobr commit"
git config alias.l "log --oneline"
git config alias.s "status"
type nul > .gitignore
git czf
```

```
chore(.gitignore): Initial commit
```

```
pip install python-dotenv
```

```
type nul > .env
```

```py
# .env
PROJECT_ENV=development
KEY_WORD=your_key_word
```

```py
# .gitignore
.env
```

```
git add .gitignore
git s
git czf
```

```
chore(.gitignore): add .env
```

```
type nul > .env
```

```
git add script.py
git s
git czf
```

```
chore(script.py): create script.py
```

```py
# script.py
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

project_env = env_vars["PROJECT_ENV"]
key_word = env_vars["KEY_WORD"]

print('Your env is {}'.format(project_env))
print('Your key word is {}'.format(key_word))
```

```
(tools) \test-py-env>python script.py
Your env is development
Your key word is your_key_word
```

```
git add script.py
git s
git czf
```

```
feat(script.py): add env variables
```