import React, { useState } from "react";
import { createPost } from "../api";
import { useAuth } from "../context/AuthContext";

export default function PostForm({ refreshPosts }) {
  const [content, setContent] = useState("");
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const { token, user } = useAuth();

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setPreview(URL.createObjectURL(selectedFile));
    } else {
      setFile(null);
      setPreview(null);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!content.trim() && !file) return;

    const formData = new FormData();
    formData.append("text", content);
    if (file) formData.append("image", file);

    try {
      await createPost(formData, token);
      setContent("");
      setFile(null);
      setPreview(null);
      setTimeout(() => refreshPosts(), 500);
    } catch (err) {
      alert(err.response?.data?.detail || "Failed to create post");
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="post-form bg-white rounded-2xl shadow-lg p-5 mb-6 flex flex-col gap-4"
    >
      <textarea
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="What's on your mind?"
        className="post-textarea resize-none p-4 rounded-xl border border-gray-300 focus:border-purple-500 focus:ring-2 focus:ring-purple-200 outline-none transition-all text-gray-700"
        rows={4}
      />

      {/* File Input */}
      <label className="file-label flex items-center justify-center gap-2 p-2 border-2 border-dashed border-gray-300 rounded-xl cursor-pointer hover:bg-gray-50 transition">
        <span>{file ? file.name : "Attach an image"}</span>
        <input
          type="file"
          onChange={handleFileChange}
          className="hidden"
          accept="image/*"
        />
      </label>

      {/* Preview */}
      {preview && (
        <div className="image-preview mt-2">
          <img
            src={preview}
            alt="Preview"
            className="rounded-xl max-h-64 w-full object-contain shadow-md"
          />
        </div>
      )}

      <button
        type="submit"
        className="post-submit bg-gradient-to-r from-purple-500 via-pink-500 to-blue-500 text-white font-semibold py-2 px-6 rounded-xl shadow-md hover:scale-105 transition-transform"
      >
        Post
      </button>
    </form>
  );
}
