import subprocess
import sys


def get_github_username():
    try:
        # Run the git command to get the user's GitHub username
        username = subprocess.check_output(
            ['git', 'config', 'user.name']).decode().strip()
        return username
    except subprocess.CalledProcessError:
        # Git configuration not found or an error occurred
        return input("Enter your github username : ")


def push_to_remote(remote_name='origin', branch_name='main'):
    try:

        # Add and commit the changes
        subprocess.check_output(['git', 'add', '.'])
        subprocess.check_output(['git', 'commit', '-m', 'Update README.md'])
        # Run the 'git push' command to push changes to the remote repository
        subprocess.check_output(['git', 'push', remote_name, branch_name])
        # print(output.decode())  # Print the output for debugging
        print("You are all done! Your README.md file is up to date and pushed to the remote repository.")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing to remote: {e}")
        print("Commit the repository manually to the remote repository now. You will be all done!")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Commit the repository manually to the remote repository now. You will be all done!")
        sys.exit(1)


line_to_append = '/CopyMyReadme.py'
gitignore_path = '.gitignore'

# Check if the line is already in the .gitignore file
with open(gitignore_path, 'r') as gitignore:
    lines = gitignore.readlines()
    line_exists = any(line.strip() == line_to_append for line in lines)

# If the line doesn't exist, append it
if not line_exists:
    with open(gitignore_path, 'a') as gitignore:
        gitignore.write("\n"+line_to_append)


github_username = "nipuna-dulara"

# Prompt the user to input their social media usernames
print("Leave next fields empty to drop respective social media icon from your README.md file.")
linkedin_username = input("Enter your LinkedIn username: ")
stackoverflow_url = input("Enter your Stack Overflow url: ")
hackerrank_username = input("Enter your HackerRank username: ")
twitter_username = input("Enter your Twitter username: ")

# Open the Markdown file for reading and writing ('r+')
with open('README.md', 'r+') as profile_readme:
    # Read the content of the file
    content = profile_readme.read()

    content = content.replace(
        "https://stackoverflow.com/users/21977864/chathura-de-silva", stackoverflow_url)
    content = content.replace("apchathuradesilva", linkedin_username)
    content = content.replace("chathuradesilva", hackerrank_username)
    content = content.replace("chathuradsilva", twitter_username)
    content = content.replace("nipunadulara", github_username)
    content = content.replace("Chathura De Silva", github_username)
    profile_readme.seek(0)  # Move the file cursor to the beginning
    # Write the modified content back to the file
    profile_readme.write(content)
    profile_readme.truncate()  # Truncate the remaining content


push_to_remote()
