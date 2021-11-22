#cloud-boothook
#!/bin/bash
yum update -y
yum install -y httpd.x86_64
systemctl start httpd.service
systemctl enable httpd.service
wget https://cloud-1901183.s3.amazonaws.com/index.html
sudo cp index.html /var/www/html/index.html