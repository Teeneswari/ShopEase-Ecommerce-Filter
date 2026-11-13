
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ShopEase E-Commerce API",
    description="Product filtering and sorting API",
    version="1.0"
)

# Enable communication with React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# MASTER PRODUCT INVENTORY
# ==========================================

products = [
    {
        "id": 1,
        "name": "iPhone 15",
        "category": "Electronics",
        "price": 65000,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S24",
        "category": "Electronics",
        "price": 55000,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400"
    },
    {
        "id": 3,
        "name": "HP Laptop",
        "category": "Electronics",
        "price": 45000,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400"
    },
    {
        "id": 4,
        "name": "Sony Headphones",
        "category": "Electronics",
        "price": 2500,
        "rating": 4.2,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400"
    },
    {
        "id": 5,
        "name": "Smart Watch",
        "category": "Electronics",
        "price": 3500,
        "rating": 4.0,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"
    },
    {
        "id": 6,
        "name": "Wireless Mouse",
        "category": "Electronics",
        "price": 799,
        "rating": 4.3,
        "image": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=400"
    },
    {
        "id": 7,
        "name": "Bluetooth Speaker",
        "category": "Electronics",
        "price": 2200,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400"
    },
    {
        "id": 8,
        "name": "Gaming Keyboard",
        "category": "Electronics",
        "price": 1800,
        "rating": 4.1,
        "image": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=400"
    },
    {
        "id": 9,
        "name": "Cotton T-Shirt",
        "category": "Apparel",
        "price": 500,
        "rating": 4.1,
        "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400"
    },
    {
        "id": 10,
        "name": "Denim Jeans",
        "category": "Apparel",
        "price": 1500,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1542272604-787c3835535d?w=400"
    },
    {
        "id": 11,
        "name": "Winter Jacket",
        "category": "Apparel",
        "price": 3000,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400"
    },
    {
        "id": 12,
        "name": "Formal Shirt",
        "category": "Apparel",
        "price": 1200,
        "rating": 3.9,
        "image": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=400"
    },
    {
        "id": 13,
        "name": "Hoodie",
        "category": "Apparel",
        "price": 1800,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400"
    },
    {
        "id": 14,
        "name": "Casual Dress",
        "category": "Apparel",
        "price": 2200,
        "rating": 4.3,
        "image": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400"
    },
    {
        "id": 15,
        "name": "Sneakers",
        "category": "Footwear",
        "price": 2500,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400"
    },
    {
        "id": 16,
        "name": "Running Shoes",
        "category": "Footwear",
        "price": 4000,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1556906781-9a412961c28c?w=400"
    },
    {
        "id": 17,
        "name": "Sports Sandals",
        "category": "Footwear",
        "price": 800,
        "rating": 3.8,
        "image": "https://images.unsplash.com/photo-1603487742131-4160ec999306?w=400"
    },
    {
        "id": 18,
        "name": "Leather Shoes",
        "category": "Footwear",
        "price": 3500,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1614252369475-531eba835eb1?w=400"
    },
    {
        "id": 19,
        "name": "Casual Shoes",
        "category": "Footwear",
        "price": 1800,
        "rating": 4.2,
        "image": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=400"
    },
    {
        "id": 20,
        "name": "Formal Heels",
        "category": "Footwear",
        "price": 2200,
        "rating": 4.0,
        "image": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=400"
    },

    # Additional Electronics
    {
        "id": 21,
        "name": "Canon DSLR Camera",
        "category": "Electronics",
        "price": 42000,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"
    },
    {
        "id": 22,
        "name": "Apple iPad",
        "category": "Electronics",
        "price": 38000,
        "rating": 4.8,
        "image": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"
    },
    {
        "id": 23,
        "name": "Gaming Monitor",
        "category": "Electronics",
        "price": 18000,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400"
    },
    {
        "id": 24,
        "name": "Mechanical Keyboard",
        "category": "Electronics",
        "price": 3200,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=400"
    },
    {
        "id": 25,
        "name": "Power Bank",
        "category": "Electronics",
        "price": 1200,
        "rating": 4.1,
        "image": "https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=400"
    },
    {
        "id": 26,
        "name": "Wireless Earbuds",
        "category": "Electronics",
        "price": 2800,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?w=400"
    },

    # Additional Apparel
    {
        "id": 27,
        "name": "Summer Floral Dress",
        "category": "Apparel",
        "price": 1800,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1612336307429-8a898d10e223?w=400"
    },
    {
        "id": 28,
        "name": "Men's Casual Hoodie",
        "category": "Apparel",
        "price": 2200,
        "rating": 4.3,
        "image": "https://images.unsplash.com/photo-1578681994506-b8f463449011?w=400"
    },
    {
        "id": 29,
        "name": "Women's Top",
        "category": "Apparel",
        "price": 950,
        "rating": 4.2,
        "image": "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=400"
    },
    {
        "id": 30,
        "name": "Casual Blazer",
        "category": "Apparel",
        "price": 3500,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=400"
    },
    {
        "id": 31,
        "name": "Cotton Kurti",
        "category": "Apparel",
        "price": 1100,
        "rating": 4.4,
        "image": "https://images.unsplash.com/photo-1583391733956-6c78276477e7?w=400"
    },
    {
        "id": 32,
        "name": "Winter Sweater",
        "category": "Apparel",
        "price": 1900,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=400"
    },

    # Additional Footwear
    {
        "id": 33,
        "name": "White Sneakers",
        "category": "Footwear",
        "price": 2800,
        "rating": 4.6,
        "image": "https://images.unsplash.com/photo-1495555961986-6d4c1ecb7be3?w=400"
    },
    {
        "id": 34,
        "name": "Running Sports Shoes",
        "category": "Footwear",
        "price": 4500,
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=400"
    },
    {
        "id": 35,
        "name": "Women's Flats",
        "category": "Footwear",
        "price": 1200,
        "rating": 4.1,
        "image": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=400"
    },
    {
        "id": 36,
        "name": "Leather Boots",
        "category": "Footwear",
        "price": 5200,
        "rating": 4.7,
        "image": "https://images.unsplash.com/photo-1608256246200-53e635b5b65f?w=400"
    },
    {
        "id": 37,
        "name": "Casual Loafers",
        "category": "Footwear",
        "price": 2100,
        "rating": 4.3,
        "image": "https://images.unsplash.com/photo-1531310197839-ccf54634509e?w=400"
    },
    {
        "id": 38,
        "name": "Sports Training Shoes",
        "category": "Footwear",
        "price": 3800,
        "rating": 4.5,
        "image": "https://images.unsplash.com/photo-1552346154-21d32810aba3?w=400"
    },
    {
        "id": 39,
        "name": "Premium Running Shoes",
        "category": "Footwear",
        "price": 6500,
        "rating": 4.9,
        "image": "https://images.unsplash.com/photo-1539185441755-769473a23570?w=400"
    },
    {
        "id": 40,
        "name": "Casual Flip Flops",
        "category": "Footwear",
        "price": 450,
        "rating": 3.9,
        "image": "https://images.unsplash.com/photo-1603487742131-4160ec999306?w=400"
    }

]


