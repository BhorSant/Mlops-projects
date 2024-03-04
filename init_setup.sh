echo [$(date)] : "START"

echo [$(date)] : "creating env with python 3.8 version"

conda create --prefix ./env python=3.8 -y

echo [$(date)] :"activating the environment"

source activate ./env

echo [$(date)] : "installing the dev requiremnet"

pip install -r requirement_dev.txt

echo [$(date)] : "END"