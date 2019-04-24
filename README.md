# UG Final Year Project - Mentors for All

HOW TO RUN THE PROJECT:

1. Install Miniconda:

You can install miniconda on Unix by following the tutorial: http://deeplearning.lipingyang.org/2018/12/24/install-miniconda-on-mac/

2. Navitage to the UGFinalProject folder in Terminal

3. Create and start conda environment by typing the following in Terminal:
```
conda create --name 150260848_UG_Final_Project python=3.7.1 django=2.1
conda activate 150260848_UG_Final_Project
```
4. Install aditional django packages by typing the following in Terminal:
```
pip install django-extensions
```
5. Navigate to the application folder in Terminal:
```
cd find-a-mentor
```
6. Configure script permission and execute the script "resetdb.sh" by typing the following in Terminal:
```
chmod +x resetdb.sh
./resetdb.sh
```
This script will load test data and perform the database migrations.

7. Run the development server by typing the following in Terminal:
```
python manage.py runserver
```

The website is now ready for viewing at http://127.0.0.1:8000 !

You can use usernames starting from test1 up to test10 all with the password: "test" to log onto the website.