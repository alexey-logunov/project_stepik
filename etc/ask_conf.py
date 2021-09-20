CONFIG = {
'mode': 'django',
'working_dir': '/home/box/web/ask',
'python': '/usr/bin/python3',
    'args': (
    '--bind=0.0.0.0:8000',
    '--workers=2',
    '--timeout=10',
    'ask.wsgi'
    )
}

# CONFIG = {
# 'mode': 'wsgi',
# 'working_dir': '/home/alexey-logunov/PycharmProjects/web/ask',
# 'python': '/usr/bin/python3',
#     'args': (
#     '--bind=0.0.0.0:8000',
#     '--workers=2',
#     '--timeout=10',
#     'wsgi:application'
#     )
# }
