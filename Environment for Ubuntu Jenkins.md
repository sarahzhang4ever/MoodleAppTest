# Selenium, AWS, Python, Jenkins, Git Integration

### Initial EC2 Installation on AWS
```
sudo apt-get update
sudo apt-get upgrade
```

### Install Google Chrome Binary for Linux
```
sudo apt-get install -y libappindicator1 fonts-liberation
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -f
sudo dpkg -i google-chrome*.deb
sudo apt-get install -f
google-chrome --version
```

### Install ChromeDriver Binary for Linux
```
sudo apt-get update
wget https://chromedriver.storage.googleapis.com/98.0.4758.102/chromedriver_linux64.zip
sudo apt-get install unzip
sudo apt-get update
sudo unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
chromedriver – version
```

### Install Java 11 (will be used by Jenkins)
```
sudo apt update
sudo apt search openjdk
sudo apt install openjdk-11-jdk
sudo apt install openjdk-11-jdk
java -version
```

### Install Jenkins 
```
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
  
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
  
sudo apt-get update
sudo apt-get install jenkins
cat /var/lib/jenkins/config.xml
```

### Check Jenkins status (should be green and Active)
```
sudo systemctl status jenkins
```

### If Jenkins status is Inactive
```
sudo systemctl start jenkins
sudo systemctl status jenkins
```
### Check Python3 version
```
python3 —version
```

### If Python3 is not installed
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.9
python3 --version
```

### Install pip3 package manager
```
sudo apt install python3-pip
pip3 --version 
```

### Install virtualenv using pip3
```
sudo pip3 install virtualenv 
virtualenv --version
```

### Open a Firewall for Jenkins connections (optional)
```
sudo ufw allow 8080
sudo ufw status
sudo ufw allow OpenSSH
sudo ufw enable
```

### Unlock Jenkins (copy and paste an Admin Password)
```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

### Install Git on EC2 (upgrading Git to the latest version) - (optional)
```
git --version
sudo add-apt-repository -y ppa:git-core/ppa
sudo apt-get update
sudo apt-get install git -y
```

### Open Jenkins —> go to Manage Plugins (check the availability)
```
Credentials Plugin 
Git plugin
```

### Make Jenkins & Git integration (using Terminal or CMD)
```
ssh-keygen
```

### Add Private key to the Jenkins GIT Credentials
```
cat /home/ubuntu/.ssh/id_rsa 
```

### Add Public key to the GitHub Deploy Keys
```
cat /home/ubuntu/.ssh/id_rsa.pub
```

### General Moodle Selenium Script
Setup a proper path, I call my virtualenv dir "venv", and  I've got the virtualenv command installed in /usr/local/bin
```
PATH=${PATH}:/usr/local/bin
if [ ! -d "venv" ]; then
        virtualenv venv
fi
. venv/bin/activate
pip3 install faker
pip3 install selenium
pip3 install pytest
cd /var/lib/jenkins/workspace/PythonSeleniumMoodle/
python3 -m unittest discover --pattern=moodle_tests.py
deactivate
```
