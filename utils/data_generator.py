from faker import Faker

fake = Faker()
def random_user():
    return {
        'name': fake.first_name(),
        'email': fake.email(),
        'first_name': fake.first_name(),
        'password': fake.password(length=10),
        'last_name': fake.last_name(),
        'address': fake.address(),
        'city': fake.city(),
        'state': fake.state(),
        'zipcode': fake.postcode(),
        'mobile': fake.phone_number(),
        'number': fake.credit_card_number(card_type=None),  # 4556429684793109
        'month': fake.day_of_month(),  #10/25
        'year': fake.year(),
        'security_code': fake.credit_card_security_code() #123
    }

