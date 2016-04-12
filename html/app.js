var flow = new Flow({
  target: '/upload', // target path
});

/********** File Item Component *************/
var fileItemTpl = '' + 
'<li class="ui-list-item">' +
'  <div class="ui-item-icon"><img src="img/file-{{format}}.png"></div>' +
'  <div class="ui-item-right">' +
'  <span class="ui-item-name">{{file.name}}</span>' +
'  <span class="ui-item-addition">{{size}}</span>' +
'  <div class="ui-progress"><div class="ui-active-prog" style="width: {{progress}}"></div></div>' +
'  <button class="ui-transparent" v-on:click="removeSelf">X</button>' +
'</li>';

var FileItem = Vue.extend({
  template: fileItemTpl,
  props: ['file', 'index'],
  data: function() {return {prog: 0}},
  computed: {
    size: function() {
      var MB = 1000*1000, KB = 1000;
      if (+this.file.size > MB) {
        return Math.round(+this.file.size / MB) + ' MB';
      } else if (+this.file.size > KB) {
        return Math.round(+this.file.size / KB) + ' KB';
      }
      return +this.file.size = ' B';
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
    removeSelf: function() {
      this.$dispatch('remove', this.index);
    },
    setProgress: function(p) {
      this.prog = p;
    }
  }
});

Vue.component('file-item', FileItem);

/********** File List Component *************/
var fileListTpl = '' +
'<ul class="ui-list">' +
'  <file-item v-for="item in items" :file="item" :index="$index" v-on:remove="remove" v-ref="item.uniqueIdentifier"></file-item>' +
'</ul>';

var FileList = Vue.extend({
  template: fileListTpl,
  data: function() {
    return { items: [] }
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

flow.on('fileProgress', function(file) {
  main.$refs.list.$refs[file.uniqueIdentifier].setProgress(file.progress());
});