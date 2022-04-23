
### Creacion del enviroment para instalar las versiones y librerias que se necesitaran en el proyecto

python3 -m venv code-facilito
python --version

source code-facilito/Scripts/activate

cd despliegue/
pip install -r requirements.txt

python main.py


API
http://127.0.0.1:3000/docs

FRONTEND
http://localhost:4200/