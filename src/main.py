from pybooru import Danbooru
import subprocess
import os

client = Danbooru('danbooru')

post_limit = 50

path = (os.path.expanduser('~')+"/Danload/images/")
if not os.path.exists(path):
    os.makedirs(path)
dirname = os.path.dirname(path)

post_list = []

def download():
  subprocess.call("wget {0}".format(" ".join(post_list))+" -P"+dirname)

def actions():
  action = input("mpv"+"\t\t"+"(m)"+"\n"+"download"+"\t"+"(d)"+"\n"+"Option: ")
  match action:
    case "m":
      mpv_view()
    case "d": 
      print("downloading")
      download()
    case _:
      print("invalid input, try again")
      actions()

def mpv_view():
  subprocess.call("mpv {0}".format(" ".join(post_list)))

def tag_search(search_tags):
  posts = client.post_list(limit=post_limit,tags=search_tags)
  for post in posts:
    print(post['id'])
    print(post['tag_string_artist'])
    print(post['file_url'])
    post_list.append(post['file_url'])
  actions()

tag_search(input("Search Tags: "))