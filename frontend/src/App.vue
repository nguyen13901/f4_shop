<template>
	<div class="app">
    <header>
		<div class="header-bar">
			<div class="header-title">Jin F4Shop</div>
		</div>
		<div class="header-container">
			<div class="nav-container">
				<div class="navigation">
					<ul>
						<li><a href="#">Home</a></li>
						<li><a href="#">About us</a></li>
						<li><a href="#">Contact</a></li>
						<li><a href="#">Meet the Team</a></li>
						<li><a href="#">FAQ</a></li>
						<li><a href="#">Support</a></li>
						<li><a href="#">Store Policies</a></li>
						<li><a href="#">Testimonials</a></li>
						<li><a href="#">Shop</a></li>
					</ul>
				</div>
				<i class="fa fa-facebook"></i>
			</div>
		</div>
	</header>
  <main>
	<div class="content-wrapper">
		<div class="content-container">
			<div class="img-introduce">
			</div>
			<div class="intro-container">
				<div class="intro-title">CHECK US OUT</div>
				<div class="intro-word">Save More</div>
			</div>
		</div>
	</div>
	<home-page :products="products"></home-page>
  </main>
  <footer>
	<div class="subscribe-form">
            <div class="form-title">Subscribe Form</div>
            <div class="form-sub">
                <input type="text" placeholder="e.g.email@gmail.com">
                <button class="join-btn"><span>Join</span></button>
            </div>
    </div>
	<div class="contact-info">
		<div class="contact-mail">nguyen13901@gmail.com</div>
		<div class="fb-icon"><i class="fa fa-facebook"></i></div>
		<div class="copyright">&copy;2022 by ClothesShop. Proudly created with Wix.com</div>
	</div>
  </footer>
</div>
</template>

<script>
import HomePageVue from './components/HomePage.vue';
export default {
	name: "App",
	components: {
		'home-page': HomePageVue
	},
	data() {
		return {
			products: [
				{name: "Banana", price: "20"},
				{name: "Apple", price: "60"},
				{name: "Watermelon", price: "10"},
				{name: "Strawberry", price: "100"}
			]
		}
	}
};
</script>

<style>
	@import "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css";
	@import "css/reset.css";
	@import "css/main.css";
</style>
