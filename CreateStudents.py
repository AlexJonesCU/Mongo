#using this to get a file of random students

from faker import Faker
import csv
fake = Faker()
fake.random

#majors
my_word_list = ['CPSC','COM', 'DANCE','ECON','BUS','IES','ENG','MATH','BIO','HSK']

writer = csv.writer(open('Students2.txt', 'w'))

writer.writerow(["StudentId","FirstName", "LastName", "major", "courses"])

for _ in range(50):
    writer.writerow(
        [fake.pyint(min_value=1, max_value = 9999999, step=1),
        fake.first_name(),fake.last_name(),
        fake.word(ext_word_list=my_word_list),
        (fake.word(ext_word_list=my_word_list), fake.pyint(min_value=100, max_value = 450, step=1), fake.word(ext_word_list=my_word_list), fake.pyint(min_value=100, max_value = 450, step=1))
        ]
    )
