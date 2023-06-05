from os import remove
from os import path

def write_text(text, name_file):
    with open(name_file, 'a') as f:
        f.write(text)

def write_camion(line, name_file):
    write_text(f'<record id=\'student{line[1]}\' model=\'school.student\'>', name_file)
    write_text(f'<field name=\'name\'>{line[0]}</field>', name_file)
    write_text(f'<field name=\'modelo\'>{line[1]}</field>', name_file)
    write_text(f'<field name=\'altura\'>{line[2]}</field>', name_file)
    write_text(f'<field name=\'foto\'>{line[3]}</field>', name_file)
    write_text('</record>', name_file)

def write_clientes(line, name_file):
    write_text(f'<record id=\'cliente{line}\' model=\'surtidores.cliente\'>', name_file)
    write_text(f'<field name=\'name\'>{line[1]}</field>', name_file)
    write_text(f'<field name=\'dni\'>{line[2]}</field>', name_file)
    write_text(f'<field name=\'apellidos\'>{line[3]}</field>', name_file)
    write_text(f'<field name=\'ciudad\'>{line[4]}</field>', name_file)
    write_text(f'<field name=\'edad\'>{line[5]}</field>', name_file)
    write_text(f'<field name=\'foto\'>{line[6]}</field>', name_file)
    write_text(f'<field name=\'direccion\'>{line[7]}</field>', name_file)
    write_text('</record>', name_file)

def delete_file(name_file):
    if path.exists(name_file):
        remove(name_file)

def clientes_generator(name_file):
    delete_file(name_file)
    write_text('<odoo><data>', name_file)
    with open("clientes.csv") as file:
        for line in file:
            write_clientes(line.strip(), name_file)
    write_text('</data></odoo>', name_file)


def camiones_generator(name_file):
    delete_file(name_file)
    write_text('<odoo><data>', name_file)
    with open("camiones.csv") as file:
        for line in file:
            line = line.split(',')
            write_camion(line, name_file)
    write_text('</data></odoo>', name_file)


clientes_generator('demo/clientes.xml')
camiones_generator('demo/camiones.xml')
