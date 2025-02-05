from ollama import chat


response = chat(model='deepseek-r1:1.5b', messages=[
  {
    'role': 'user',
    'content': 'bonjour sais tu coder en js ?',
  },
])
print(response.message.content)
