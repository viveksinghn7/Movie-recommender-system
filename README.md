# Movie Recommender System

This is a simple movie recommender system built using Python, Streamlit, and The Movie Database (TMDB) API. The system recommends 5 movies based on the similarity of the selected movie to other movies in the database.

## Installation

1. Clone the repository or download the code.
2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```
3. Install the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```
4. Create a `.env` file in the project directory and add your API key:
    ```plaintext
    API_KEY=your_api_key_here
    ```
5. Ensure you have the `movie_list.pkl` and `similarity.pkl` files in the `models` directory.

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2. Open your web browser and go to `http://localhost:8501`.
3. Select a movie from the dropdown menu.
4. Click on the "Show Recommendations" button to see the recommended movies and their posters.

## Explanation

- **Poster Fetching**: Fetches the movie poster from TMDb using the movie ID.
- **Recommendation**: Recommends movies based on the similarity to the selected movie.
- **Streamlit UI**: Provides a user interface to select a movie and display the recommended movies and their posters.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
