## 🎯 Overview

This project is a personal blog application that allows users to view, create, edit, and delete articles.

## Getting Started

### Installation

1. Clone the repository in the current working directore:
  
    ```bash
    git clone https://github.com/T1mC0de/personal_blog.git
    cd personal_blog
    ```

2. Install dependencies:
  
    ```bash
    pip install -r requirements.txt
    ```

3. Start the development server:
  
    ```bash
    python3 main.py
    ```
    or
    ```bash
    python main.py
    ```

## 📚 API
  
   This section documents the main routes of the application. Each route is described with its parameters.

### `GET /` or  `GET /home`
  
    Displays the home page with a list of articles.

### `GET /article`
  
    Displays the creating page.


### `GET /article/<int:id>`
  
    Displays the article by id.

### `POST /submit_article`
  
    Submits article on the server.

### `GET /delete_article/<int:id>`
  
    Deletes article by id.

### `GET /edit_article/<int:id>`
  
    Displays the editing page.

### `POST /save/<string:article_title>`
  
    Saves changes on the server.

## Inspired by
inspired by https://roadmap.sh/projects/personal-blog