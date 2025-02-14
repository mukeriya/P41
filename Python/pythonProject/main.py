def create_directory_structure(base_path):
# Створюємо основну директорію
# os.makedirs(base_path, exist_ok=True)
# Додаємо першу директорію і файл
# dir_1 = os.path.join(base_path, 'Dir_1')
# os.makedirs(dir_1, exist_ok=True)
# with open(os.path.join(dir_1, 'file_1.txt'), 'w') as f: f.write('Це файл 1') # Додаємо другу директорію і файли dir_2 = os.path.join(base_path, 'Dir_2') os.makedirs(dir_2, exist_ok=True) with open(os.path.join(dir_2, 'file_2.txt'), 'w') as f: f.write('Це файл 2') with open(os.path.join(dir_2, 'file_3.txt'), 'w') as f: f.write('Це файл 3') # Додаємо третю директорію і файл dir_3 = os.path.join(base_path, 'Dir_3') os.makedirs(dir_3, exist_ok=True) with open(os.path.join(dir_3, 'file_4.txt'), 'w') as f: f.write('Це файл 4') # Викликаємо функцію для створення структури create_directory_structure('MyDirectoryStructure')