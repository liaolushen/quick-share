<style scoped>
	#groups {
		min-height: 100%;
		background-color: #EAEAEA;
	}
	#groups header {
		color: #A4A5A5;
		padding: 25px 0 0 15px;
	}
	.clearfix:after {
		content: '.';
		height: 0;
		visibility: hidden;
		display: block;
		clear: both;
	}
</style>

<template>
	<div class="view-page" id="home-page">
		<m-header></m-header>
		<div id="groups" class="clearfix">
			<header>你所创建的群组</header>
			<group-card v-for="group in groupList" :during="group.during" :title="group.title" :date="group.date"></group-card>
			<group-card during="10:00-16:00" title="2016 国际体验设计大会" date="6月29日"></group-card>
			<group-card></group-card>
			<group-card during="10:00-16:00" title="2016 国际体验设计大会" date="6月29日"></group-card> 
		</div>
	</div>
</template>

<script>
import MHeader from './partials/header-partial'
import GroupCard from './../GroupCard'

export default {
  data() {
    return {
			groupList: [
				{
					title: '2016 国际体验设计大会',
					date: '6月29日',
					during: '10：00-16：00'
				},
				{
					title: '2016 国际体验设计大会',
					date: '6月29日',
					during: '10：00-16：00'					
				}
			],			
    }
  },
  components: {
		MHeader,
		GroupCard, 
  }
}
</script>