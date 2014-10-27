Feature: Obtener el area de figuras geometricas basicas
	Como usuario del sistema
	Quiero obtener el area  de distintas figuras
	Para facilitar algunos otros calculos

Scenario: "Cuadrado" y el lado es "6"
	Given: Que la figura es un "cuadrado" y el lado es "6"
	When realizo el calculo
	Then obtengo el resultado "36"

Scenario: "Cuadrado" y el lado es "8"
	Given: Que la figura es un "cuadrado" y el lado es "8"
	When realizo el calculo
	Then obtengo el resultado "64"

Scenario: "Cuadrado" y el lado es "10"
	Given: Que la figura es un "cuadrado" y el lado es "10"
	When realizo el calculo
	Then obtengo el resultado "100"

Scenario: "Circulo" y el radio es "3"
	Given: Que la figura es un "circulo" y el lado es "3"
	When realizo el calculo
	Then obtengo el resultado con decimales es "28.27"

Scenario: "Circulo" y el radio es "5"
	Given: Que la figura es un "circulo" y el lado es "5"
	When realizo el calculo
	Then obtengo el resultado con decimales es "78.54"

Scenario: "Circulo" y el radio es "9"
	Given: Que la figura es un "circulo" y el lado es "9"
	When realizo el calculo
	Then obtengo el resultado con decimales es "254.47"

Scenario: "Rectangulo" y el lado es "9" y altura "3"
	Given: Que la figura es un "rectangulo" y el ancho es "9" y de altura "3"
	When realizo el calculo
	Then obtengo el resultado "27"

Scenario: "Rectangulo" y el lado es "4" y altura "5"
	Given: Que la figura es un "rectangulo" y el ancho es "4" y de altura "5"
	When realizo el calculo
	Then obtengo el resultado "20"