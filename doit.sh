python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -e .\[test\]
pip install -r requirements.txt

# Run Tests
# docker compose up -d postgres
# export DATABASE_PORT=5432
# export DATABASE_HOST=localhost
# export DATABASE_PASSWORD=postgres
# export DATABASE_USER=postgres
# pytest 

# Run Sandbox Site
# make sandbox
# sandbox/manage.py runserver

# Generate fake data
# docker compose up -d postgres 
# Generate 10k fake books
# python utility/generate_fake_books.py 10000 sandbox/fixtures/books.generated.csv
# Takes approx 15 seconds per 1000 records to insert so 1M records is about 4 hours
# make sandbox 
# Then run the sandbox site
# sandbox/manage.py runserver