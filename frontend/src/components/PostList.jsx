import React from "react";
import API from "../api";

export default function PostList({ posts, refreshPosts }) {
  const deletePost = async (id) => {
    await API.delete(`/delete-post/${id}`);
    refreshPosts();
  };

  return (
    <div>
      <h2>All Posts</h2>

      {posts.length === 0 && <p>No posts yet.</p>}

      {posts.map((post) => (
        <div
          key={post.id}
          style={{
            border: "1px solid #ccc",
            padding: "10px",
            marginBottom: "10px",
          }}
        >
          <p>
            <strong>{post.username}</strong>
          </p>
          <p>{post.text}</p>

          {post.image_path && (
            <img
              src={`http://127.0.0.1:8000/${post.image_path}`}
              alt="uploaded"
              width="200"
            />
          )}

          <button onClick={() => deletePost(post.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
}
