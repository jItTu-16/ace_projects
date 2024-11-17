import requests


def github_user_finder(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    user_data = response.json()
    print(user_data)

    if response.status_code == 200:
        return {
            "username": user_data.get("login"),
            "public_repos": user_data.get("public_repos"),
            "followers": user_data.get("followers"),
            "following": user_data.get("following"),
            "html_url": user_data.get("html_url"),
            "avatar_url": user_data.get("avatar_url"),
        }

    elif response.status_code == 404:
        return {"error": "User not found"}


username = input("Enter username: ")
user_info = github_user_finder(username)

if "error" in user_info:
    print(user_info["error"])
else:
    print("Username: ", user_info["username"])
    print("No. of Public Repos: ", user_info["public_repos"])
    print("Followers: ", user_info["followers"])
    print("Folloeing: ", user_info["following"])
    print("Profile URL: ", user_info["html_url"])
    print("Avatar URL: ", user_info["avatar_url"])
