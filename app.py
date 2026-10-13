from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# قائمة منتجات الهوديز الأولية لمتجر OUSHAM
products = [
    {
        "id": 1,
        "name": "OUSHAM Heavyweight Oversized Hoodie",
        "price": 499,
        "image": "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?auto=format&fit=crop&w=600&q=80",
        "tag": "Best Seller"
    },
    {
        "id": 2,
        "name": "OUSHAM Minimalist Black Hoodie",
        "price": 450,
        "image": "https://images.unsplash.com/photo-1509967419530-da38b4704bc6?auto=format&fit=crop&w=600&q=80",
        "tag": "New"
    },
    {
        "id": 3,
        "name": "OUSHAM Graphic Streetwear Hoodie",
        "price": 520,
        "image": "https://images.unsplash.com/photo-1578587018452-892bacefd3f2?auto=format&fit=crop&w=600&q=80",
        "tag": "Limited"
    },
    {
        "id": 4,
        "name": "OUSHAM Neutral Beige Hoodie",
        "price": 470,
        "image": "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?auto=format&fit=crop&w=600&q=80",
        "tag": "Classic"
    }
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.json
    # هنا يمكنك معالجة الطلب وحفظه في قاعدة البيانات محلياً
    cart_items = data.get('items', [])
    total_price = data.get('total', 0)
    print(f"تم استلام طلب جديد! المنتجات: {cart_items}, الإجمالي: {total_price} درهم")
    return jsonify({"status": "success", "message": "تم تأكيد طلبك بنجاح وسنتواصل معك قريباً!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)