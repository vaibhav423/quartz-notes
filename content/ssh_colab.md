# run everytime you start a new colab session  
!pip install colab_ssh --upgrade

from colab_ssh import launch_ssh_cloudflared, init_git_cloudflared
launch_ssh_cloudflared(password="123456")

# Optional: if you want to clone a Github or Gitlab repository
repository_url="<PUT_YOUR_REPOSITORY_URL_HERE>"
init_git_cloudflared(repository_url)

# it disconnets quickly if idle
