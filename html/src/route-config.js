export function configRouter (router) {
  router.map({
    '/': {
      component: require('./components/messages-page.vue'),

    },
    '/prop': {
      name: 'prop',
      component: require('./components/property-page.vue'),
    },
    '/qrcode': {
      name: 'qrcode',
      component: require('./components/qrcode-page.vue'),
    },
    '/files': {
      name: 'files',
      component: require('./components/files-page.vue'),
    },
    '/history': {
      name: 'history',
      component: require('./components/history-page.vue')
    },
    '/feedback': {
      name: 'feedback',
      component: require('./components/feedback-page.vue')
    }
  });
}