# ==========================================
# CORE FILTERING AND SORTING FUNCTION
# ==========================================

def filter_products(
    inventory,
    categories=None,
    min_price=None,
    max_price=None,
    min_rating=None,
    sort_by=None
):

    result = []

    # Step 1: Apply all filters
    for product in inventory:

        # Category filter
        if categories and product["category"] not in categories:
            continue

        # Minimum price filter
        if min_price is not None:
            if product["price"] < min_price:
                continue

        # Maximum price filter
        if max_price is not None:
            if product["price"] > max_price:
                continue

        # Minimum rating filter
        if min_rating is not None:
            if product["rating"] < min_rating:
                continue

        result.append(product)

    # Step 2: Sort after filtering
    if sort_by == "price_asc":
        result.sort(key=lambda p: p["price"])

    elif sort_by == "rating_desc":
        result.sort(
            key=lambda p: p["rating"],
            reverse=True
        )

    return result


# ==========================================
# HOME API
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Welcome to ShopEase E-Commerce API",
        "status": "Running"
    }


# ==========================================
# GET ALL CATEGORIES
# ==========================================

@app.get("/api/categories")
def get_categories():

    categories = sorted({
        product["category"]
        for product in products
    })

    return {
        "categories": categories
    }


# ==========================================
# GET AND FILTER PRODUCTS
# ==========================================

@app.get("/api/products")
def get_products(

    categories: list[str] | None = Query(default=None),

    min_price: float | None = Query(default=None, ge=0),

    max_price: float | None = Query(default=None, ge=0),

    min_rating: float | None = Query(default=None, ge=1, le=5),

    sort_by: str | None = None

):

    # Validate price range
    if (
        min_price is not None
        and max_price is not None
        and min_price > max_price
    ):
        raise HTTPException(
            status_code=400,
            detail="Minimum price cannot exceed maximum price"
        )

    # Validate sorting
    if sort_by not in (None, "", "price_asc", "rating_desc"):
        raise HTTPException(
            status_code=400,
            detail="Invalid sorting option"
        )

    # Validate categories
    allowed_categories = {
        "Electronics",
        "Apparel",
        "Footwear"
    }

    if categories:
        invalid = set(categories) - allowed_categories

        if invalid:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid categories: {sorted(invalid)}"
            )

    # Call core filtering function
    filtered_products = filter_products(
        inventory=products,
        categories=categories,
        min_price=min_price,
        max_price=max_price,
        min_rating=min_rating,
        sort_by=sort_by
    )

    return {
        "total": len(filtered_products),
        "filters_applied": {
            "categories": categories,
            "min_price": min_price,
            "max_price": max_price,
            "min_rating": min_rating,
            "sort_by": sort_by
        },
        "products": filtered_products
    }


# ==========================================
# GET SINGLE PRODUCT
# ==========================================

@app.get("/api/products/{product_id}")
def get_product(product_id: int):

    for product in products:

        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


    
