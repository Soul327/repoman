# clone - Gets a new repo and adds it to our list
# update - Updates all repos

import sys
import os
import subprocess

def cloneRepo(url, accessToken, path = "repos"):
	index = url.index("github.com")
	fullURL = url[:index] + accessToken + "@" + url[index:]
	print(fullURL)

	result = subprocess.run(
		['git', 'clone', fullURL],
		cwd = path,
		capture_output = True,
		text = True
	)
	print(result.stdout)


def updateRepo(path):
	result = subprocess.run(
		['git', 'pull', 'origin', 'main'],
		cwd = path,
		capture_output = True,
		text = True
	)
	print(result.stdout)


def status():
	"""
	Prints the status of the program
	"""
	print("Script name:", sys.argv[0], "\nArguments:", sys.argv[1:])
	print("Github Personal Access Token:", accessToken)
	print()


def func_clone():
	if len(sys.argv) != 3:
		print("Error")
	cloneRepo(
		url = sys.argv[2],
		accessToken = accessToken
	)

def func_update():
	pass

def showHelp():
	print("Arguments are required")

repoPath = ""
accessToken = None
secrets = os.environ.get('ATTI-SECRETS')

os.makedirs("repos", exist_ok=True)
os.makedirs("secrets", exist_ok=True)

# Load access token
with open("secrets/github-personal-access-token.txt", "r") as file:
	accessToken = file.read()

if len(sys.argv) <= 1:
	showHelp()
	exit(0)

match sys.argv[1]:
	case "clone": func_clone()
	case "update":
		if len(sys.argv) == 2:
			# Update all
			print("Updating all repos")

			for name in os.listdir("repos"):
				repoPath = os.path.join(f"repos/{name}")
				print(repoPath)
				updateRepo(repoPath)
		else:
			# Update individual
			pass