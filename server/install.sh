#create virtual environment
python3 -m pip install --user virtualenv
python3 -m virtualenv venv

# Activate Virtual environement
. venv/bin/activate

# Install requirements
pip install Flask
pip install rsa
pip install pycryptodomex
pip install scikit-learn
pip install Pillow
pip install matplotlib
pip install gunicorn
