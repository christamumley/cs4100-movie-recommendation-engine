def main():
    # TODO: Add your code here
    
    # Example: Print a welcome message
    print("Welcome to the Movie Recommendation System!")
    
    # Example: Get user input
    user_input = input("Please type a description of a movie you'd like to watch: ")
    
    # Example: Process user input
    if user_input:
        #just an example for now
        processed_text = text_processor(user_input)
        key_words = key_word_extracter(processed_text)
        present_genres = genre_identifier(key_words)
        present_tropes = trope_identifier(key_words)
        ratings = rating_tester(key_words)

        features = [present_genres, present_tropes, ratings]

        movie_rec = movie_recommender(features)

        print(f"Here is a movie we think you'd like, {movie_rec}!")
    else:
        print("Hello, anonymous!")
    
    # TODO: Add more code here
    
if __name__ == "__main__":
    main()