import { useState, useEffect } from 'react'
// import ProductCard from '../components/ProductCard'
import { BASE_URL } from '../api/api'
import { ProductCard } from '../components'

function Products() {
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    fetch(`${BASE_URL}/api/products/`)
      .then(res => {
        if (!res.ok) {
          throw new Error('Failed to fetch products')
        }
        return res.json()
      })
      .then((data) => (
        setProducts(data),
        console.log(data),
        setLoading(false)
      ))
      .catch(error => (
        setError(error.message),
        setLoading(false)
      ))
  }, [])

  if (loading) {
    return <div className='flex h-full w-full justify-center items-center text-lg text-gray-600'>Loading...</div>
  }

  if (error) {
    return <div className='flex h-full w-full justify-center items-center text-lg text-red-600'>{error}</div>
  }

  return (
    <div className="min-h-screen bg-gray-100">
      <h1 className='text-3xl font-bold text-center py-6 bg-white shadow-md'>Product List</h1>
      <div className='grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4 p-6'>
        {products.length > 0 ? (
          products.map(product => (
            <ProductCard key={product.id} product={product} />
          ))
        ): (
          <p className='flex h-full w-full justify-center items-center text-lg text-gray-600'>No products available...</p>
        )}
      </div>
    </div>
  )
}

export default Products
