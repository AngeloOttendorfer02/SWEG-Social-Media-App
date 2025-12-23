import React, { useEffect, useState } from "react";
import PostForm from "../src/components/PostForm";
import PostList from "../src/components/PostList";
import { fetchAllPosts } from "../src/api";
import { useAuth } from "../src/context/AuthContext";
import "../src/styles/feedpage.css";
import { useNavigate } from "react-router-dom";

export default function FeedPage() {
    const [posts, setPosts] = useState([]);
    const { user, logout } = useAuth();
    const navigate = useNavigate();

    const loadPosts = async () => {
        try {
            const response = await fetchAllPosts();
            setPosts(response.data.reverse());
        } catch (err) {
            console.error("Error fetching posts:", err);
        }
    };

    useEffect(() => {
        loadPosts();
    }, []);

    return (
        <div className="feed-page">
            {/* Header */}
            <header className="feed-header flex items-center justify-between p-4 bg-gradient-to-r from-purple-500 via-pink-500 to-blue-500 text-white shadow-md sticky top-0 z-50">
                <h1
                    className="app-title text-2xl font-bold cursor-pointer"
                    onClick={() => navigate("/")}
                >
                    SwegApp
                </h1>
                <div className="header-right flex items-center gap-3">
                    <span className="username font-medium">{user?.username}</span>
                    <button
                        onClick={() => navigate("/")}
                        className="header-button bg-white text-purple-600 hover:bg-gray-100"
                    >
                        Home
                    </button>
                    <button
                        onClick={logout}
                        className="header-button bg-red-500 hover:bg-red-600 text-white"
                    >
                        Logout
                    </button>
                </div>
            </header>

            {/* Main Content */}
            <main className="feed-main p-4">
                <PostForm refreshPosts={loadPosts} />
                <PostList posts={posts} refreshPosts={loadPosts} />
            </main>
        </div>
    );
}
