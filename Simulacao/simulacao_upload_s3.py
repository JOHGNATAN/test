import boto3
import os
import time

bucket_name = 'files-tobe-processed'

def upload_to_s3(file_name, bucket_name, object_name):
    s3_client = boto3.client('s3')
    return s3_client.upload_file(file_name, bucket_name, object_name)

def import_files(choose_folder):
    
    list_of_folders = ['customers', 'orders', 'status']
    diretorio = [f"C:\\Users\\johsilva\\Downloads\\{choose_folder}\\{i}" for i in list_of_folders]
    
    if choose_folder == 'full_load':
        for dir in diretorio:
            if os.path.exists(dir):
                for file_name in os.listdir(dir):
                    file_path = os.path.join(dir, file_name)
                    folder = os.path.basename(dir)
                    object_name = f'{choose_folder}/{folder}/{file_name}'

                    try:
                        upload_to_s3(file_path, bucket_name, object_name)
                        print(f'✅ {file_name} uploaded to {object_name}')
                    except Exception as e:
                        print(f'Ocorreu um erro: {e}')

    elif choose_folder == 'cdc':
        files_to_upload = {folder: [] for folder in list_of_folders}
        for dir in diretorio:
            if os.path.exists(dir):
                for file_name in os.listdir(dir):
                    file_path = os.path.join(dir, file_name)
                    folder = os.path.basename(dir)
                    object_name = f'{choose_folder}/{folder}/{file_name}'
                    files_to_upload[folder].append((file_path, object_name))
        
        while any(files_to_upload.values()):
            for folder in list_of_folders:
                if files_to_upload[folder]:
                    file_path, object_name = files_to_upload[folder].pop(0)
                    try:
                        upload_to_s3(file_path, bucket_name, object_name)
                        print(f'✅ {os.path.basename(file_path)} uploaded to {object_name}')
                    except Exception as e:
                        print(f'Ocorreu um erro: {e}')
            print('Aguardando 10 minutos...')
            time.sleep(600)

def util():
    choose_folders = ['full_load', 'cdc']
    for volume in choose_folders:
        try:
            import_files(volume)
        except Exception as e:
            print(f'Ocorreu um erro: {e}')
