# Event-Management-System

## Overview

The **Event Management System** is a web-based application designed to simplify the creation, management, and participation in events. Users can register, log in, and manage their events with a user-friendly interface. Organizers can create and edit event details, upload images, and manage participants, while attendees can view event details and register for events.

## Features

- **User Authentication:** Secure login and registration for users.
- **Event Creation:** Users can create events, specifying details like name, date, location, and description.
- **Event Management:** Edit and delete events, upload images, and manage event-specific details.
- **Dashboard:** A personalized dashboard for users to manage their events.
- **Image Uploads:** Support for image uploads to enhance event details.
- **Responsive Design:** The application is fully responsive, providing a seamless experience across devices.
- **Real-time Updates:** Ensure that the event data is up to date without needing to reload the page.

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (custom styling)
- **Database:** SQLite (default Django database, can be replaced with PostgreSQL or MySQL)
- **Media Storage:** Django's default file storage for images
- **Version Control:** Git

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/event-management-system.git
   cd event-management-system
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your web browser and navigate to `http://localhost:8000/`.

## Usage

1. **Register or Log In:** Create a new account or log in with your existing credentials.
2. **Dashboard:** Access your dashboard to view and manage your events.
3. **Create Events:** Use the "Add Event" button to create new events.
4. **Manage Events:** Edit or delete your events as needed.
5. **View Events:** Browse events, view event details, and manage attendees.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to reach out at deolankaratharva@gmail.com
