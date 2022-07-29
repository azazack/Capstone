import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";
import type { RemovableRef } from "@vueuse/shared";

interface Auth {
    admin: RemovableRef<Record<string, unknown>>;
    token: RemovableRef<string>;
}

export const useAuth = defineStore("auth", {
    state: (): Auth => {
        return {
            admin: useStorage("user", {}),
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
            this.admin = user
        },
        setToken(token: string) {
            this.token = token;
        },
    },
});
