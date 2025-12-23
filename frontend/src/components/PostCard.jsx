import React from "react";
import { deletePost } from "../api";
import { useAuth } from "../context/AuthContext";

export default function PostCard({ post, refreshPosts }) {
    const { user, token } = useAuth();

    return (
        <div className="bg-gradient-to-r from-purple-50 via-pink-50 to-blue-50 rounded-3xl shadow-2xl p-6 mb-6 border border-purple-100">
            <div className="flex justify-between items-center mb-3">
                <h3 className="text-xl font-semibold text-pink-600">
                    {post.username}
                </h3>
                <span className="text-gray-400 text-sm">
                    {new Date(post.created_at).toLocaleString()}
                </span>
            </div>

            <p className="text-gray-700 mb-4">{post.text}</p>

            {post.resized_image_path && (
                <img
                    src={`${import.meta.env.VITE_API_URL}/${post.resized_image_path}`}
                    alt="post"
                    className="w-full max-h-96 object-cover rounded-2xl mb-4"
                />
            )}

            {user?.username === post.username && (
                <div className="flex justify-end">
                    <button
                        onClick={async () => {
                            try {
                                await deletePost(post.id, token);
                                refreshPosts();
                            } catch (err) {
                                alert(err.response?.data?.detail || "Failed to delete post");
                            }
                        }}
                        className="bg-red-500 hover:bg-red-600 text-white font-medium px-3 py-1 rounded-full shadow-sm transition-all"
                    >
                        Delete
                    </button>
                </div>
            )}
        </div>
    );
}
