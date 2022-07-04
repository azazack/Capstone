import { useAxios, UseAxiosOptions } from "@vueuse/integrations/useAxios";
import type { AxiosInstance } from "axios";
import axios, { AxiosRequestConfig } from "axios";
import { notify } from "@kyvg/vue3-notification";

class AxiosSingleton {
    private static instance: AxiosInstance;

    // eslint-disable-next-line @typescript-eslint/no-empty-function
    private constructor() {}

    public static getInstance(): AxiosInstance {
        if (!AxiosSingleton.instance) {
            AxiosSingleton.instance = axios.create({
                headers: {
                    "content-type": "application/json",
                    accept: "application/json",
                },
            });

            AxiosSingleton.instance.interceptors.response.use(
                (response) => {
                    return response;
                },
                (err) => {
                    const errors = err.response?.data;
                    if (errors.errors)
                        Object.values(errors.errors).forEach((key): void => {
                            notify({
                                title: `${key}`,
                                type: "error",
                            });
                        });
                    else
                        notify({
                            title: errors.error,
                            type: "error",
                        });

                    // if (
                    //     err.response.status === 401 &&
                    //     err.config.url !== "/api/admin/login"
                    // ) {
                    //     localStorage.clear();
                    //     window.location.reload();
                    // }
                }
            );
        }

        if (localStorage.token) {
            AxiosSingleton.instance.defaults.headers.common = {
                ...AxiosSingleton.instance.defaults.headers.common,
                authorization: localStorage.token,
            };
        }

        return AxiosSingleton.instance;
    }
}

export default (
    path?: string,
    config: AxiosRequestConfig = {},
    options: UseAxiosOptions = { immediate: true }
) => {
    if (!path)
        return {
            ...useAxios(AxiosSingleton.getInstance()),
            axios: AxiosSingleton.getInstance(),
        };
    return {
        ...useAxios(path, config, AxiosSingleton.getInstance(), options),
        axios: AxiosSingleton.getInstance(),
    };
};
