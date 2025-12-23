import axios from "axios";

const API = axios.create({
    baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
    headers: {
        "Content-Type": "application/json",
    },
    withCredentials: true,
});

export const registerUser = async (username, password) => {
    const res = await API.post("/register", { username, password });
    return res.data;
};

export const loginUser = async (username, password) => {
    const res = await API.post("/login", { username, password });
    return res.data;
};

export const fetchAllPosts = () => API.get("/get-all-posts");

export const createPost = (formData, token) =>
    API.post("/create-post", formData, {
        headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `Bearer ${token}`,
        },
    });

export const deletePost = (postId, token) =>
    API.delete(`/delete-post/${postId}`, {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    });

export default API;
