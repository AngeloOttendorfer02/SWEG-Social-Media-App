import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { fetchAllPosts } from "../src/api";
import "../src/styles/homepage.css";

export default function HomePage() {
    const navigate = useNavigate();
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const loadPosts = async () => {
            try {
                const res = await fetchAllPosts();
                setPosts(res.data);
            } catch (err) {
                console.error("Error fetching posts:", err);
            } finally {
                setLoading(false);
            }
        };
        loadPosts();
    }, []);

    const handleLogin = () => navigate("/login");
    const handleRegister = () => navigate("/register");

    return (
        <div className="home-page">
            <header className="hero-section">
                <h1>Welcome to SWEG Social</h1>
                <p>Connect, share, and explore amazing posts!</p>
                <div className="hero-buttons">
                    <button onClick={handleRegister}>Sign Up</button>
                    <button onClick={handleLogin}>Login</button>
                </div>
            </header>

            <main className="feed-section">
                <h2>Latest Posts</h2>
                {loading ? (
                    <p>Loading posts...</p>
                ) : posts.length === 0 ? (
                    <p>No posts yet. Be the first to post!</p>
                ) : (
                    <div className="posts-list">
                        {posts.map((post) => (
                            <div className="post-card" key={post.id}>
                                <strong>{post.username}</strong>
                                <p>{post.text}</p>
                                {post.resized_image_path && (
                                    <img
                                        src={`${import.meta.env.VITE_API_URL}/${post.resized_image_path}`}
                                        alt="post"
                                    />
                                )}
                            </div>
                        ))}
                    </div>
                )}
            </main>
        </div>
    );
}
