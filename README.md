# Employee Register CRUD Application

This Django-based Employee Register application implements CRUD (Create, Read, Update, Delete) operations for efficient employee record management.

## Features

- Create new employee records
- Read and display a list of all employees
- Update existing employee information
- Delete employee records

## Technologies Used

- Django 5.1
- PostgreSQL
- Bootstrap 5
- Font Awesome 6
- Crispy Forms with Bootstrap 4 template pack

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/employee-register-crud.git
   cd employee-register-crud
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your environment variables:
   ```
   SECRET_KEY=your_secret_key
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=your_database_host
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8000/employee/list/`

## Usage

- To add a new employee: Click the "Add New" button on the employee list page.
- To view all employees: Navigate to the main employee list page.
- To edit an employee: Click the "Edit" button next to the employee's record.
- To delete an employee: Click the "Delete" button next to the employee's record.

## Project Structure

- `employee_project/`: Main project directory
- `employee_register/`: App directory containing models, views, and forms
- `templates/`: HTML templates for the application