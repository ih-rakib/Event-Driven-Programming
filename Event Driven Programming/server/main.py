import glob
import shutil
import os 
from zipfile import ZipFile

source_path = '../source/*'
destination_path = '../destination'

numbers = [1, 2, 3]

while True : 
    source_object = glob.glob(source_path)
    if len(source_object) > 0 : 
        object_path = source_object[0]
        object_name = object_path.split('\\')[-1].split('.')
        prefix = object_name[0]
        postfix = object_name[1]

        if postfix == 'txt' : 
            shutil.copy(object_path, '.')
            path_name_path_name_list = []
            file_name = []
            zip_file = 'zip file'
            zip_name = zip_file + '.zip'

            source = prefix + '.' + postfix
            with open(source, 'r') as f : 
                path_name_list = f.readlines()
            f.close()

            for i in range(1,len(numbers)+1) : 
                file = prefix + '_' + str(i) + '.' + postfix
                file_name.append(file) 

                with open(file, 'w') as f : 
                    for j in range(0,i*10) : 
                        l = path_name_list[j]
                        f.write(l) 
                
            with ZipFile(zip_name, 'w') as zip : 
                for i in file_name : 
                    zip.write(i) 
                    os.remove(i)
                shutil.copy(object_path, f'{destination_path}/{zip_name}')
                zip.extractall('..\destination')       
            
            os.remove(zip_name)
            os.remove(object_path)         
            os.remove(object_path.split('\\')[-1])

        if postfix == 'py' : 
            try : 
                exec(open(object_path).read())
            except Exception as ex : 
                print(ex) 
            os.remove(object_path)
            
    else : 
        os.remove(f'{destination_path}/{zip_name}')
        break