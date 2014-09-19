## Current

```
├── Procfile
├── app.py
├── config.py
├── db_create.py
├── db_create_users.py
├── manage.py
├── migrations
├── models.py
├── project
│   ├── __init__.py
│   └── users
│       ├── __init__.py
│       ├── templates
│       │   └── login.html
│       └── views.py
├── readme.md
├── requirements.txt
├── sql.py
├── static
│   ├── bootstrap.min.css
│   └── bootstrap.min.js
├── templates
│   ├── base.html
│   ├── index.html
│   └── welcome.html
└── tests.py
```

## New Structure!

```
├── Procfile
├── config.py
├── db_create.py
├── db_create_users.py
├── manage.py
├── migrations
├── project
│   ├── __init__.py
│   ├── home
│   │   ├── __init__.py
│   │   ├── templates
│   │   │   ├── index.html
│   │   │   └── welcome.html
│   │   └── views.py
│   ├── models.py
│   ├── static
│   │   ├── bootstrap.min.css
│   │   └── bootstrap.min.js
│   ├── templates
│   │   └── base.html
│   └── users
│       ├── __init__.py
│       ├── templates
│       │   └── login.html
│       └── views.py
├── readme.md
├── requirements.txt
├── run.py
├── sql.py
└── tests.py
```