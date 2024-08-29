import json

def read_json_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def fill_report_structure(tests_structure, values_dict):
    if isinstance(tests_structure, dict):
        # перебираем ключи в словаре
        for key, value in tests_structure.items():
            # если ключ = "id", то заполняем соответствующее поле "value"
            if key == 'id' and value in values_dict:
                tests_structure['value'] = values_dict[value]
            elif isinstance(value, (dict, list)):
                fill_report_structure(value, values_dict)
    elif isinstance(tests_structure, list):
        for item in tests_structure:
            fill_report_structure(item, values_dict)

def main():
    values_file = 'values.json'
    tests_file = 'tests.json'
    report_file = 'report.json'

    values_data = read_json_file(values_file)
    tests_data = read_json_file(tests_file)

    # преобразуем содержимое values.json в словарь для быстрого доступа
    values_dict = {item['id']: item['value'] for item in values_data['values'] if isinstance(item, dict) and 'id' in item and 'value' in item}

    # проверяем тип данных, сохраняем значения из tests.json
    if isinstance(tests_data, dict) and 'tests' in tests_data:
        tests_structure = tests_data['tests']
        if isinstance(tests_structure, list):
            fill_report_structure(tests_structure, values_dict)

    # записываем результат в report.json
    with open(report_file, 'w', encoding='utf-8') as file:
        json.dump(tests_data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
