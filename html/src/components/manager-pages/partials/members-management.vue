<style scoped>
  .m-search-box {
    position: relative;
    margin-top: 20px;
  }
  .m-icon-search {
    position: absolute;
    left: 1.2em;
    top: 0.7em;
  }
  .m-icon-search::before {
    content: "\EA0E";
    font-family: weui;
    color: #AAA;
  }
  .m-search-box input {
    display: block;
    min-width: 80%;
    border: 1px solid #DADADA ;
    border-radius: 10px;
    font-size: 1.3em;
    padding: 0.5em 2em;
  }
  .hide {
		display: none;
  }
  .show {
  	display: flex;
  }
</style>

<template>
	<div class="search-wrapper">
	  <div class="m-search-box">
	    <span class="m-icon-search"></span>
	    <input @input="searching" class="weui-input" type="text" title="" placeholder="搜索">
	  </div>
  </div>
  <group >
    <mem-cell v-for="member in members" :name="member.nick_name" :uid="member.uid" :id="getOwnId(member.uid)"></mem-cell>
  </group>
</template>

<script>
import {Group, Cell} from 'vux'
import MemCell from './../../MemberCell'
import { getMembers } from './../../../vuex/getters'

export default {
	vuex: {
		getters:{
			members: getMembers
		}
	},
	computed: {
		inSearch(index) {
			return true;
		}
	},
	methods: {
		getOwnId(id) {
			return "mem" + id;
		},
		searching(event) {
			var str = $(event.target).val();
			for(var i = 0; i < this.members.length; i++) {
				if(this.members[i].nick_name.indexOf(str) !== -1) {
					$('#'+this.getOwnId(this.members[i].uid)).removeClass('hide').addClass('show');
				} else {
					$('#'+this.getOwnId(this.members[i].uid)).removeClass('show').addClass('hide');		
				}
			}
		}
	},
	components: {
		Group,
		Cell,
		MemCell
	}
}
</script>
