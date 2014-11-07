pip install -r requirements.txt

autopep8 -ir .
flake8 --max-complexity=10 --exclude=*.txt,*.md --max-line-length=200 .

lettuce test
python Test_Figura.py -v
coverage run --branch Test_Figura.py
coverage report -m
coverage html --title="Cobertura de Figura"