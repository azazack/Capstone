/* eslint-disable @typescript-eslint/no-explicit-any */
import { useDebounceFn } from "@vueuse/core";

export default (fun: (...args: any[]) => void) => {
    let controller = new AbortController();

    return useDebounceFn((...args: any[]) => {
        controller.abort();
        controller = new AbortController();
        fun(controller.signal, ...args);
    }, 500);
};
