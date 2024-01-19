# fake_receita.py

from datetime import datetime
from faker import Faker
from models import Receita  
def preencher_banco_dados_com_fakes(num_registros=10):
    fake = Faker()

    for _ in range(num_registros):
        Receita.objects.create(
            receita_id=fake.random_number(digits=5),
            nome_receita=fake.word(),
            data=fake.date_time_this_decade(),
            preparo=fake.text(max_nb_chars=250),
            rendimento=fake.random_int(min=1, max=10),
            categoria=fake.word()
        )

preencher_banco_dados_com_fakes()
