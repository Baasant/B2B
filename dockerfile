# # Use Python as base image
# FROM python:3.9  

# # Set working directory inside the container
# WORKDIR /app  

# # Copy only needed files
# COPY . .  


# # Install dependencies
# RUN pip install --upgrade pip

# RUN pip install -r requirements.txt  

# # Run the app
# CMD ["streamlit", "run", "app_main.py", "--server.port=8501", "--server.address=0.0.0.0"]

# # CMD ["python", "app_main.py"]

# Use Python as base image

FROM python:3.9  

# Set working directory inside the container
WORKDIR /app  

# Copy only the requirements file first (to leverage Docker caching)
COPY requirements.txt /app/

# Install dependencies before copying the rest of the code
RUN pip install --no-cache-dir -r requirements.txt  

# Now copy the rest of the application
COPY . /app/

# Expose Streamlit's default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app_main.py", "--server.port=8501", "--server.address=0.0.0.0"]
