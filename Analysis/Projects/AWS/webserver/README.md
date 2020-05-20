### Flask Server Setup

1. aws > launch instances
2. chose first ubuntu ec2 and selected my previously created try3.pem key
3. ssh -i \~/.ssh/try3.pem ubuntu@ec2-18-232-163-78.compute-1.amazonaws.com
4. sudo apt install emacs24
5. made requirements.txt
6. curl -O https://bootstrap.pypa.io/get-pip.py
7. python3 get-pip.py --user
8. pip install -r requirements.txt
   1. had to remove importlib... standard lib?
   2. forgot flask/dill so straight pip'd 'em in then added lines into req.txt
9. scp -i \~/.ssh/try3.pem fraud.py ubuntu@ec2-18-232-163-78.compute-1.amazonaws.com:~/
   1. fraud schwarls37$ scp -i ~/.ssh/try3.pem -r webserver ubuntu@ec2-18-232-163-78.compute-1.amazonaws.com:~/fraud/
   2. did a bit of cleaning and path fixing locally (remotely) there
   3. scp -i \~/.ssh/try3.pem custom_pipeline.py ubuntu@ec2-18-232-163-78.compute-1.amazonaws.com:~/fraud/
10. remotely: `export FLASK_APP=fraud.py`
11. remotely: `export PYTHONPATH=$PYTHONPATH'/home/ubuntu/fraud:'` (where I put custom_pipeline.py)
12. remotely: sudo apt install apache2 *DEPRECIATED:UNNECESSARY*
13. remotely: sudo service apache2 restart *DEPRECIATED:UNNECESSARY*
14. remotely: sudo apt-get install libapache2-mod-wsgi *DEPRECIATED:UNNECESSARY*
15. I did not initially make the security groups correctly.
    1. create a security group with
       - 5000(Port)
       - tcp(Protocol)
       - 0.0.0.0/0, ::/0(Source)
    2. ec2 dashboard > select instance > actions > networking
       - add the security group above (but don't remove the original -- it gives ssh/scp)
16. required pip install pyopenssl (and also now added to req.txt)
17. remotely: `nohup flask run --host=0.0.0.0 --cert=adhoc &` (in /home/ubuntu/fraud)
18. remotely: to kill the above: `lsof -i :5000` and then `kill -9 <PID>`
19. `ssh-keygen -t rsa` and copy-pasted into github > settings > SSH and GPG keys > New SSH Key
20. added repo: github.com:pointOfive/anralk_200313