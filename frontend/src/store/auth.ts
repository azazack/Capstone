import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";
import type { RemovableRef } from "@vueuse/shared";

interface Auth {
    admin: RemovableRef<string>;
    token: RemovableRef<string>;
}

export const useAuth = defineStore("auth", {
    state: (): Auth => {
        return {
            admin: useStorage("user", ""),
            token: useStorage("token", ""),
        };
    },
    getters: {
        user: (state) => state.admin,
        isAuth: (state) => !!state.token,
    },
    actions: {
        logout() {
            localStorage.clear();
        },
        setUser(user: Record<string, string>) {
            this.admin = JSON.stringify(user);
        },
        setToken(token: string) {
            this.token = token;
        },
    },
});
