(function(w, d) {

/**
 * Custom alert window. Just a util class.
 * Single Instance.
 */
var Alert = (function(){
  var ele = d.getElementById('mask');
  var all = ele.getElementsByTagName('div')[0]; // alert

  function _show() { ele.style.display = 'block'; }
  function _hide() { ele.style.display = 'none'; }

  ele.addEventListener('click', _hide);

  return {
    alert: function(text) {
      all.innerHTML = text;
      _show();
    }
  };

}());

var token = (''+Date.now());

var alert = function(txt) {Alert.alert(txt);}; // override native alert function.

// alert('使用了 Flow.js，见 Github。');

var flow = new Flow({
  target: '/api/share/upload', // target path
  simultaneousUploads: 1,
  speedSmoothingFactor: 0.02,
  query: {
    'roomId': '123456'
  }

});



if (!flow.support) {
  alert('Your browser does not support!');
}


/**
 * Item is a class for each file.
 * @param file {FlowFile}
 */
var Item = function(file) {
  this.filename = file.name;
  this.size = file.size;
  this.format = Item.getFormat(this.filename);
};

/**
 * @return {String} HTML rendered with meta data of file.
 */
Item.prototype.getHTML = function() {
  var result = '' +
    '<li class="ui-list-item">' +
    '<div class="ui-item-icon">' +
    '  <img src="static/img/file-' + this.format + '.png">' +
    '</div>' +
    '<div class="ui-item-right">' +
    '  <span class="ui-item-name">' + this.filename + '</span>' +
    '  <span class="ui-item-addition">' + Item.formatSize(this.size) + '</span>' +
    '</div>'
    '</li>';
  return result;
};

/**
 * Static method. Return size formated with 'KB' or 'MB'.
 * @param siz
 e {Number} size in unit of Byte.
 * @return {String} formated size with unit of 'KB' or 'MB'.
 */
Item.formatSize = function(size) {
  var res;
  var MB = 1000*1000, KB = 1000;
  if (size > MB) {
    res = Math.round(size / MB) + ' MB';
  } else if (size > KB) {
    res = Math.round(size / KB) + ' KB';
  }
  return res;
};

Item.getFormat = function(filename) {
  var rformat = filename.split('').reverse().join('').split('.')[0];
  return rformat.split('').reverse().join('');
};

/**
 * List is a class for store file items.
 * @param ele {HTMLElement} list element.
 */
var List = function(ele) {
  this.ele = ele;
  this.data = []; // type is Item
};

/**
 * Add an item to the list instance.
 * @param item {Item} The item you want to add.
 */
List.prototype.add = function(item) {
  this.data.push(item);
  this.update();
};

/**
 * Update the user interface.
 */
List.prototype.update = function() {
  var itemsHTML = '';
  for (var i = 0, len = this.data.length; i < len; i++) {
    itemsHTML += this.data[i].getHTML();
  }
  this.ele.innerHTML = itemsHTML;
};

List.prototype.remove = function() {
  // @todo
};

var fileList = new List(d.getElementById('file-list'));
var uploadBtn = d.getElementById('upload');

flow.assignBrowse(d.getElementById('browse'));
flow.assignDrop(d.getElementById('drop-area'));

flow.on('fileAdded', function(file, event){
  var fileItem = new Item(file);
  fileList.add(fileItem);
  console.log(file, event);
});

flow.on('filesSubmitted', function(file, event) {
  flow.upload();
})

flow.on('fileSuccess', function(file,message){
  console.log(file,message);
});

flow.on('fileError', function(file, message){
  console.log(file, message);
});

flow.on('catchAll', function(event) {
  console.log('catchAll', arguments);
})

uploadBtn.addEventListener('click', function(e) {

});

}(window, document));
