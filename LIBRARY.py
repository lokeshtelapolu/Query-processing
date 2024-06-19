import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read CSV file and generate visualizations
def visualize_book_data(csv_file):
    try:
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv(Art Garfunkel Library.csv)
        
        # Print all column names to verify structure
        print("Column Names:", df.columns)
        
        # Assuming 'Favorite' column indicates user preference (1 for favorite, 0 for not favorite)
        # You may adjust this based on your actual data structure
        
        # Basic statistics
        num_books = len(df)  # Total number of books read
        num_favorites = df['Favorite'].sum()  # Number of favorite books
        
        # Print basic statistics
        print(f"Total Number of Books Read: {num_books}")
        print(f"Number of Favorite Books: {num_favorites}")
        
        # Plotting
        plt.figure(figsize=(12, 6))
        
        # Count plot for authors
        plt.subplot(1, 2, 1)
        sns.countplot(y='Author', data=df, order=df['Author'].value_counts().index[:10])
        plt.title('Top 10 Authors Read')
        plt.xlabel('Number of Books')
        plt.ylabel('Author')
        
        # Histogram for year published
        plt.subplot(1, 2, 2)
        sns.histplot(df['Year Published'], bins=20, kde=True)
        plt.title('Distribution of Year Published')
        plt.xlabel('Year Published')
        plt.ylabel('Frequency')
        
        # Display plots
        plt.tight_layout()
        plt.show()
    
    except FileNotFoundError:
        print(f"Error: File not found at path: {csv_file}")

# Example usage
if __name__ == "__main__":
    # Replace 'path_to_your_file.csv' with the actual path to your CSV file
    csv_file_path = r"C:\Users\mslok\OneDrive\Documents\query capestone.csv"
    visualize_book_data(csv_file_path)
