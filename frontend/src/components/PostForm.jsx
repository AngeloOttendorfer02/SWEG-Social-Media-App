import React, { useState } from "react";
import API from "../api";

export default function PostForm({ onPostCreated }) {
  const [username, setUsername] = useState("");
  const [text, setText] = useState("");
  const [image, setImage] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("username", username);
    formData.append("text", text);
    if (image) formData.append("image", image);

    await API.post("/create-post", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });

    setUsername("");
    setText("");
    setImage(null);

    onPostCreated();
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
      <h2>Create Post</h2>

      <input
        type="text"
        placeholder="Username"
        value={username}
        required
        onChange={(e) => setUsername(e.target.value)}
      />

      <textarea
        placeholder="Write something..."
        value={text}
        required
        onChange={(e) => setText(e.target.value)}
      />

      <input type="file" onChange={(e) => setImage(e.target.files[0])} />

      <button type="submit">Post</button>
    </form>
  );
}
