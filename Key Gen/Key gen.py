import random,pyperclip,time
while True:
 def generate_random_windows_key(length):
     characters = 'BCDFGHJKMNPQRTVWXY23456789'
     key = ''.join(random.choice(characters) for _ in range(length))
     key_with_hyphens = '-'.join([key[i:i+5] for i in range(0, length, 5)])
     return key_with_hyphens

 random_key = generate_random_windows_key(25)
 print(random_key)
 pyperclip.copy(random_key)
 time.sleep(5)
