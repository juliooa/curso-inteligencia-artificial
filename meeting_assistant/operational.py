import tiktoken

COST_GPT3_5_TURBO = 0.0015
TOKENS_ENCODING = 'cl100k_base'

def calculate_cost(tokens):
    print("Tokens: " + str(tokens))
    print("Cost: $" + str(tokens * COST_GPT3_5_TURBO/1000))

def get_tokens_number(text):
    encoding = tiktoken.get_encoding(TOKENS_ENCODING)
    tokens_list = encoding.encode(text)
    return len(tokens_list)