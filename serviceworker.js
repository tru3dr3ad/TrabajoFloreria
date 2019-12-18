var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/css/estilos.css',
    '/static/core/img/FlorLoto.png',
    '/galeria',
    '/nueva-flores',
];

self.addEventListener('install', function(event) {
    // Perform install steps
    event.waitUntil(
        caches.open(CACHE_NAME)
        .then(function(cache) {
            console.log('Opened cache');
            return cache.addAll(urlsToCache);
        })
    );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        fetch(event.request)
        .then(function(result) {
            return caches.open(CACHE_NAME)
                .then(function(c) {
                    c.put(event.request.url, result.clone());
                    return result;
                })
        })
        .catch(function(e) {
            return caches.match(event.request)
        })
    );
});

// NOTIFICACIONES PUSH
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
    apiKey: "AIzaSyA57Ps0lyaVXkQack1jd3E6kSrVZx7fHg8",
    authDomain: "floreria-e7984.firebaseapp.com",
    databaseURL: "https://floreria-e7984.firebaseio.com",
    projectId: "floreria-e7984",
    storageBucket: "floreria-e7984.appspot.com",
    messagingSenderId: "52219613875",
    appId: "1:52219613875:web:e39023e9a6eee3650416c6"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload) {
    console.log("Ha llegado una notificacion")

    let titulo = payload.notification.title;
    let opciones = {
        body: payload.notification.body,
        icon: payload.notification.icon
    }
    self.registration.showNotification(titulo, opciones);
});