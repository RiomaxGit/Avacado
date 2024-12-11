# AVACADO

<p align="center">
    <img src="./1.png" width="400">
</p>

> A real-time django chat application

### Project Summary:

The avacado Real-Time Chat Application is a web-based platform
developed using Python, Django, and Django Channels. It enables
users to login, join chat rooms, and engage in real-time group
conversations. With a simple and intuitive interface, users can
seamlessly navigate through the application to communicate
effectively with others. Utilizing Django Channels (web sockets),
messages are delivered instantly, ensuring a smooth and
interactive chatting experience.

### Figma UI:
[UI Design](https://www.figma.com/file/W88cIOOplUPLUBbk1IpBMb/Untitled?type=design&node-id=1%3A2&mode=design&t=Bk9eVOYEbv4wnGGL-1)

### Running the project:

1. Activate the virtual environment
```bash
pipenv shell

```

2. Running the project
```bash
python manage.py runserver
```

Default Port: 8000

3. Visit the page:
localhost:8000

> Running the project in VSCode debug mode will run on PORT 9000


### Instruction on how to integrate with VSCode:
Run the command pallet:
1. Views -> Command Pallet (Shift + Ctrl + P)
2. Search for python interpreter
3. Copy the env path:
    - To get env path:
    ```bash
    pipenv --venv
    ```
4. Get the path and add /bin/python to the end <br/>
> Example: /home/vaishakh/.local/share/virtualenvs/avacado-ftA2AhBZ/bin/python
5. Open Terminal (Ctrl + `)

### Framework & Libraries used:
- <b>Language Used</b>
    - Python
- <b>Tools</b>
    - Figma - UI / UX
- <b>Framework / Libraries</b>
    - Django Framework
    - Django Channels
    - Daphne (Protocol Server for ASGI)
- <b>Database</b>
    - SQLite
- <b>Concepts</b>
    - MVC Pattern
    - ASGI (Asynchronous Server Gateway Interface)
    - WebSocket


### Planning & Implementation:
VACADO chat app will consist of the following components:
- <b>Frontend</b>
    - Users are able to login.
    - Users are able to join multiple channels / chat rooms.
    - Users are able to send and receive messages.
- <b>Backend</b>
    - Django to maintain the user authentication, handling http requests and integrating with the database.
    - User authentication is implemented using the
    - Django’s built-in user authentication system.
- <b>Database</b>
    - Using Django’s default SQLite database to store user information, and chat room information.
    - Real-Time Communication:
    - Using Django Channels to enable WebSocket communication for real-time messaging.

### References & Inspiration:
[Django Framework](https://docs.djangoproject.com/en/4.2/) <br/>
[Django Channel Documentation](https://channels.readthedocs.io/en/latest/) <br/>
[WebSocket Documentation](https://websockets.readthedocs.io/en/stable/) <br/>
[ASGI (Asynchronous server gateway interface) specification](https://github.com/django/asgiref/blob/main/specs/asgi.rst) <br/>