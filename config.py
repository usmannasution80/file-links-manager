def config(key, value = None):

  config_file = 'config.json'

  if not isfile(config_file):
    file = open(config_file, 'w')
    file.write('{}')
    file.close()

  file = open(config_file, 'r')
  configs = json.loads(file.read())
  file.close();

  if value == None:
    try:
      return configs[key]
    except:
      return ''
  else:
    configs[key] = value
    json_str = json.dumps(configs);
    file = open(config_file, 'w')
    file.write(json_str)
    file.close()