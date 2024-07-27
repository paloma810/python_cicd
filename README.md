# python_cicd

## Directory
```
├── common_lib/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── lambda_functions/
│   ├── 01_function1/
│   │   ├── handler.py
│   │   ├── requirements.txt
│   │   └── test_handler.py
│   ├── 02_function2/
│   │   ├── handler.py
│   │   ├── requirements.txt
│   │   └── test_handler.py
│   └── ...
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```
## CI Pipline
* if you change & push the *.sh, bellow task is executed.
  1. lint by shellcheck (severity=error)
  2. unit test by shellspec
  3. checking test coverage >= 70% by shellspec (kcov)
* if you change & push the *_spec.sh, bellow task is executed.
  1. unit test by shellspec
  2. checking test coverage >= 70% by shellspec (kcov)
