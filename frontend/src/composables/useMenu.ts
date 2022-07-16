import {computed} from "vue"

export default () => {
    return computed(() => [
        {
            name: "Dashboard",
            route: {name: "dashboard"},
            children:[
                {
                    name: "Dashboard",
                    route: {name: "dashboard"},
                }
            ]
        },
    ])
}
