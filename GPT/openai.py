
import openai

openai.api_key = "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"

def ask_gpt(prompt, temperature=0.7):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message["content"]

import Streamligt as st

user_prompt = st.text_input("What would you like to ask GPT?")
if st.button("Ask"):
    response = ask_gpt(user_prompt)
    st.write(response)
