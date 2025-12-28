import { useState, createContext, useContext } from "react";

const CartContext = createContext();

export const CartProvider = ({ children }) => {
    const [cartItems, setCartItems] = useState([]);

    function addToCart(product) {
        const existing = cartItems.find(item => item.id === product.id);

        if (existing) {
            setCartItems(
                cartItems.map(item =>
                    item.id === product.id
                        ? { ...item, quantity: item.quantity + 1 }
                        : item
                )
            );
        } else {
            setCartItems([...cartItems, { ...product, quantity: 1 }]);
        }
    }

    function removeFromCart(id) {
        setCartItems(cartItems.filter(item => item.id !== id));
    }

    function updateQuantity(id, quantity) {
        if (quantity < 1) return;
        setCartItems(
            cartItems.map(item =>
                item.id === id ? { ...item, quantity } : item
            )
        );
    }

    // ✅ CALCULATE TOTAL (ensure number)
    const total = cartItems.reduce(
        (sum, item) =>
            sum + Number(item.product_price) * item.quantity,
        0
    );

    return (
        <CartContext.Provider
            value={{
                cartItems,
                total, // ✅ exposed here
                addToCart,
                removeFromCart,
                updateQuantity
            }}
        >
            {children}
        </CartContext.Provider>
    );
};

export const useCart = () => useContext(CartContext);
