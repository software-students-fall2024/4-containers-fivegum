
# Containerized App Exercise

A containerized app that performs speech-to-text conversion using machine learning, with a web interface to display results and a database for data storage.

# Badges
![Unit Testing Workflow Status](https://github.com/software-students-fall2024/4-containers-fivegum/actions/workflows/testing.yml/badge.svg)
![Logging Workflow Status](https://github.com/software-students-fall2024/4-containers-fivegum/actions/workflows/event-logger.yml/badge.svg)
![Linting Workflow Status](https://github.com/software-students-fall2024/4-containers-fivegum/actions/workflows/lint.yml/badge.svg)

# About

The Speech-to-Text App consists of three main components:
1. **Machine Learning Client**: Processes audio data and converts speech to text.
2. **Web App**: Allows users to display processed text and record audio.
3. **Database**: A MongoDB database storing metadata and transcriptions. 

# Subsystems

## 1. Machine Learning Client

### Features:
- Captures and processes audio data.
- Performs speech-to-text conversion.
- Stores transcription results and metadata in MongoDB.

## 2. Web App

### Features:
- Allows users to upload audio files for transcription.
- Displays transcription results.
- Connects to MongoDB to fetch and store data.

## 3. Database

### Features:
- MongoDB instance running in a Docker container.
- Stores audio metadata and processed text.

### Setup:
Create a .env file with the following:
```
MONGODB_USERNAME=user
MONGODB_PASSWORD=pass
MONGODB_URI=mongodb://user:pass@mongodb:27017
SECRET=your-secret-key
```

Note that `MONGODB_URI` must be of the form `mongodb://MONGODB_USERNAME:MONGODB_PASSWORD@mongodb.27017`.

We also include an `.env.example` for your convenience.

# Installation and Usage

### Steps to Run the Application:
In our testing environment, we are using `docker compose`, as opposed to `docker-compose`. As such, the instructions will be provided with this utility. 

1. Clone the repo:
   ```
   git clone https://github.com/software-students-fall2024/4-containers-fivegum.git
   cd 4-containers-fivegum
   ```
2. Build the containers:
   ```
   docker compose build
   ```
3. Run the containers:
   ```
   docker compose up
   ```
4. Go to `localhost:8080`.

### Running Tests:
To run tests for individual subsystems, first ensure the application is runnning with `docker compose up`. 
We take this approach because the environment variables setup is made easier by using `docker-compose`, as oppoosed to requiring an `.env` for each subsystem in order to test.

Once the containers are up, you can proceed to the instructions below.

1. Testing the Machine Learning Client:
   ```
   docker compose exec machine-learning-client pytest tests/
   ```
2. Testing the Web App:
   ```
   docker compose exec web-app pytest tests/
   ```

# Group Members
- Neha Magesh: [link](https://github.com/nehamagesh)
- Luca Ignatescu: [link](https://github.com/LucaIgnatescu)
- Tahsin Tawhid: [link](https://github.com/tahsintawhid)
- James Whitten: [link](https://github.com/jwhit0)
