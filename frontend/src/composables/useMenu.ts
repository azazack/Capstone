import {computed} from "vue"

export default () => {
    return computed(() => [
        {
            name: "Dashboard",
            route: {name: "dashboard"},
        },
        {
            name: "Sent",
            route: {name: "sent"},
        },
        {
            name: "Received",
            route: {name: "received"},
        }
    ])
}
