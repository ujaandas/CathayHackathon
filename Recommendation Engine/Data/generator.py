import random
import csv

# Generate mock interaction data


def generate_interaction_data(user_id, product_id):
    action = random.choice(['purchase', 'view', 'like', 'rating'])
    rating = random.randint(1, 5) if action == 'rating' else None
    # Random timestamp between Jan 1, 2021, and Oct 19, 2022
    timestamp = random.randint(1609459200, 1634620800)

    interaction_data = [user_id, product_id, action, rating, timestamp]

    return interaction_data


# Generate mock user data
def generate_user_data(user_id):
    age = random.randint(18, 60)
    gender = random.choice(['Male', 'Female'])
    location = random.choice(['Location A', 'Location B', 'Location C'])
    favorite_categories = random.choices(
        ['Electronics', 'Clothing', 'Home', 'Beauty'], k=2)
    user_preferences = {
        'favorite_categories': favorite_categories,
        'favorite_brands': [],
        'product_features': {
            'color': random.choice(['Red', 'Blue', 'Green']),
            'size': random.choice(['Small', 'Medium', 'Large']),
            'material': random.choice(['Cotton', 'Leather', 'Plastic']),
            'technical_specs': []
        }
    }

    user_data = [user_id, age, gender, location,
                 favorite_categories, user_preferences]

    return user_data

# Generate mock product data


def generate_product_data(product_id):
    categories = ['Electronics', 'Clothing', 'Home', 'Beauty']
    product_name = f'Product {product_id}'
    description = f'This is the description for Product {product_id}.'
    category = random.choice(categories)
    price = round(random.uniform(10, 1000), 2)
    product_features = {
        'color': random.choice(['Red', 'Blue', 'Green']),
        'size': random.choice(['Small', 'Medium', 'Large']),
        'material': random.choice(['Cotton', 'Leather', 'Plastic']),
        'technical_specs': []
    }

    product_data = [product_id, product_name,
                    description, category, price, product_features]

    return product_data

# Generate mock data


def generate_mock_data(num_users, num_products, num_interactions):
    users = []
    products = []
    interactions = []

    # Generate user data
    for i in range(num_users):
        user_data = generate_user_data(i)
        users.append(user_data)

    # Generate product data
    for i in range(num_products):
        product_data = generate_product_data(i)
        products.append(product_data)

    # Generate interaction data
    for i in range(num_interactions):
        user_id = random.randint(0, num_users - 1)
        product_id = random.randint(0, num_products - 1)
        interaction_data = generate_interaction_data(user_id, product_id)
        interactions.append(interaction_data)

    # Save data to CSV files
    with open('./users.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['user_id', 'age', 'gender', 'location',
                        'favorite_categories', 'user_preferences'])  # Write header row
        writer.writerows(users)  # Write user data rows

    with open('./products.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['product_id', 'product_name', 'description',
                        'category', 'price', 'product_features'])  # Write header row
        writer.writerows(products)  # Write product data rows

    with open('./interactions.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['user_id', 'product_id', 'action',
                        'rating', 'timestamp'])  # Write header row
        writer.writerows(interactions)  # Write interaction data rows


# Generate mock data with 100 users, 50 products, and 500 interactions
generate_mock_data(100, 50, 500)
