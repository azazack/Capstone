import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import { isAuth, isGuest } from "../middleware/auth";

const routes: RouteRecordRaw[] = [
    // {
    //     path: "/",
    //     beforeEnter: isAuth,
    //     component: () => import("../layouts/index.vue"),
    //     children: [
    //         {
    //             path: "",
    //             redirect: "/dashboard",
    //         },
    //     ],
    // },
    {
        name: "login",
        path: "/login",
        beforeEnter: isGuest,
        component: () => import("../pages/login.vue"),
    },
    {
        name: "register",
        path: "/register",
        beforeEnter: isGuest,
        component: () => import("../pages/register.vue"),
    },
    {
        name: "test",
        path: "/",
        beforeEnter: isAuth,
        component: () => import("../pages/test.vue"),
    },
];

export const router = createRouter({
    scrollBehavior() {
        // always scroll to top
        return {
            el: "#app",
            top: 0,
        };
    },
    routes,
    history: createWebHistory(),
});
