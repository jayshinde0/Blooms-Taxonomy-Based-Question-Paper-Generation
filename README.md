# Bloom's Taxonomy Based Question Paper Generation

## Project Overview

This project aims to automate the creation of question papers by using Bloom's Taxonomy and machine learning techniques. The system helps educators generate questions across various cognitive levels, from basic recall to critical analysis, ensuring diverse and well-balanced assessments. The integration of machine learning algorithms allows for the automatic prediction of marks and categorization of questions based on cognitive complexity.

## Features

- **Bloom's Taxonomy Integration**: Generate questions based on cognitive levels (Remember, Understand, Apply, Analyze, Evaluate, Create).
- **Machine Learning Algorithms**: Uses algorithms like Linear Regression for mark prediction and Random Forest for Bloom's Taxonomy level prediction.
- **Customizable Parameters**: Allows educators to specify subject, grade level, difficulty, and topics covered.
- **Analytics**: Provides insights into student performance to help educators improve instructional strategies.

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv myenv
   myenv\Scripts\activate
   ```

2. Install the required dependencies:
   ```bash
   pip install django
   pip install opencv-python
   pip install pandas
   pip install scikit-learn==1.2.2
   pip install pickle-mixin
   ```

3. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

   - Access the project: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Admin panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Technologies Used

- **Backend**: Django (Python)
- **Machine Learning**: Scikit-learn, Pandas
- **Web Development**: HTML, CSS, JavaScript

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This version is more concise and focused on the key details of your project.
