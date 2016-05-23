export function configRouter (router) {
  router.map({
    '/': {
      name: 'login',
      component: require('./components/manager-pages/login-page.vue'),
      auth: false
    },
    '/room/:room_id': {
      component: require('./components/user-pages/messages-page.vue'),
    },
    '/prop': {
      name: 'prop',
      component: require('./components/user-pages/property-page.vue'),
    },
    '/qrcode': {
      name: 'qrcode',
      component: require('./components/user-pages/qrcode-page.vue'),
    },
    '/files': {
      name: 'files',
      component: require('./components/user-pages/files-page.vue'),
    },
    '/history': {
      name: 'history',
      component: require('./components/user-pages/history-page.vue')
    },
    '/feedback': {
      name: 'feedback',
      component: require('./components/user-pages/feedback-page.vue')
    },
    '/chat-entrance': {
      name: 'chat-entrance',
      component: require('./components/user-pages/feedback-page.vue')
    },
    '/chat-entrance': {
      name: 'chat-entrance',
      component: require('./components/user-pages/chat-entrance-page.vue')
    },
    '/home': {
      name: 'home',
      component: require('./components/manager-pages/home-page.vue'),
      auth: true
    },
    '/group-management/:room_id': {
      name: 'group-management',
      component: require('./components/manager-pages/group-management-page.vue'),
      auth: true
    },  
  });
  router.redirect({
    '*': '/'
  })
}