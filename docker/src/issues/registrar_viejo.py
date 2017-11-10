

if __name__ == '__main__':
    import os
    import sys

    #dominio = os.environ['ISSUES_URL'].replace('http://','').replace('https://','')
    dominio = 'issues.econo.unlp.edu.ar'
    nombre = sys.argv[1]
    path = sys.argv[2]
    server = sys.argv[3]

    import auth_utils
    r = auth_utils.RegistrarServicio()
    r.register(name=nombre, domain=dominio, path=path, server=server)
