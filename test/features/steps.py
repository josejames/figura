# -*- coding: utf-8 -*-
from lettuce import *
import sys
sys.path.append('../')
from Figura import Figura

@step(u'Given: Que la figura es un "([^"]*)" y el lado es "([^"]*)"')
def given_que_la_figura_es_un_cuadrado_y_el_lado_es_6(step, figura, lado):
    world.parametros = [figura, int(lado)]

@step(u'Given: Que la figura es un "([^"]*)" y el ancho es "([^"]*)" y de altura "([^"]*)"')
def given_que_la_figura_es_un_group1_y_el_ancho_es_group2_y_de_altura_group3(step, figura, lado, lado2):
	world.parametros = [figura, int(lado), int(lado2)]

@step(u'When realizo el calculo')
def when_realizo_el_calculo(step):
    fig = Figura(world.parametros)
    world.area = fig.getArea()

@step(u'Then obtengo el resultado "([^"]*)"')
def then_obtengo_el_resultado_36(step, area):
    assert world.area == int(area), 'area calculada {0}, area esperada {1}'.format(world.area, area)

@step(u'Then obtengo el resultado con decimales es "([^"]*)"')
def then_obtengo_el_resultado_con_decimales_es_group1(step, area):
	assert float(world.area) == float(area), 'area calculada {0}, area esperada {1}'.format(world.area, area)	
    
