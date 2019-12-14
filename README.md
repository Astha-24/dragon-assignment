# dragon-assignment
## Installation
1. Vagrant <br>
[Download vagrant from here](https://www.vagrantup.com/downloads.html)
## Steps To Run The Application
1. `git clone git@github.com:Astha-24/dragon-assignment.git`
2. `cd dragon-assignment`
3. `vagrant up` *First Time Only*
4. `vagrant ssh`
5. `cd /vagrant/`
6. `python -m venv ~/env` *First Time Only*
7. `source ~/env/bin/activate`
8. `pip install -r requirements.txt` *First Time Only*
9. `python manage.py migrate` *First Time Only*
10. `python manage.py runserver 0.0.0.0:8000`
---
**NOTE** <br>
In case you are facing problem running `vagrant up` change the port number to an available port
by changing it in the `Vagrantfile`.

`config.vm.network "forwarded_port", guest: 8000, host: <your available port>`

---
## ENDPOINTS
[**LINK TO POSTMAN COLLECTION**](https://www.getpostman.com/collections/81107b6e00d970a1e80f)
- (GET)`/dragon_api/rules/` : Displays all the rules
- (POST)`/dragon_api/rules/`: Create new rules 
    <br>
    INPUT_FIELDS:<br> 
    `time_period` : Time (in hours) <br>
    `max_animals_to_kill`: No of animals allowed to kill
    <br>
    OUTPUT: <br> ```{
    "message": "The Rule is sucessfully created",
    "rule_id": 3,
    "status": 201
    }```  
- (DELETE)`/dragon_api/delete-rule/3/`: Delete rule by rule_id
    <br> OUTPUT: <br>
    ```{
        "message": "The Rule with 3 succesfully deleted",
     "status": 200}```

- (GET)`/dragon_api/dragons/`: Displays all the dragons
- (POST)`/dragon_api/dragons/`: Register a Dragon <br>
   INPUT FIELDS:<br> `dragon_name`
   <br>
   OUTPUT: <br>
   `{"message": "The Dragon is sucessfully registered", "dragon_id": 2, "status": 201}`
  
- (POST)`/dragon_api/kill_by_dragon/`: Determines whether the dragon can kill or not
    <br> INPUT FIELDS: <br>
`dragon`: Dragon ID <br>
`kill_time`: **timestamp** for the Request <br>
`animals_killed`: **noOfAnimal** requested to kill
    <br>
    OUTPUT: <br>
    ``{
        "did kill": true
    }``

---
