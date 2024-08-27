import Vue from "vue";
import VueRouter from "vue-router";
import VideoDownloader from "../components/VideoDownloader.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/downloader",
    name: "VideoDownloader",
    component: VideoDownloader,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
