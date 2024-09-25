- Initialize virtual environment
    python m venv venv
- Activation de l'environment
    source venv/bin/activate
    venv\Scripts\activate
- Install dependancies 
    pip install fastapi uvicorn
- create project directory structrure
- configure database relation :
    Database : MySQL
    Install all dependencies : 
        pip install sqlalchemy
        pip install aiomysql
        pip install alembic (for migrations)
    Install python-dotenv : pip install python-dotenv
    Configure migrations : 
        Execute commande ligne :alembic init alembic
        Run migrations : alembic revision --autogenerate -m "create users table"
        Applicate migrations : alembic upgrade head
- Create controllers and router to add users :
    - create schema validation : domains/schema/user.py
    - install passlib[bcrypt] to crypt the password : pip install passlib[bcrypt]
    - create function to save user : services/user.service.py
    - create controller to create a user : controllers/user_controller.py
- Create controller and router to login and logout:
    - install python-jose to generate connexion token: pip install python-jose
    - manage access token : librairies/manageAccessToken.py
    
    

        
