from sys import argv

script, user_name = argv
prompt = '> '

print("hi %s, I am the %s script"  % (user_name, script))
print("I would like to ask you a few questions")
print("do you like me %s?" % user_name)
likes = input(prompt)
print("where do u live %s?" % user_name)
lives = input(prompt)

print("what kinda computer u have?")
computer = input(prompt)


print("""alright, so you said %r about liking me. 
you live in %r. Not sure where that is.
and you have a %r computer. nice
""" % (likes, lives, computer))

