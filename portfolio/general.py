import os

def create_dir(directory):
    
    if not os.path.exists(directory):
        
        os.makedirs(directory)
        
def write_file(path, date):
    
   f = open(path,'w')
   f.write(data)
   f.close()
   
   