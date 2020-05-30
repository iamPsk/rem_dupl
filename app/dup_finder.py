import os, filecmp

def find_duplicate(path: str):
  no_of_files = 0
  no_of_duplicates = 0
  no_of_folders = 0
  no_of_entrys = 0

  def compare(entry, path, iterate=True):
    with os.scandir(os.path.abspath(path)) as _dir:

      if iterate:
        for cur_entry in _dir:
          if entry.inode() ==  cur_entry.inode():
            break
        
        for cur_entry in _dir:
          if cur_entry.is_dir():
            return compare(entry, cur_entry.path, False)

          if cur_entry.is_file():
            return filecmp.cmp(entry, cur_entry)

    return False
    
  with os.scandir(os.path.abspath(path)) as folders:

    for entry in folders:
      
      no_of_entrys  += 1

      if entry.is_dir():
        # print(f'Current directory: {entry.path}')
        no_of_folders += 1
        res = find_duplicate(entry.path)
        no_of_folders += res['no_of_folders']
        no_of_files += res['no_of_files']
        no_of_duplicates += res['no_of_duplicates']
   
      
      if entry.is_file():
        no_of_files += 1

        if compare(entry, path):
          no_of_duplicates += 1
          print(entry)
          os.remove(entry)


  return {
    'no_of_entrys': no_of_entrys,
    'no_of_files': no_of_files,
    'no_of_folders': no_of_folders,
    'no_of_duplicates': no_of_duplicates
  }


if __name__ == "__main__":
    val = find_duplicate(r'E:/Anitoons')
    print(val)
