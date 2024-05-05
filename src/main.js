import { createApp } from "vue";
import { createPinia } from "pinia";
import CarbonComponents from "@carbon/vue";

import "./style.css";
import "carbon-components/css/carbon-components.css";
import "@carbon/web-components/es/components/ui-shell/index.js";

import router from "./router";
import App from "./App.vue";

// const store = createPinia();
const app = createApp(App);

app.use(createPinia())
  .use(router)
  .use(CarbonComponents)
  .mount("#app");
