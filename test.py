from git import Repo
import os
import tarfile

repo = Repo(".")
file="tmp.tar"
with open(file, "w") as tar: repo.archive(tar, prefix="o1/", path="config/") 
with tarfile.open(file, mode="r|") as tar: tar.extractall()
os.remove(file)

#repo.archive(
