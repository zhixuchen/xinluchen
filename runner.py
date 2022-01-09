import os

if __name__ == '__main__':
    # print(os.system('%s' % ("py manage.py runserver  0.0.0.0:8000")))

    # print(os.system('%s' % ("py manage.py startapp Staff_info")))
    print(os.system('%s' % ("py manage.py makemigrations")))
    print(os.system('%s' % ("py manage.py migrate")))
    print(os.system('%s' % ("py manage.py runserver ")))
# # print("")
