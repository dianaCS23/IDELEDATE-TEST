const express = require('express');
const app = express();
app.use(express.json());  

// Mock database
let products = [
    { id: 1, title: "Camisetah", price: 29.99 },
    { id: 2, title: "Pantalones", price: 49.99 }
];

// 1. Get the latest product from the database
app.get('/products/latest', (req, res) => {
    if (products.length > 0) {
        const latestProduct = products[products.length - 1];
        res.status(200).json(latestProduct);
    } else {
        res.status(404).json({ message: "No products available" });
    }
});

// 2. Update a product with invalid data
app.put('/products/:id', (req, res) => {
    const product = products.find(p => p.id === parseInt(req.params.id));
    if (!product) {
        return res.status(404).json({ message: "Product not found" });
    }

    const { price } = req.body;
    if (price < 0) {
        return res.status(400).json({ message: "Invalid price. Price cannot be negative." });
    }

    product.price = price || product.price;
    res.status(200).json(product);
});

// 3. Add a new product with missing or invalid data
app.post('/products', (req, res) => {
    const { title, price } = req.body;

    if (!title || !price) {
        return res.status(400).json({ message: "Title and price are required." });
    }

    const newProduct = {
        id: products.length + 1,
        title,
        price
    };

    products.push(newProduct);
    res.status(201).json(newProduct);
});

// 4. Delete a product by ID
app.delete('/products/:id', (req, res) => {
    const productIndex = products.findIndex(p => p.id === parseInt(req.params.id));
    if (productIndex === -1) {
        return res.status(404).json({ message: "Product not found" });
    }

    products.splice(productIndex, 1); // Remove the product from the array
    res.status(204).send(); // No content to send back
});

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`API running on http://localhost:${port}`);
});
