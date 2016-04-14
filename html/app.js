var flow = new Flow({
  target: '/upload', // target path
  simultaneousUploads: 1,
  query: {
    groupCode: Date.now()
  }
});


/********** File Item Component *************/

var fileItemTpl = '' +
'<li class="ui-list-item">' +
'  <div class="ui-item-icon"><img src="img/file-{{format}}.png"></div>' +
'  <div class="ui-item-right">' +
'  <span class="ui-item-name">{{file.name}}</span>' +
'  <span class="ui-item-addition">{{isShow ? speed + "/s  ": ""}}{{size}}</span>' +
'  <div :class="{\'ui-progress\': true, \'ui-show\': isShow}"><div class="ui-active-prog" style="width: {{progress}}"></div></div>' +
'  <button class="ui-transparent" v-on:click="removeSelf">X</button>' +
'</li>';

var FileItem = Vue.extend({
  template: fileItemTpl,
  props: ['file', 'index'],
  computed: {
    isShow: function() {
      // 进度条为0或100%时不显示
      return this.file.progress() > 0 && this.file.progress() < 1;
    },
    size: function() {
      return this.trans(this.file.size);
    },
    speed: function() {
      return this.trans(this.file.averageSpeed);
    },
    progress: function() {
      return this.file.progress() * 100 + '%';
    },
    format: function() {
      var rformat = this.file.name.split('').reverse().join('').split('.')[0];
      return rformat.split('').reverse().join('');
    }
  },
  methods: {
    trans: function(size) {
      var MB = 1000*1000, KB = 1000;
      if (+size > MB) {
        return Math.round(+size / MB) + ' MB';
      } else if (+size > KB) {
        return Math.round(+size / KB) + ' KB';
      }
      return +size + ' B';
    },
    removeSelf: function() {
      this.$dispatch('remove', this.index);
    }
  }
});

Vue.component('file-item', FileItem);


/********** File List Component *************/

var fileListTpl = '' +
'<ul class="ui-list">' +
'  <file-item v-for="item in items" :file="item" :index="$index" v-on:remove="remove""></file-item>' +
'</ul>';

var FileList = Vue.extend({
  template: fileListTpl,
  data: function() {
    return { items: [], progresses: []}
  },
  methods: {
    add: function(file) {
      this.items.push(file);
    },
    remove: function(index) {
      this.items.splice(index, 1);
    }
  }
});

Vue.component('file-list', FileList);


/********** Header Component *************/

var headerTpl = '' +
    '<div class="ui-header">' +
    '  <div class="ui-header-wp">' +
    '    <h1 class="logo">SHARE</h1>' +
    '    <button class="ui-ghost-button" v-on:click="gen" v-if="pIndex">生成</button>' +
    '    <button class="ui-ghost-button" v-on:click="gen" v-if="pDownload">下载全部</button>' +
    '  </div>' +
    '</div>';

var Header = Vue.extend({
  template: headerTpl,
  props: ['page'],
  computed: {
    pIndex: function() {return this.page == 'index'},
    pDownload: function() {return this.page == 'download'}
  },
  methods: {
    gen: function() {
      alert('Generate!');
    }
  }
});

Vue.component('ui-header', Header);


/********** Main Component *************/
var main = new Vue({el: '#app'});

flow.assignBrowse(document.querySelector('#browse'));
flow.assignDrop(document.getElementById('drop-area'));

flow.on('fileAdded', function(file, event) {
  main.$refs.list.add(file);
});

flow.on('filesSubmitted', function(file, event) {
  flow.upload();
});
