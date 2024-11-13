'use client';

import { SessionProvider } from "next-auth/react";

interface SessionProvProps {
    children: React.ReactNode;
}

export default function SessionProv({ children }: SessionProvProps) {
    return (
        <SessionProvider>
            {children}
        </SessionProvider>
    );
}