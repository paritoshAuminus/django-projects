import React from 'react'
import { BASE_URL } from '../api/api'
import { Link } from 'react-router-dom'

function ProductCard({ product }) {
  return (
    <Link to={`/products/${product.id}`}>
      <div className='bg-white rounded-xl shadow-md hover:shadow-lg hover:scale-[1.02] transition-transform p-4 cursor-pointer'>
        <img
          src={`${BASE_URL}${product.image}`}
          alt={product.name}
          className="w-full h-56 object-cover rounded-lg mb-4"
        />
        <h2 className="text-lg font-semibold text-gray-800 truncate">
          {product.name}
        </h2>
        <p className="text-gray-600 font-medium">${product.price}</p>
        <p className='text-gray-600 text-sm'>{product.description.slice(0, 55)}...</p>
      </div>
    </Link>
  )
}

export default ProductCard