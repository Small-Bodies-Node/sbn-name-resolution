#! /usr/bin/env false

### 0. Load vars defined in .env
if [ ! -f $PWD/.env ]; then
    echo "No .env file found!!!"
    return 1
fi
source .env

### 1. Message user
clear
echo """${GRE}
=======================================================
        Initializing Python Virtual Environment
=======================================================
 ${WHI}"""

sleep 1

### 2. Get rid of caches NOT in .venv
find . -type d ! -path './.venv/*' -name '__pycache__' -exec rm -rf {} +
find . -type d ! -path './.venv/*' -name '.pytest_cache' -exec rm -rf {} +
find . -type d ! -path './.venv/*' -name '.mypy_cache' -exec rm -rf {} +

### 3. Check for existence of `.venv` dir
if [[ ! -d $PWD/.venv ]]; then
    echo """${BLU}
    virtual Environment Not Found -- Creating '.venv'
"""
    $PYTHON_3_5_OR_HIGHER -m venv .venv
fi

### 4. Activate VENV
source ./.venv/bin/activate

### 5. Install package dependencies for project
pip install --upgrade -q -q -q pip
pip install -q -r requirements.vscode.txt
pip install -q -r requirements.txt

### 6. Link git pre-commit-hook script
ln -fs $PWD/_precommit_hook $PWD/.git/hooks/pre-commit

### 7. Final Message
echo """${BLU}
    Done. Bon courage!
${WHI}
"""
