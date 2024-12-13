message = 'Hello world'

for word in message.split(' '):
    print(word)

search_word = 'o'

for i in range(len(message)):
    if message[i:i + len(search_word)] == search_word:
        print('!!!!')
