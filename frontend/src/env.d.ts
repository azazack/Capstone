/// <reference types="vite/client" />

declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  // eslint-disable-next-line @typescript-eslint/no-explicit-any, @typescript-eslint/ban-types
  const component: DefineComponent<{}, {}, any>
  export default component
}

declare interface Menu {
  icon?: import("@fortawesome/fontawesome-common-types").IconDefinition;
  name: string;
  route?: { path?: string; name?: string };
  children?: Menu[];
}

declare interface Paginate {
  current_page: number;
  last_page: number;
  next_page?: number;
  total_count: number;
  prev_page?: number;
}
