function ProductCard({ product }) {
  return (
    <div className="w-72 rounded-xl border border-gray-200 bg-white overflow-hidden transition-shadow hover:shadow-lg">
      
      {/* Image */}
      <div className="h-44 bg-gray-100 flex items-center justify-center">
        {product.image ? (
          <img
            src={product.image}
            alt={product.name}
            className="h-full w-full object-cover"
          />
        ) : (
          <span className="text-sm text-gray-400">No Image</span>
        )}
      </div>

      {/* Content */}
      <div className="p-4 flex flex-col h-full">
        <h3 className="text-lg font-semibold text-gray-900 mb-1">
          {product.name}
        </h3>

        <p className="text-sm text-gray-600 flex grow mb-3">
          {product.description || 'No description available.'}
        </p>

        <div className="flex items-center justify-between">
          <span className="text-lg font-bold text-gray-900">
            ${product.price}
          </span>

          <button className="px-3 py-1.5 text-sm font-medium rounded-lg bg-black text-white hover:bg-gray-800 transition">
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  )
}

export default ProductCard
