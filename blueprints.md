## Pre Re-org

```
├── Procfile
├── app.py
├── config.py
├── db_create.py
├── db_create_users.py
├── manage.py
├── migrations
├── models.py
├── requirements.txt
├── sql.py
├── static
│   ├── bootstrap.min.css
│   └── bootstrap.min.js
├── templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   └── welcome.html
└── test.py
```

## Post Re-org

```
├── Procfile
├── app.py
├── config.py
├── db_create.py
├── db_create_users.py
├── manage.py
├── migrations
├── models.py
├── models.pyc
├── project
│   ├── __init__.py
│   └── users
│       ├── __init__.py
│       ├── templates
│       │   └── login.html
│       └── views.py
├── readme.md
├── requirements.txt
├── sql.py
├── static
│   ├── bootstrap.min.css
│   └── bootstrap.min.js
├── templates
│   ├── base.html
│   ├── index.html
│   └── welcome.html
└── tests.py
```