import type { NavigationGuardNext, RouteLocationNormalized } from "vue-router";
import { useAuth } from "../store/auth";

const isAuth = (
    _to: RouteLocationNormalized,
    _from: RouteLocationNormalized,
    next: NavigationGuardNext
): void => {
    const auth = useAuth();

    if (auth.isAuth) {
        next();
        return;
    }
    next("/login");
};

const isGuest = (
    _to: RouteLocationNormalized,
    _from: RouteLocationNormalized,
    next: NavigationGuardNext
): void => {
    const auth = useAuth();

    if (auth.isAuth) {
        next("/");
        return;
    }
    next();
};

export { isAuth, isGuest };
