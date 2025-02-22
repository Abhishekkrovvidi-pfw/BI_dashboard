# Full Stack BI Developer Screening Task

## Project Description

### Problem Statement
This project demonstrates a data pipeline and BI dashboard that integrates data from a public API, processes it, and visualizes it in an interactive dashboard. The goal is to provide insights into global weather data, including temperature trends, humidity levels, and weather conditions across various cities.

### Technologies Used
- **Backend**:
  - **Python**: For data ingestion and ETL processing.
  - **Pandas**: For data manipulation and transformation.
  - **Requests**: For API calls.
  - **SQLite**: For storing processed data.
  - **Flask**: For serving the data to the frontend.
- **Frontend**:
  - **React**: For building the interactive dashboard.
  - **Chart.js**: For data visualization.
- **Version Control & CI/CD**:
  - **GitHub**: For version control.
  - **CircleCI**: For continuous integration and deployment.

### Challenges and Solutions
- **Data Inconsistency**: Ensuring data consistency and handling missing or incorrect data from the API. Solved by implementing data validation and cleansing steps during ETL processing.
- **Real-time Data Updates**: Ensuring the dashboard reflects real-time data. Solved by setting up periodic data fetch and update mechanisms.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Node.js and npm
- SQLite

### Backend Setup
1. Create a virtual environment and activate it:
    ```bash
    cd weather-dashboard/backend
    python -m venv venv
    source venv/bin/activate
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask server:
    ```bash
    flask run
    ```

### Frontend Setup
1. Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Start the React development server:
    ```bash
    npm start
    ```

### Running the Project
- The Flask server will be running at `http://localhost:5000`.
- The React development server will be running at `http://localhost:3000`.

### CI/CD Setup
- The project includes a `.circleci/config.yml` file for CircleCI configuration. Ensure you have CircleCI set up and connected to your GitHub repository.
