"""Examples of making HTTP API requests with the requests package."""

import requests


TIMEOUT_SECONDS = 10


# Make a GET request and decode its JSON response.
def get_github_user(username):
    response = requests.get(
        f"https://api.github.com/users/{username}",
        timeout=TIMEOUT_SECONDS,
    )
    response.raise_for_status()
    return response.json()


# Pass query-string arguments with params.
def get_github_repositories(username):
    response = requests.get(
        f"https://api.github.com/users/{username}/repos",
        params={"type": "owner"},
        timeout=TIMEOUT_SECONDS,
    )
    response.raise_for_status()
    return response.json()


# Pass a JSON request body with json.
# This example is not called below because creating a server changes real resources.
def create_openstack_server(compute_endpoint, auth_token):
    response = requests.post(
        f"{compute_endpoint.rstrip('/')}/servers",
        headers={"X-Auth-Token": auth_token},
        json={
            "server": {
                "name": "test-server",
                "imageRef": "12345",
                "flavorRef": "1",
            }
        },
        timeout=TIMEOUT_SECONDS,
    )
    response.raise_for_status()
    return response.json()


# Inspect a response status code before processing its body.
def show_github_user_status(username):
    response = requests.get(
        f"https://api.github.com/users/{username}",
        timeout=TIMEOUT_SECONDS,
    )

    if response.status_code == 200:
        print("Success!")
    elif response.status_code == 404:
        print("Not Found!")
    else:
        response.raise_for_status()


def main():
    try:
        print(get_github_user("octocat"))
        print(get_github_repositories("octocat"))
        show_github_user_status("octocat")
    except requests.RequestException as error:
        print(f"API request failed: {error}")


if __name__ == "__main__":
    main()
