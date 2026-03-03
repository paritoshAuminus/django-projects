import BASE_URL from "../api/api"

// -------------------------------------------
// AUTHENTICATION 
// ------------------------------------------- 

class Auth{
    // register
    async register() {
        try {
            const response = await fetch(`${BASE_URL}/auth/v1/login/`, {
            })            
        } catch (error) {
            
        }

    }
}