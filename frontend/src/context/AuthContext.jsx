import { createContext, useContext, useEffect, useState } from "react";
import { jwtDecode } from "jwt-decode";

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
    const [token, setToken] = useState(null);
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const storedToken = localStorage.getItem("access_token");
        if (storedToken) {
            try {
                const decoded = jwtDecode(storedToken);
                if (decoded?.sub) {
                    setToken(storedToken);
                    setUser({ username: decoded.sub });
                } else {
                    localStorage.removeItem("access_token");
                }
            } catch (err) {
                console.error("Invalid token", err);
                localStorage.removeItem("access_token");
            }
        }
        setLoading(false);
    }, []);

    const login = (jwtToken) => {
        try {
            const decoded = jwtDecode(jwtToken);
            setToken(jwtToken);
            setUser({ username: decoded.sub });
            localStorage.setItem("access_token", jwtToken);
        } catch (err) {
            console.error("Failed to login: invalid token", err);
        }
    };

    const logout = () => {
        localStorage.removeItem("access_token");
        setToken(null);
        setUser(null);
    };

    return (
        <AuthContext.Provider
            value={{ token, user, login, logout, isAuthenticated: !!token }}
        >
            {!loading && children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);
