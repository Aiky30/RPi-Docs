# Git setup

## Setup your identity
```
git config --global user.name "Rave Davis"
git config --global user.email RaveDavis@example.com
```

## Check your config
```
git config --list
```

## Create an RSA key
```
ssh-keygen -t rsa -b 4096 -C "RaveDavis@example.com"
```

Copy the contents of the public key
```
vi /home/pi/.ssh/id_rsa.pub
```

Register the key with your git repository config, for github this is: https://github.com/settings/keys

Tell the ssh agent to use the key
```
ssh-add /home/pi/.ssh/id_rsa
```