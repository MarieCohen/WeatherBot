import os
from openai import OpenAI

from states import get_prompt
from config import OPENAI_API_KEY

OPENAI_API_KEY = OPENAI_API_KEY


chat_style = {}
context = {}

client = OpenAI(
    api_key = "OPENAI_API_KEY"
)

async def generate_text(prompt) -> dict:
    """
    connect = sqlite3.connect('gpt_us.db') # Подключаемся к бд, чтобы достать последние два ответа бота. Они будут нужны для чат 
    cursor = connect.cursor()
    sql_query = f"SELECT con, con2 FROM ChatGPT WHERE id = '{id}'"
    """

    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role": "user", "content": f"{prompt}"
            }
        #{"role": "user", "content": f"{con} {con2}"} #Здесь можно передать контекст чата
        ],
        temperature = 0.5)
    response = completion.choices[0].message
    return response.content
