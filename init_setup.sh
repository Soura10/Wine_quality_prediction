echo [$(date)]: "START"
echo [$(date)]: "creating environment with python 3.8 version"
conda create --prefix ./wine python=3.8 -y
echo [$(date)]: "activating the environment"
source activate ./wine
echo [$(date)]: "installing the requirements"
pip install -r requirements.txt
echo [$(date)]: "END"