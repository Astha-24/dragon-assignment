# dragon-assignment
## Steps to run the application
1. `git clone git@github.com:Astha-24/dragon-assignment.git`
2. `cd dragon-assignment`
3. `vagrant up`
4. `vagrant ssh`
5. `cd /vagrant/`
6. `python -m venv ~/env`
7. `source ~/env/bin/activate`
8. `pip install -r requirements.txt`
9. `python manage.py migrate`
10. `python manage.py runserver 0.0.0.0::8000`<br>
[Download vagrant from here](https://www.vagrantup.com/downloads.html)