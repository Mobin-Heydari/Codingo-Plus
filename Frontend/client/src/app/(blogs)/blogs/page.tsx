import next from "next";
import { Blogs } from "@/types/blog";

export default async function BlogsPage() {
  const data = await fetch("http://127.0.0.1:8000/blogs/blog/");
  const Blogs = await data.json();

  return <main></main>;
}