<template>
  <div class="left-part">
    <group>
      <cell title="成员管理" @click="groupFunc = 'mbMang'"></cell>
      <cell title="群组信息" @click="groupFunc = 'gpInfo'"></cell>
      <cell title="群二维码" @click="groupFunc = 'gpQruc'"></cell>
    </group>
    <group>
      <cell title="删除群组" @click="dlGroup"></cell>
    </group>
  </div>
  <div class="breakline"></div>
  <div class="right-part" v-if="groupFunc === 'gpInfo'">
    <m-group-form></m-group-form>
  </div>
  <div class="right-part" v-if="groupFunc==='mbMang'">
    <div class="search-wrapper">
  	 <m-search></m-search>
    </div>
    <group>
      <mem-cell name="kani"></mem-cell>
      <mem-cell name="mike"></mem-cell>
    </group>
  </div>
  <div class="right-part" v-if="groupFunc==='gpQruc'">
    <p>显示二维码</p>
  </div>	
</template>

<style scoped>

.breakline {
  display: inline-block;
  height: 1000px;
  border-right: 1px solid #ccc;
}

.left-part {
  width: 45%;
}

.right-part {
  width: 45%;
  margin-right: 3%;
}
.search-wrapper {
  margin-top: 20px;
}

</style>

<script>
import MGroupForm from './group-info-form'
import {Group, Cell, Search} from 'vux'
import MemCell from './../../MemberCell'
import MSearch from './../../MySearch'

export default {
	data() {
		return {
			groupFunc: 'gpInfo'
		}
	},
	methods: {
    dlGroup: () => console.log('delete')
	},
	components: {
		MGroupForm,
		Group,
		Cell,
		MemCell	,
		Search,
		MSearch
	}
}
</script>