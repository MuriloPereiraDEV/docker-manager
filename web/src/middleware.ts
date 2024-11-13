import withAuth, { NextAuthMiddlewareOptions, NextRequestWithAuth } from "next-auth/middleware";
import { NextResponse } from "next/server";

const middleware = (request: NextRequestWithAuth) => {
    console.log('[MIDDLEWARE_NEXTAUTH_TOKEN]: ', request.nextauth.token)

    const isHomeRoute = request.nextUrl.pathname === '/';
    const isLoggedIn = !!request.nextauth.token;
    const isPrivateRoutes = request.url.includes('/manager');
    const isAnalystUser = request.nextauth.token?.role === 'analyst';

    if (isPrivateRoutes && !isAnalystUser) {
        return NextResponse.rewrite(new URL('/denied', request.url))
    }

    if (isHomeRoute && isLoggedIn) {
        return NextResponse.redirect(new URL('/manager', request.url));
    }
}

const callbackOptions: NextAuthMiddlewareOptions = () => {}

export default withAuth(middleware, callbackOptions)

export const config = {
    matcher: '/manager'
};