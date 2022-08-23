<template>
	<div class="app">
		<header-vue></header-vue>
		<main>
			<router-view></router-view>
		</main>
		<footer-vue></footer-vue>
	</div>
</template>

<script>
import HeaderVue from './components/HeaderVue.vue';
import FooterVue from './components/FooterVue.vue';

export default {
	name: "App",
	components: {
		'header-vue': HeaderVue,
		'footer-vue': FooterVue,
	},
};
</script>

<style>
@import "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css";
@import "css/reset.css";
</style>
