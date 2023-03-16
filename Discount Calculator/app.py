from flask import Flask, render_template, request

app = Flask(__name__) # app instance is created using Flask class of flask module

items = []  # a list to store items and their prices


@app.route('/', methods=['GET'])
# Get 
def index():
    return render_template('index.html')


@app.route('/add_item', methods=['POST'])
def add_item():
    item = request.form['item']
    price = float(request.form['price'])
    items.append({'item': item, 'price': price})
    return render_template('index.html', items=items)


@app.route('/calculate_bill', methods=['POST'])
def calculate_bill():
    total = sum(item['price'] for item in items)
    if total < 1000:
        discount = 0.1
    elif total >= 1000 and total <= 2000:
        discount = 0.2
    else:
        discount = 0.3
    discount_amount = round(total * discount, 2)
    final_amount = round(total - discount_amount, 2)

    bill = {
        'items': items,
        'total_bill': total,
        'discount_percentage': discount * 100,
        'discount_amount': discount_amount,
        'final_amount': final_amount
    }
    
    return render_template('bill.html', **bill)
items = []
total_bill = 0.0

if __name__ == '__main__':
    app.run(debug=True)
