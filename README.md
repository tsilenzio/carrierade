# Carrierade
App for carrier for stuffs

## Install
Within the directory of the project run the following

Windows
```
python3 -m venv .venv
source .venv\bin\activate.ps1

python3 -m pip install -r requirements.txt
```

MacOS
```
pytheon3 -m vnv .venv
source .venv/bin/activate

python3 -m pip install -r requirements.txt
```

## Build application
Compiles the Qt6 Designer UI files into Python files

Make sure to activate the python virtual environment first
```
invoke build
```

## Start application
Starts the application without the need to compile it to a system executable binary

Make sure to activate the python virtual environment first

```
invoke start
```

## Compile application
Compiles the application into a system executable binary

Make sure to activate the python virtual environment first

```
invoke compile
```
