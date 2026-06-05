IMAGE_MAP = {

    # Gaming
    "Gaming Mouse": "images/products/gaming_mouse.jpg",
    "Gaming Keyboard": "images/products/gaming_keyboard.jpg",
    "Gaming Headset": "images/products/gaming_headset.jpg",
    "Gaming Chair": "images/products/gaming_chair.jpg",
    "RGB Mouse Pad": "images/products/rgb_mousepad.jpg",
    "Gaming Monitor": "images/products/gaming_monitor.jpg",

    # Electronics
    "Laptop": "images/products/laptop.jpg",
    "Smartphone": "images/products/smartphone.jpg",
    "Tablet": "images/products/tablet.jpg",
    "Smart Watch": "images/products/smartwatch.jpg",
    "Bluetooth Speaker": "images/products/speaker.jpg",
    "Webcam": "images/products/webcam.jpg",

    # Fashion
    "T-Shirt": "images/products/tshirt.jpg",
    "Jeans": "images/products/jeans.jpg",
    "Jacket": "images/products/jacket.jpg",
    "Sneakers": "images/products/sneakers.jpg",
    "Hoodie": "images/products/hoodie.jpg",
    "Cap": "images/products/cap.jpg",

    # Books
    "Python Programming": "images/products/python_book.jpg",
    "DSA Handbook": "images/products/dsa_book.jpg",
    "Machine Learning": "images/products/machine_learning_book.jpg",
    "Data Science": "images/products/data_science_book.jpg",
    "Web Development": "images/products/web_development_book.jpg",
    "AI Fundamentals": "images/products/ai_book.jpg",

    # Sports
    "Football": "images/products/football.jpg",
    "Cricket Bat": "images/products/cricket_bat.jpg",
    "Tennis Racket": "images/products/tennis_racket.jpg",
    "Basketball": "images/products/basketball.jpg",
    "Yoga Mat": "images/products/yoga_mat.jpg",
    "Gym Gloves": "images/products/gym_gloves.jpg"
}


def get_image(product_name):

    for key in IMAGE_MAP:

        if key.lower() in product_name.lower():

            return IMAGE_MAP[key]

    return None