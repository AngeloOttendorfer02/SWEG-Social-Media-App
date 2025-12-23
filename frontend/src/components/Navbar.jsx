import React from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
    return (
        <nav className="navbar p-4 bg-gray-800 text-white flex justify-between">
            <Link to="/" className="font-bold text-xl">SocialApp</Link>
            <div className="space-x-4">
                <Link to="/login">Login</Link>
                <Link to="/register">Register</Link>
            </div>
        </nav>
    );
}
