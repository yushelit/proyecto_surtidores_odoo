import csv
import random
from os import remove
from os import path

lista_enteros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_combustibles = [0, 1, 2, 3, 4]


def write_text(text, name_file):
    with open(name_file, 'a') as f:
        f.write(text)


def write_clientes(line, name_file, identificador):
    write_text(f'<record id=\'cliente{identificador}\' model=\'surtidores.cliente\'>', name_file)
    write_text(f'<field name=\'name\'>{line[0]}</field>', name_file)
    write_text(f'<field name=\'dni\'>{line[1]}</field>', name_file)
    write_text(f'<field name=\'apellidos\'>{line[2]}</field>', name_file)
    write_text(f'<field name=\'ciudad\'>{line[3]}</field>', name_file)
    write_text(f'<field name=\'edad\'>{line[4]}</field>', name_file)
    write_text(f'<field name=\'direccion\'>{line[5].strip()}</field>', name_file)

    write_text('</record>', name_file)


def write_camion(line, name_file, identificador):
    write_text(f'<record id=\'camion{identificador}\' model=\'surtidores.camion\'>', name_file)
    write_text(f'<field name=\'name\'>{line[0]}</field>', name_file)
    write_text(f'<field name=\'modelo\'>{line[1]}</field>', name_file)
    write_text(f'<field name=\'altura\'>{line[2].strip()}</field>', name_file)
    write_text('</record>', name_file)


def write_productos(line, name_file, identificador):
    write_text(f'<record id=\'producto{identificador}\' model=\'surtidores.producto\'>', name_file)
    write_text(f'<field name=\'name\'>{line[0]}</field>', name_file)
    write_text(f'<field name=\'precio\'>{line[1].strip()}</field>', name_file)
    write_text('</record>', name_file)


def write_envases(line, name_file, identificador):
    write_text(f'<record id=\'envase{identificador}\' model=\'surtidores.envase\'>', name_file)
    write_text(f'<field name=\'name\'>{line[0]}</field>', name_file)
    write_text(f'<field name=\'capacidad\'>{line[1].strip()}</field>', name_file)
    write_text(f'<field name=\'tipo_combustible\' ref=\'producto{random.choice(lista_combustibles)}\'/>', name_file)
    write_text('</record>', name_file)


def write_viajes(line, name_file, identificador):
    write_text(f'<record id=\'viaje{identificador}\' model=\'surtidores.viaje\'>', name_file)
    write_text(f'<field name=\'origen\'>{line[0]}</field>', name_file)
    write_text(f'<field name=\'destino\'>{line[1].strip()}</field>', name_file)
    write_text(f'<field name=\'camion\' ref=\'camion{random.choice(lista_enteros)}\'/>', name_file)
    write_text(f'<field name=\'cliente\' ref=\'cliente{random.choice(lista_enteros)}\'/>', name_file)
    write_text(f'<field name=\'envases\' eval=\"[(6, 0, [ref(\'envase{random.choice(lista_enteros)}\'), ref(\'envase{random.choice(lista_enteros)}\')])]"/>', name_file)
    # write_text(f'<field name=\'fecha\'>{line[2].strip()}</field>', name_file)
    write_text('</record>', name_file)


def delete_file(name_file):
    if path.exists(name_file):
        remove(name_file)


def clientes_generator(name_file):
    delete_file(name_file)
    write_text('<odoo><data>', name_file)
    identificador = 0
    with open('clientes.csv') as file:
        for line in file:
            line = line.split(',')
            write_clientes(line, name_file, identificador)
            identificador += 1
    write_text('</data></odoo>', name_file)


def camiones_generator(name_file):
    delete_file(name_file)
    write_text('<odoo><data>', name_file)
    identificador = 0
    with open("camiones.csv") as file:
        for line in file:
            line = line.split(',')
            write_camion(line, name_file, identificador)
            identificador += 1
    write_text('</data></odoo>', name_file)


def productos_generator(name_file):
    delete_file(name_file)
    write_text('<odoo><data>', name_file)
    identificador = 0
    with open("productos.csv") as file:
        for line in file:
            line = line.split(',')
            write_productos(line, name_file, identificador)
            identificador += 1
    write_text('</data></odoo>', name_file)


def envases_generator(name_file):
    delete_file(name_file)
    write_text('<odoo><data>', name_file)
    identificador = 0
    with open("envases.csv") as file:
        for line in file:
            line = line.split(',')
            write_envases(line, name_file, identificador)
            identificador += 1
    write_text('</data></odoo>', name_file)


def viajes_generator(name_file):
    delete_file(name_file)
    write_text('<odoo><data>', name_file)
    identificador = 0
    with open("viajes.csv") as file:
        for line in file:
            line = line.split(',')
            write_viajes(line, name_file, identificador)
            identificador += 1
    write_text('</data></odoo>', name_file)


clientes_generator('demo/clientes.xml')
camiones_generator('demo/camiones.xml')
productos_generator('demo/productos.xml')
envases_generator('demo/envases.xml')
viajes_generator('demo/viajes.xml')
