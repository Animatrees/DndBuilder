# D&D Character Builder

This is the initial iteration of the D&D Character Builder project, implemented using Django framework. At its current state, the project has a basic file structure set up and utilizes Poetry for dependency management. It also includes a few commands in the Makefile for convenience.

## Requirements

- Python 3.11+
- Django 5.0+
- Poetry

## Installation

1. **Clone the repository:**

   \```
   git clone https://github.com/Animatrees/DndBuilder.git
   \```

2. **Navigate to the project directory:**

   \```
   cd DndBuilder
   \```

3. **Install dependencies using Poetry:**

   \```
   poetry install
   \```

## Usage

- **Run the Django development server:**

  \```
  make runserver
  \```

- **Visit** `http://localhost:8000` **in your web browser to access the application.**

## Makefile Commands

- **`make runserver`:** Run the Django development server.
- **`make migrate`:** Apply all made migrations.
- **`make migrations`:** Make migrations to models.
- **`make update_db`:** Make migrations and apply them.
- **`make superuser`:** Create a superuser.


## License

This project is licensed under the [MIT License](LICENSE).
