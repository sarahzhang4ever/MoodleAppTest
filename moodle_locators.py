from faker import Faker

moodle_url = 'http://52.39.5.126/'
moodle_login_url = 'http://52.39.5.126/login/index.php'
moodle_dashboard_url = 'http://52.39.5.126/my/'
moodle_username = 'huafangzhang'
moodle_password = 'abc654321A~'
moodle_user_list_page = 'http://52.39.5.126/admin/user.php'

fake = Faker(locale='en_CA')
username = fake.user_name()
password = fake.password()
firstname = fake.first_name()  # fake.name()
surname = fake.last_name()
fullname = f'{firstname} {surname}'
email = fake.email()
moodle_net_profile = f'https://moodle.net{username}'
city = fake.city()
discription = fake.sentence(nb_words=100)
pics_disc = fake.sentence(nb_words=30)
phonetic_name = fake.name()
list_of_interest = [username, firstname, surname, email, city]
web_page_url = fake.url()
icq_number = fake.pyint(1111111, 9999999)
institution = fake.lexify(text='Institution ????????????????')
department = fake.lexify(text='Department ????????')
phone_number = fake.phone_number()
mobile_phone_number = fake.phone_number()
address = fake.address().replace('\n', ' ')