import {createRouter, createWebHistory} from "vue-router";
import facultes from "../components/facultes.vue";
import laboratoires from "../components/laboratoires.vue";
import publications from "../components/publications.vue";
import chercheurs from "../components/chercheurs.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/facultes",
            name: "facultes",
            component: facultes,
        },
        {
            path: "/chercheurs",
            name: "chercheurs",
            component: chercheurs,
        },
        {
            path: "/publications",
            name: "publications",
            component: publications,
        },
        {
            path: "/labos",
            name: "laboratoires",
            component: laboratoires,
        }
        /* {
          path: '/about',
          name: 'about',
          // route level code-splitting
          // this generates a separate chunk (About.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import('../views/AboutView.vue')
        }*/
    ],
});

export default router;
