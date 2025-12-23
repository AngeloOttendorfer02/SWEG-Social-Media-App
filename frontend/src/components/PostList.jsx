import React from "react";
import PostCard from "./PostCard";

export default function PostList({ posts, refreshPosts }) {
  return (
    <div className="flex flex-col">
      {posts.length > 0 ? (
        posts.map((post) => (
          <PostCard key={post.id} post={post} refreshPosts={refreshPosts} />
        ))
      ) : (
        <p className="text-gray-500 text-center mt-6">No posts yet. Be the first to post!</p>
      )}
    </div>
  );
}
