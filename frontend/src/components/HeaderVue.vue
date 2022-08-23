<template>
    <header>
        <div id="dialog" v-if="viewProduct">
            <div class="dialog-wrapper">
                <span class="close" @click="closeDialog()">&times;</span>
                <div class="dialog-container">
                    <div class="dialog-product-img" :style="getImage()">
                    </div>
                    <div class="dialog-product-content">
                        <div class="dialog-product-name">{{ product.name }}</div>
                        <div class="dialog-product-price">{{ product.price }} $</div>
                        <div class="dialog-product-id">SKU: {{ product.id }}</div>
                        <div class="dialog-product-color">{{ product.color }}</div>
                        <div class="amount"><input type="number" value="1" max="20" min="1"></div>
                        <div class="add-btn">
                            <button>Add to cart</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="header-bar">
            <div class="header-title">Jin F4Shop</div>
        </div>
        <div class="header-container">
            <div class="nav-container">
                <div class="navigation">
                    <ul>
                        <li><a><router-link to="/">Home</router-link></a></li>
                        <li><a><router-link to="/about-us">About us</router-link></a></li>
                        <li><a href="#"><router-link to="/contact">Contact</router-link></a></li>
                        <li><a href="#"><router-link to="/meet-the-team">Meet the Team</router-link></a></li>
                        <li><a href="#"><router-link to="/FAQ">FAQ</router-link></a></li>
                        <li><a href="#"><router-link to="/support">Support</router-link></a></li>
                        <li><a href="#"><router-link to="/store-policies">Store Policies</router-link></a></li>
                        <li><a href="#"><router-link to="/testimonials">Testimonials</router-link></a></li>
                        <li><a href="#"><router-link to="/shop">Shop</router-link></a></li>
                    </ul>
                </div>
                <i class="fa fa-facebook"></i>
            </div>
        </div>
    </header>
</template>

<script>

export default {
    data() {
        return {
            product: {},
        }
    },
    computed: {
        viewProduct() {
            this.getProduct();
            return this.$store.state.isViewProduct;
        },
    },
    methods: {
        closeDialog() {
            this.$store.dispatch('cancelViewProduct');
        },
        getProduct() {
            this.product = this.$store.state.current_product;
        },
        getImage() {
            return {
                "background-image": "url(" + this.product.get_image + ")",
            };
        }
    },
}
</script>
<style scoped>
</style>