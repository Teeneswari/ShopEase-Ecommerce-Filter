
import { useState } from "react";

function ProductCard({ product }) {
  const [imageError, setImageError] = useState(false);

  return (
    <div className="product-card">

      <div className="product-image">
        <img
          src={
            imageError
              ? "https://placehold.co/400x300?text=Product+Image"
              : product.image
          }
          alt={product.name}
          loading="lazy"
          onError={() => setImageError(true)}
        />

        <span className="category-tag">
          {product.category}
        </span>
      </div>

      <div className="product-info">

        <h3>{product.name}</h3>

        <div className="product-rating">
          <span>★</span>
          {product.rating} / 5
        </div>

        <div className="product-bottom">
          <p className="price">
            ₹{product.price.toLocaleString("en-IN")}
          </p>

          <span className="availability">
            In Stock
          </span>
        </div>

      </div>
    </div>
  );
}

export default ProductCard;
