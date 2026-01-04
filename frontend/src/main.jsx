import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { BrowserRouter } from "react-router-dom";
import { AuthProvider } from "../src/context/AuthContext";
import { PostsProvider } from "../src/context/PostContext";
import "../src/styles/main.css";

ReactDOM.createRoot(document.getElementById("root")).render(
    <AuthProvider>
        <PostsProvider>
            <BrowserRouter>
                <App />
            </BrowserRouter>
        </PostsProvider>
    </AuthProvider>
);
