<h1 align="center">FAQs (With Translations)</h1>


<h2>Features Implemented</h2>

It supports following features:

- Create, retrieve, and list FAQs.
- Automatic translation of questions into other languages such has Hindi using `googletrans`.
- Caching of FAQ details to reduce database load using `Redis`.
- Uses `ckeditor` for rich text answers of questions with multilingual support.
- `Dockerfile` to containerize the applicaiton.
- `docker-compose.yaml` file for running up redis.
- Unit tests using `pytest`.




<h2 align="center">PREVIEW</h2>

<p align="center">
<img src="https://ucarecdn.com/8c9d9d14-fed1-4015-8d71-360ecfc31a18/Screenshot20250202150741.png" alt="Screenshot-2025-02-02-150741" width="49%">
<img src="https://ucarecdn.com/c8c47f0e-6891-4844-a7c2-b2ea1153df1b/Screenshot20250202151041.png" alt="Screenshot-2025-02-02-151041" width="49%">
</p>
<p align="center">
<img src="https://ucarecdn.com/49b7dd2e-fe73-4df4-8e22-b0d8f02052e5/Screenshot20250202151210.png" alt="Screenshot-2025-02-02-151210" width="49%">
<img src="https://ucarecdn.com/325105b0-f446-4480-863b-ac07ba3a8cf8/Screenshot20250202151249.png" alt="Screenshot-2025-02-02-151249" width="49%">
</p>
<p align="center">
<img src="https://ucarecdn.com/dd7e44a5-4500-46f7-8325-5a22bf39064a/Screenshot20250202151321.png" alt="Screenshot-2025-02-02-151321" width="49%">
</p>


<h2 align="center">Installation using Docker Compose</h2>

Follow these steps to set up and run FAQ Translation APIs using Docker Compose:

**Prerequisites:**

- Make sure you have Docker and Docker Compose installed on your machine. If not, you can [install them here](https://docs.docker.com/compose/install/).

**1. Clone the Repository:**

Clone the FAQ Translation repository to your local machine using the following command:

```bash
git clone https://github.com/Ratnesh2003/FAQ-System
```

**2. Navigate to the project directory:**

```bash
cd faq
```

**3. Start the Containers:**

Build and start the Docker containers using the following command:

```bash
docker-compose up --build
```

This command will pull necessary images, build all the services, and start the containers.

**5. Access the FAQ System APIs:**

Once the containers are up and running, you can access the application in your web browser using the following URL:

- **Backend:** [http://localhost:8000](http://localhost:8000)


**Default Admin Credentials:**

Use the following credentials to access the admin panel:

- **Username:** admin
- **Password:** password


<h2 align="center">Installation without Docker Compose</h2>

Follow these steps to set up and run FAQ Translation APIs without Docker Compose:

**Prerequisites:**

1. **Python:** Make sure you have Python installed on your machine. If not, you can [install it here](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/).

2. **Redis:** Make sure you have Redis installed on your machine. If not, you can [install it here](https://redis.io/download).

**Getting Started:**

**1. Clone the Repository:**

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/Ratnesh2003/FAQ-System
```

**2. Navigate to the project directory:**

```bash
cd faq
```

**3. Create and Activate a Virtual Environment:**

```bash
pip install virtualenv
virtualenv venv
venv/scripts/activate  # On Windows
source venv/bin/activate  # On Linux and macOS
```

**4. Install the Dependencies:**

```bash
pip install -r requirements.txt
```

**5. Create the Database:**

Create a PostgreSQL database and connect to it by entering credentials in .env file, once connected run the migrate command:

```bash
python manage.py migrate
```

**6. Create a Superuser:**

**You can create a superuser account executing the following commands:**

```bash
python manage.py createsuperuer
```

A prompt will appear asking for email followed by password.

**Alternatively, you can create a superuser by using the following custom command:**

```bash
python manage.py add_superuser --email <email> --password <password>
```

**7. Run the Backend Server:**

```bash
python manage.py runserver
```

**Access the endpoints in your web browaer:** [http://localhost:8000](http://localhost:8000)

**Access the Django Admin Panel, go to:** [http://localhost:8000/admin](http://localhost:8000/admin)

Use the superuser credentials to login.

These steps will get you up and running with the FAQ System on your local machine.

