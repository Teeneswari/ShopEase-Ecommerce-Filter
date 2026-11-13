
import { useEffect, useState } from "react";
import Sidebar from "./components/Sidebar";
import ProductGrid from "./components/ProductGrid";
import "./App.css";

function App() {
  const [filters, setFilters] = useState({
    categories: [],
    min_price: 0,
    max_price: 100000,
    min_rating: "",
    sort_by: ""
  });

  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchProducts = async () => {
      setLoading(true);
      setError("");

      try {
        const params = new URLSearchParams();

        filters.categories.forEach(category => {
          params.append("categories", category);
        });

        params.set("min_price", filters.min_price);
        params.set("max_price", filters.max_price);

        if (filters.min_rating !== "") {
          params.set("min_rating", filters.min_rating);
        }

        if (filters.sort_by) {
          params.set("sort_by", filters.sort_by);
        }

        const response = await fetch(
          `http://127.0.0.1:8000/api/products?${params.toString()}`
        );

        if (!response.ok) {
          throw new Error("Unable to fetch products");
        }

        const data = await response.json();
        setProducts(data.products);

      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, [filters]);

  const updateFilters = (key, value) => {
    setFilters(prev => ({
      ...prev,
      [key]: value
    }));
  };

  const resetFilters = () => {
    setFilters({
      categories: [],
      min_price: 0,
      max_price: 100000,
      min_rating: "",
      sort_by: ""
    });
  };

  return (
    <div className="app">

      <header className="header">
        <h1>ShopEase</h1>
        <p>Find your perfect product</p>
      </header>

      <div className="main-layout">

        <Sidebar
          filters={filters}
          updateFilters={updateFilters}
          resetFilters={resetFilters}
        />

        <ProductGrid
          products={products}
          loading={loading}
          error={error}
          sortBy={filters.sort_by}
          updateFilters={updateFilters}
          resetFilters={resetFilters}
        />

      </div>
    </div>
  );
}

export default App;
