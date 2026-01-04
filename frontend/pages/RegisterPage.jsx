import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { registerUser } from "../src/api";
import { useAuth } from "../src/context/AuthContext";
import "../src/styles/registerpage.css";

export default function RegisterPage() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const { login } = useAuth();
    const navigate = useNavigate();

    const handleRegister = async (e) => {
        e.preventDefault();
        try {
            const data = await registerUser(username, password);
            login(data.access_token);
            navigate("/feed");
        } catch (err) {
            console.error(err);
            alert(err.response?.data?.detail || "Registration failed");
        }
    };

    return (
        <div className="register-container">
            <div className="register-card">
                <h2>Create Account</h2>
                <form onSubmit={handleRegister} className="register-form">
                    <input
                        placeholder="Username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                        className="register-input"
                    />
                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        className="register-input"
                    />
                    <button type="submit" className="register-button">
                        Register
                    </button>
                </form>
                <p className="register-footer">
                    Already have an account?{" "}
                    <span className="register-link" onClick={() => navigate("/login")}>
                        Login
                    </span>
                </p>
            </div>
        </div>
    );
}
