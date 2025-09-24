is_magician = False
is_expert = True
# check if magician AND expert: "You're a master magician!"

# check if magician BUT not an expert: "At least you're getting there."

# If you're not a magician "You need magic powers."

if is_magician and is_expert:
    print('You\'re a master magician!')
elif is_magician and not is_expert:
    print('At least you\'re getting there.')
elif not is_magician:
    print('You need magic powers!')
