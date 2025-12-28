import React from 'react'
import { Routes, Route } from 'react-router-dom'
import { ProductDetails, Navbar } from './components'
import { Products, Cartpage } from './pages'

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path='/' element={<Products />} />
        <Route path='/products/:id' element={<ProductDetails />} />
        <Route path='/cart' element={<Cartpage />} />
      </Routes>
    </>
  )
}

export default App