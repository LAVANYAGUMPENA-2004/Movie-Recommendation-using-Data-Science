# Data-Science-Project-1-Movie-Recommendation


### Libraries & Data Loading
The script uses libraries like numpy, pandas, and sklearn to manipulate data and perform machine learning tasks.
A CSV file containing movie data (such as genres, keywords, tagline, cast, and director) is loaded into a pandas DataFrame (movies_data).

### Data Preprocessing:
Missing values in selected features (genres, keywords, etc.) are filled with empty strings to avoid errors.
A new column, combined_features, is created by concatenating these features into a single string for each movie, which helps in comparing movies based on content.

### Text to Numeric Conversion:
The script uses TfidfVectorizer to convert the text data in the combined_features column into numerical values, making it possible to calculate the similarity between movies.

### Cosine Similarity:
The cosine_similarity function calculates how similar each movie is to the others based on their feature vectors.

### User Input & Movie Search:
The user is prompted to enter their favorite movie. The script finds the closest matching movie from the dataset.
It retrieves the index of the selected movie and calculates similarity scores with other movies.

### Recommendation:
The script sorts the movies by similarity and prints out the top 30 most similar movies as suggestions for the user.
