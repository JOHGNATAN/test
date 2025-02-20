import os

# Diretório onde os arquivos estão localizados
list = ['customers', 'orders', 'status']
choose_folder = input('Escolha a pasta: ')

diretorio = [f"C:\\Users\\johsilva\\Downloads\\{choose_folder}\\{i}" for i in list]

def renomear_arquivos(diretorio):
    for dir in diretorio:
        if os.path.exists(dir):
           for file_name in os.listdir(dir):
               
               try:
                   novo_nome = os.path.join(dir, f'{choose_folder}_' + os.path.basename(dir) + '_' + file_name)
                   os.rename(os.path.join(dir, file_name), novo_nome)
                   print(novo_nome)

               except Exception as e:
                   print(f'Ocorreu um erro {e}')  

        else:
            print(f'Diretório "{dir}" não encontrado')

# renomear_arquivos(diretorio)


####################################################################################


# def undo(diretorio):
#     for dir in diretorio:
#         if os.path.exists(dir):
#            for file_name in os.listdir(dir):
               
#                try:
#                    nome_antigo = os.path.join(dir, file_name)
#                    new_name = os.path.join(dir, nome_antigo.split('_')[-1])
#                    os.rename(nome_antigo, new_name)
                
#                except Exception as e:
#                    print(f'Ocorreu um erro {e}') 
                         
#         else:
#             print(f'Diretório "{dir}" não encontrado')

# undo(diretorio)


