import json

def _(key, values = {}):
  file = open('locales/en.json', 'r')
  data = json.loads(file.read())
  file.close()
  try:
    value = data[key]
    for key in values:
      value = value.replace(':' + key, str(values[key]))
    return value
  except:
    return '';