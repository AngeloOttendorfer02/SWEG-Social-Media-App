import React, { useState } from "react";
import { deletePost } from "../api";
import { useAuth } from "../context/AuthContext";

export default function PostCard({ post, refreshPosts, suggestReplyForPost }) {
    const { user, token } = useAuth();

    // Local state for loading suggestion
    const [loadingSuggestion, setLoadingSuggestion] = useState(false);

    // Manual suggestion regeneration
    const handleSuggestReply = async () => {
        setLoadingSuggestion(true);
        await suggestReplyForPost(post.id);
        setLoadingSuggestion(false);
    };

    return (
        <div className="bg-gradient-to-r from-purple-50 via-pink-50 to-blue-50 rounded-3xl shadow-2xl p-6 mb-6 border border-purple-100">

            {/* Header */}
            <div className="flex justify-between items-center mb-3">
                <h3 className="text-xl font-semibold text-pink-600">{post.username}</h3>
                <span className="text-gray-400 text-sm">{new Date(post.created_at).toLocaleString()}</span>
            </div>

            {/* Sentiment Badge */}
            {post.sentiment && (
                <span
                    className={`inline-block mb-3 px-3 py-1 rounded-full text-sm font-semibold
          ${post.sentiment === "positive"
                            ? "bg-green-100 text-green-700"
                            : post.sentiment === "negative"
                                ? "bg-red-100 text-red-700"
                                : "bg-gray-100 text-gray-700"
                        }`}
                >
                    {post.sentiment.toUpperCase()}
                    {post.sentiment_score !== null && ` (${Math.round(post.sentiment_score * 100)}%)`}
                </span>
            )}

            {/* Post Text */}
            <p className="text-gray-700 mb-4">{post.text}</p>

            {/* Image */}
            {post.resized_image_path && (
                <img
                    src={`${import.meta.env.VITE_API_URL}/${post.resized_image_path}`}
                    alt="post"
                    className="w-full max-h-96 object-cover rounded-2xl mb-4"
                />
            )}

            {/* Suggest Reply Button */}
            <div className="flex gap-3 mt-4">
                <button
                    onClick={handleSuggestReply}
                    disabled={loadingSuggestion}
                    className="bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 disabled:opacity-50 text-white font-semibold px-5 py-2 rounded-full shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-105"
                >
                    {loadingSuggestion ? "Thinking…" : "Suggest reply"}
                </button>
            </div>

            {/* Delete Button */}
            {user?.username === post.username && (
                <div className="flex justify-end mt-4">
                    <button
                        onClick={async () => {
                            try {
                                await deletePost(post.id, token);
                                refreshPosts();
                            } catch (err) {
                                alert(err.response?.data?.detail || "Failed to delete post");
                            }
                        }}
                        className="bg-gradient-to-r from-red-500 to-pink-600 hover:from-red-600 hover:to-pink-700 text-white font-semibold px-5 py-2 rounded-full shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-105"
                    >
                        Delete
                    </button>
                </div>
            )}
        </div>
    );
}
