<style scoped>
	.ui_card {
		float: left;
		display: inline-block;
		background: #FFFFFF;
		width: 20%;
		min-height: 150px;
		padding: 20px 20px 0 20px;
		margin: 10px 15px;
	}
	.ui_card_hd {
		width: 90%;
		font-size: 25px;
		color: black;
		margin-bottom: 10px
	}
	.ui_card_ft {
		color: #D7D5D3;
		border-top: 1px solid #D7D5D3;
		width: 50%;
		line-height: 1.2
	}
	
	.ui_card_add  {
	}
	p.add {
		font-size: 70px;
		text-align: center
	}
</style>

<template>
	<div class="ui_card">
		<template v-if="title !== ''">
			<div class="ui_card_hd">
				<p>{{title}}</p>
			</div>
			<div class="ui_card_ft">
				<p>{{date}}</p>
				<p>{{during}}</p>
			</div>
		</template>
		<template v-else>
			<div class="ui_card_add">
				<p class="add">+</p>
			</div>
		</template>
	</div>
</template>

<script>
export default {
	props: {
		title: {
			type: String,
			default: ''
		},
		date: {
			type: String,
			default: ''
		},
		during: {
			type: String,
			default: ''
		}
	}
}
</script>