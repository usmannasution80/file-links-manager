from _ import _
from insert import insert

def main():
  title = _('title')
  sep_len = len(title)
  print(
    ('=' * sep_len),
    title,
    ('=' * sep_len),
    _('numb_list', {'numb' : 1}),
    _('numb_insert', {'numb' : 2}),
    _('numb_exit', {'numb' : 3}),
    ('=' * sep_len),
    'Your choice : ',
    sep = '\n'
  )

main();