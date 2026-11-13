
function Sidebar({ filters, updateFilters, resetFilters }) {
  const categories = ["Electronics", "Apparel", "Footwear"];

  const handleCategory = (category) => {
    const updated = filters.categories.includes(category)
      ? filters.categories.filter(c => c !== category)
      : [...filters.categories, category];

    updateFilters("categories", updated);
  };

  const min = filters.min_price;
  const max = filters.max_price;
  const limit = 100000;

  const minPercent = (min / limit) * 100;
  const maxPercent = (max / limit) * 100;

  return (
    <aside className="sidebar">
      <h2>Filters</h2>

      <div className="filter-section">
        <h3>Categories</h3>

        {categories.map(category => (
          <label key={category} className="filter-option">
            <input
              type="checkbox"
              checked={filters.categories.includes(category)}
              onChange={() => handleCategory(category)}
            />
            {category}
          </label>
        ))}
      </div>

      <div className="filter-section">
        <h3>Price Range</h3>

        <div className="price-values">
          <span>₹{min.toLocaleString("en-IN")}</span>
          <span>₹{max.toLocaleString("en-IN")}</span>
        </div>

        <div
          className="range-slider"
          style={{
            "--min": `${minPercent}%`,
            "--max": `${maxPercent}%`
          }}
        >
          <div className="range-track"></div>
          <div className="range-selected"></div>

          <input
            type="range"
            min="0"
            max={limit}
            step="500"
            value={min}
            onChange={e => {
              updateFilters(
                "min_price",
                Math.min(Number(e.target.value), max)
              );
            }}
          />

          <input
            type="range"
            min="0"
            max={limit}
            step="500"
            value={max}
            onChange={e => {
              updateFilters(
                "max_price",
                Math.max(Number(e.target.value), min)
              );
            }}
          />
        </div>
      </div>

      <div className="filter-section">
        <h3>Minimum Rating</h3>

        {[5, 4, 3, 2, 1].map(rating => (
          <label key={rating} className="filter-option">
            <input
              type="radio"
              name="rating"
              checked={String(filters.min_rating) === String(rating)}
              onChange={() => updateFilters("min_rating", rating)}
            />
            {rating} ★ & above
          </label>
        ))}
      </div>

      <button className="reset-btn" onClick={resetFilters}>
        Reset All Filters
      </button>
    </aside>
  );
}

export default Sidebar;
