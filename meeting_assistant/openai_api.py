import openai

from operational import calculate_cost, get_tokens_number

CONTEXT_WINDOW_GPT3_5_TURBO = 4097
GPT3_5_TURBO = "gpt-3.5-turbo"

openai.api_key = "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"

def send_message(message, system_message):

    user_tokens = get_tokens_number(message)
    print("User message tokens: " + str(user_tokens))
    system_message_tokens = get_tokens_number(system_message)
    print("System message tokens: " + str(system_message_tokens))
    total_prompt_tokens= user_tokens + system_message_tokens
    calculate_cost(total_prompt_tokens)

    if total_prompt_tokens > CONTEXT_WINDOW_GPT3_5_TURBO:
        #TODO: dividir el mensaje en partes
        print("La transcripción es muy larga, por favor cortala en partes.")
        return
    
    messages = [
        {
            "role": "system",
            "content": system_message
        },
        {
            "role": "user",
            "content": message
        }
    ]

    response = openai.ChatCompletion.create(
        model=GPT3_5_TURBO, 
        messages=messages,
        temperature=0,)
    return response['choices'][0]['message']['content']