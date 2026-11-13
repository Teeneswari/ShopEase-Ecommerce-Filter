
import ProductCard from "./ProductCard";

function ProductGrid({
  products,
  loading,
  error,
  sortBy,
  updateFilters,
  resetFilters
}) {

  return (
    <main className="product-area">

      <div className="product-heading">

        <div>
          <h2>Our Products</h2>
          <p>{products.length} products found</p>
        </div>

        <select
          value={sortBy}
          onChange={e =>
            updateFilters("sort_by", e.target.value)
          }
        >

          <option value="">Default Sorting</option>

          <option value="price_asc">
            Price: Low to High
          </option>

          <option value="rating_desc">
            Top Rated First
          </option>

        </select>

      </div>

      {loading ? (

        <p>Loading products...</p>

      ) : error ? (

        <p className="error">{error}</p>

      ) : products.length === 0 ? (

        <div className="empty-state">

          <h2>No items match your criteria.</h2>

          <button onClick={resetFilters}>
            Reset Filters
          </button>

        </div>

      ) : (

        <div className="product-grid">

          {products.map(product => (
            <ProductCard
              key={product.id}
              product={product}
            />
          ))}

        </div>

      )}

    </main>
  );
}

export default ProductGrid;
