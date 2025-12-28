import React, { useEffect } from 'react'
import { Link, useParams } from 'react-router-dom'
import { useState } from 'react'
import { BASE_URL } from '../api/api'
import { useCart } from '../context/CartContext'

function ProductDetails() {

  const { id } = useParams()

  const [product, setProduct] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const { addToCart } = useCart()

    useEffect(() => {
      fetch(`${BASE_URL}/api/products/${id}`)
        .then(res => {
          if (!res.ok) {
            throw new Error('Failed to fetch product.')
          }
          return res.json()
        })
        .then(data => (
          setProduct(data),
          setLoading(false)
        ))
        .catch(error => (
          setError(error.message),
          setLoading(false)
        ))
    }, [id, BASE_URL])

  if (loading) {
    return <div className="min-h-screen flex items-center justify-center">Loading...</div>
  }

  if (error) {
    return <div className="min-h-screen flex items-center justify-center text-red-500">Error: {error}</div>
  }

  if (!product) {
    return <div className="min-h-screen flex items-center justify-center">No product found.</div>
  }

  return (
    <Link to={'product/:id'}>
      <div className="min-h-screen bg-gray-50 py-10 px-4">
        <div className="max-w-6xl mx-auto bg-white rounded-xl shadow-md p-6">

          {/* Top Section */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">

            {/* Product Image */}
            <div className="w-full">
              <img
                src={`${product.image}`}
                alt={product.name}
                className="w-full h-105 object-cover rounded-xl shadow-sm"
              />
            </div>

            {/* Product Info */}
            <div className="flex flex-col justify-between">
              <div>
                <h1 className="text-3xl font-bold text-gray-800 mb-3">
                  {product.name || 'No name available'}
                </h1>

                <p className="text-xl font-semibold text-gray-700 mb-4">
                  Rs {product.price || 'No price available'}
                </p>

                <p className="text-gray-600 leading-relaxed mb-6">
                  {product.description || 'No description available...'}
                </p>
              </div>

              {/* Action Buttons */}
              <div className="flex gap-4">
                <button onClick={() => addToCart(product)} className="flex-1 bg-gray-800 text-white py-3 rounded-lg font-medium hover:bg-gray-900 transition">
                  Add to Cart
                </button>
                <button className="flex-1 border border-gray-300 text-gray-700 py-3 rounded-lg font-medium hover:bg-gray-100 transition">
                  Buy Now
                </button>
              </div>
            </div>
          </div>

          {/* Divider */}
          <div className="my-10 border-t"></div>

          {/* Additional Details */}
          <div>
            <h2 className="text-xl font-semibold text-gray-800 mb-4">
              Product Details
            </h2>

            <ul className="space-y-2 text-gray-600">
              <li>• High quality material</li>
              <li>• Modern and stylish design</li>
              <li>• Durable and long-lasting</li>
              <li>• Suitable for everyday use</li>
            </ul>
          </div>
        </div>
      </div>
    </Link>
  )
}

export default ProductDetails
