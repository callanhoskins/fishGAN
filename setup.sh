
curl -O https://bootstrap.pypa.io/get-pip.py
sudo apt-get install python3-distutils
python3 get-pip.py
pip3 install stylegan2_pytorch
export PATH=$PATH:/home/ubuntu/.local/bin
aws s3 sync s3://fish-gan-pics ~/data
cd data
tar -xf ../train.tar.gz
