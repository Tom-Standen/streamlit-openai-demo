# Streamlit-OpenAI-Demo
A repository for querying the OpenAI API using Streamlit.

## Setup Instructions

### Clone the Repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/Tom-Standen/streamlit-openai-demo.git
cd streamlit-openai-demo
```

### Install Requirements

Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

This will install all the packages listed in `requirements.txt` including Streamlit and any other dependencies.

### Add OpenAI API Key

1. Navigate to the `.streamlit` directory within your project folder. Create it if it doesn't exist.
    ```bash
    cd .streamlit
    ```

2. Create a file named `secrets.toml` in the `.streamlit` directory.

    ```bash
    touch secrets.toml
    ```

3. Open `secrets.toml` and add your OpenAI API key:

    ```toml
    [openai]
    key = "YOUR_API_KEY_HERE"
    ```

    Replace `YOUR_API_KEY_HERE` with your actual OpenAI API key.

### Update `.gitignore`

To make sure you don't accidentally commit sensitive information, add `.streamlit/secrets.toml` to your `.gitignore` file. Open `.gitignore` and add the following line:

```
.streamlit/secrets.toml
```

## Run Streamlit App

After completing the setup, navigate back to the root directory of the project and run:

```bash
streamlit run app.py
```

Your Streamlit app should now be running and connected to the OpenAI API.
