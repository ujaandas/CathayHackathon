import pandas as pd
from surprise import Dataset, Reader, SVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Ignore warnings
pd.options.mode.chained_assignment = None  # default='warn'

# Load data
data = pd.read_csv("../Data/flight_fruits.csv")
print(data.head())

content_df = data[["ID", "Fruit", "FlightID", "Code", "Arrival Date", "Via"]]

# Join non-null values of each row
content_df["Content"] = content_df.apply(
    lambda row: " ".join(row.dropna().astype(str)), axis=1
)

# Use TF-IDF vectorizer to convert content into a matrix of TF-IDF features
tfidf_vectorizer = TfidfVectorizer()
content_matrix = tfidf_vectorizer.fit_transform(content_df["Content"])

# Compute cosine similarity matrix
content_similarity = linear_kernel(content_matrix, content_matrix)

# Create a reader object
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(data[["FlightID", "ID", "Via"]], reader)


# Use SVD to train the model
def get_content_based_recommendations(product_id, top_n):
    index = content_df[content_df["FruidID"] == product_id].index[0]
    similarity_scores = content_similarity[index]
    similar_indices = similarity_scores.argsort()[::-1][1 : top_n + 1]
    recommendations = content_df.loc[similar_indices, "ID"].values
    # Return unique recommendations
    return list(set(recommendations))


# Test the function
# print(get_content_based_recommendations("Pineapple", 5))

algo = SVD()
trainset = data.build_full_trainset()
algo.fit(trainset)


# Use SVD to train the model
def get_collaborative_filtering_recommendations(user_id, top_n):
    testset = trainset.build_anti_testset()
    testset = filter(lambda x: x[0] == user_id, testset)
    predictions = algo.test(testset)
    predictions.sort(key=lambda x: x.est, reverse=True)
    recommendations = [prediction.iid for prediction in predictions[:top_n]]
    return list(set(recommendations))


# Convert product ID to product name (only works w/ collaborative filtering)
def convert_product_id_to_name(product_id):
    return content_df[content_df["ID"] == product_id]["Fruit"].iloc[0]


# Test the function
# print(get_collaborative_filtering_recommendations("3239", 5))


# Hybrid Recommender
def get_hybrid_recommendations(user_id, product_id, top_n):
    content_based_recommendations = get_content_based_recommendations(product_id, top_n)
    collaborative_filtering_recommendations = (
        get_collaborative_filtering_recommendations(user_id, top_n)
    )
    hybrid_recommendations = list(
        set(content_based_recommendations + collaborative_filtering_recommendations)
    )
    return hybrid_recommendations[:top_n]


def recommend(params: dict):
    # Get parameters
    flight_id = params["FlightID"]
    fruit_name = params["Fruit"]
    top_n = params["top_n"]

    # Get recommendations
    recommendations = get_hybrid_recommendations(flight_id, fruit_name, top_n)
    output = []

    print(f"Hybrid Recommendations for User {flight_id} based on Product {fruit_name}:")
    for i, recommendation in enumerate(recommendations):
        try:
            recommendation = int(recommendation)
            print(f"{i + 1}. Product: {convert_product_id_to_name(recommendation)}")
            output.append(convert_product_id_to_name(recommendation))
        except ValueError:
            print(f"{i + 1}. Product: {(recommendation)}")
            output.append(recommendation)
    return output


if __name__ == "__main__":
    recommend({"flight_id": "551", "fruit_name": "Pineapple", "top_n": 5})
