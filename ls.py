from app import db_file

def ls():

  if not isfile(db_file):
    file = open(db_file, 'w')
    file.write('[]');
    file.close()

  file = open(db_file, 'r')
  data = json.loads(file.read())
  file.close

  numb = 1
  idx = 0
  max_idx = len(data)
  while numb <= 10:
    d = data[i]
    print(numb, '. ', d.filename)
    numb += 1
    idx += 1