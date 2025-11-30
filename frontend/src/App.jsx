import React, { useEffect, useState } from "react";
import API from "./api";
import PostForm from "./components/PostForm";
import PostList from "./components/PostList";

export default function App() {
  const [posts, setPosts] = useState([]);
  const [filterUser, setFilterUser] = useState("");

  const loadPosts = async () => {
    let response;

    if (filterUser.trim() === "") {
      response = await API.get("/get-all-posts");
    } else {
      response = await API.get(`/get-all-posts-by-user/${filterUser}`);
    }

    setPosts(response.data);
  };

  useEffect(() => {
    loadPosts();
  }, [filterUser]);

  return (
    <div style={{ width: "600px", margin: "0 auto", padding: "20px" }}>
      <h1>Social Media App</h1>

      <PostForm onPostCreated={loadPosts} />

      <input
        type="text"
        placeholder="Filter by username"
        value={filterUser}
        onChange={(e) => setFilterUser(e.target.value)}
        style={{ marginBottom: "20px", width: "100%" }}
      />

      <PostList posts={posts} refreshPosts={loadPosts} />
    </div>
  );
}
