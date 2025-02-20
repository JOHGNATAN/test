import os 


choose_folder = str(input('Escolha o volume: '))

list_of_folders = ['customers', 'orders', 'status']
diretorio = [f"C:\\Users\\johsilva\\Downloads\\{choose_folder}\\{i}" for i in list_of_folders]
    
for dir in diretorio:
    if os.path.exists(dir):
        for file_name in os.listdir(dir):
            file_path = os.path.join(dir, file_name)
            folder = os.path.basename(dir)
            object_name = f'{choose_folder}<</{folder}<</{file_name}<<'

            print(object_name)
            