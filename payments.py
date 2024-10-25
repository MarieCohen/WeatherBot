"""import os
import uuid
import yookassa
from yookassa import Payment

SHOP_ID = os.environ['SHOP_ID']
SHOPARTICLE_ID = os.environ['SHOPARTICLE_ID']
amount = os.environ['PRICE']

yookassa.Configuration.account_id = SHOP_ID
yookassa.Configuration.secret_key = SHOPARTICLE_ID


def create(amount, chat_id):
    id_key = str(uuid.uuid4())
    payment = Payment.create(
        {
            'amount':
            {
                'value': amount,
                'currency': 'RUB'
            },
            'payment_method_data':
            {
                'type': 'bank_card'
            },
            'confirmation':
            {
                'type': 'redirect',
                'return_url': 'https://t.me/SoulnearBot'
            },
            'capture': True,
            'metadata':
            {
                'chat_id': chat_id
            },
            'description': "Месячная подписка на SoulnearBot"
            }, id_key)
    return payment.confirmation.confirmation_url, payment.id

def check(payment_id):
    payment = yookassa.Payment.find_one(payment_id)
    if payment.status == 'succeeded':
        return payment.metadata
    else:
        return False
    """
