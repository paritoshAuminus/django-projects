import React from 'react'
import { Routes, Route } from 'react-router-dom'
import { ProductDetails } from './components'
import { Products } from './pages'

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<Products />} />
        <Route path='/products/:id' element={<ProductDetails />} />
      </Routes>
    </>
  )
}

export default App