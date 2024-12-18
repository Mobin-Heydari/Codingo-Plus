import type { NextConfig } from "next";

const nextConfig: NextConfig = {

  apiBUrl: 'http://127.0.0.1:8000/',

  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'localhost',
        port: '8000',
      },
      {
        protocol: 'http',
        hostname: '127.0.0.1',
        port: '8000',
      },
    ],
  },
};

export default nextConfig;