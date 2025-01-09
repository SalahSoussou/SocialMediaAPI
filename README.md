# SocialMediaAPI

## Project Overview
The SocialMediaAPI project is focused on creating a robust and scalable API for a social media platform. This API will handle various functionalities such as user authentication, posting updates, following users, and interacting with posts.

## Features
- **User Authentication**: Secure user registration and login.
- **User Profiles**: Manage user profile information.
- **Posts**: Create, read, update, and delete posts.
- **Follow System**: Follow and unfollow other users.
- **Likes and Comments**: Interact with posts through likes and comments.
- **Feed**: View a feed of posts from followed users.

## API Endpoints and Routes

Here are the main API endpoints and their corresponding views:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Home
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
]
```


## Technologies Used
- **Backend**: Django
- **Database**: db.sqlite


## Getting Started
### Prerequisites
- Python


### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/SalahSoussou/SocialMediaAPI.git
    ```
2. Install dependencies:
    ```bash
    cd SocialMediaAPI
    pip install -r requirements.txt
    ```
3. Set up environment variables:
    - Create a `.env` file in the root directory.

### Running the Application
Run the application:
    ```bash
    python manage.py runserver
    ```



## Contributing
Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.


