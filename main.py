import os
from git import Repo
import requests


def load_repos():
    res = requests.request(method="get", url="https://script.google.com/macros/s/AKfycbxYy20mY-fP-aKSpJVLB6mnmowGZU3HcnW51ViVv3M9eo3_FhJmnSM6I36Nx0lDxIVD/exec")
    json = res.json()
    return json["values"]

def clone_repo(repo_url, destination):
    destination_dir = os.path.join(destination, repo_url.split('/')[-1].replace('.git', ''))
    Repo.clone_from(repo_url, destination_dir)



def main():
    destination_directory = "destination"
    repo_urls = load_repos()

    for url in repo_urls:
        clone_repo(url, destination_directory)
        break


if __name__ == "__main__":
    main()