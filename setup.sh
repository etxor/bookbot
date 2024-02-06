#!/usr/bin/bash
# TODO: test fresh installation, for now these are reference commands
echo "Updating current packages"
sudo apt update && sudo apt install -y

echo "Installing git"
sudo apt install git

echo "GitHub email: "
read GH_EMAIL
echo "GitHub username: "
read GH_USERNAME

echo "Installing gh with webi"
curl -sS https://webi.sh/gh | sh
source ~/.config/envman/PATH.env
gh auth login
git config --global user.email "$GH_EMAIL"
git config --global user.name "$GH_USERNAME"

echo "Creating workspace directories"
mkdir ~/workspace
mkdir ~/workspace/github.com
mkdir ~/workspace/github.com/$GH_USERNAME

echo "Installing Python"
sudo apt install -y build-essential zlib1g-dev libssl-dev
sudo apt install -y libreadline-dev libbz2-dev libsqlite3-dev libffi-dev

echo "Installing pyenv with webi"
curl -sS https://webi.sh/pyenv | sh
source ~/.config/envman/PATH.env
echo "Append these lines to the shell config file for pyenv"
echo \# pyenv configuration
echo export PYENV_ROOT=\"\$HOME/.pyenv\"
echo command -v pyenv \>/dev/null \|\| export PATH=\"\$PYENV_ROOT/bin:\$PATH\"
echo eval \"\$\(pyenv init \-\)\"
echo eval \"\$\(pyenv virtualenv\-init \-\)\"
echo "Press a key to continue"
read DUMP_VALUE

echo "Installing Python 3.12.1"
pyenv install -v 3.12.1
pyenv global 3.12.1
echo "python version must be 3.12.1"
python --version 
echo "Press a key to continue if the value matches"
read DUMP_VALUE
