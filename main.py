import csv


def write_list_of_dicts_to_csv(filename, data):
    # Carga de archivos
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def read_csv_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def update_grocery_data(original_data, new_data):
    # Update comparando archivos considerando lo siguiente:

    original_dict = {d['SKU']: d for d in original_data}

    for row in new_data:
        sku = row['SKU']
        if sku in original_dict:
            # Si el articulo ya existe en la fuente de datos incrementa su valor de cantidad por la suma de ambas cantidades.
            original_row = original_dict[sku]
            original_row['Quantity'] = str(
                int(original_row['Quantity']) + int(row['Quantity']))
        else:
            # Si el articulo no existe en tu fuente de datos agregalo.
            original_data.append(row)
            original_dict[sku] = row

    return original_data


def main():
    # Cargar
    original_data = read_csv_to_dict('sample_grocery.csv')
    batch_data = read_csv_to_dict('grocery_batch_1.csv')

    # Actualizar
    updated_data = update_grocery_data(original_data, batch_data)

    # Guardar
    write_list_of_dicts_to_csv('grocery_db.csv', updated_data)


if __name__ == '__main__':
    main()
