import itertools

# Function to generate valid words based on the rules
def generate_words(letters, center_letter):
    # Set to hold the valid words
    valid_words = set()

    # Loop through all possible lengths of words (from 4 to 7 letters)
    for length in range(4, 8):
        # Generate all combinations of the letters of the given length
        for word_tuple in itertools.permutations(letters, length):
            word = ''.join(word_tuple).lower()
            
            # Ensure word contains the center letter and doesn't have duplicates
            if center_letter in word and word not in valid_words:
                valid_words.add(word)
    
    return valid_words

# Function to score words based on the rules
def score_words(words, center_letter):
    scored_words = []

    for word in words:
        score = len(word)
        
        # Check if the word is a pangram (uses every letter at least once)
        if len(set(word)) == 7:  # All 7 unique letters used
            score += 7  # Add 7 extra points for a pangram

        scored_words.append((word, score))

    # Sort words by score (ascending)
    scored_words.sort(key=lambda x: x[1])

    return scored_words

# Example usage
def main():
    letters = input("Enter the 7 letters (including the center letter): ").split()
    center_letter = letters[0]  # Assume the center letter is the first in the list

    # Generate words
    valid_words = generate_words(letters, center_letter)

    # Score words and sort
    scored_words = score_words(valid_words, center_letter)

    # Print words and scores from lowest to highest
    for word, score in scored_words:
        print(f"{word.upper()} - {score} points")

# Run the main function
if __name__ == "__main__":
    main()
