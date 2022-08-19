<template>
    <div class="products-wrapper">
        <div class="btn-product">
            <button class="prev-btn" @click="moveProducts(-1)">
                <ion-icon name="chevron-back-outline"></ion-icon>
            </button>
        </div>
        <div class="product-container">
            <div class="product" v-for="product in current_products" :key="product">
                <div class="product-info">
                    <div class="product-view">
                        <div class="product-img">
                            <img :src="product.get_image" alt="backpack">
                        </div>
                        <div class="view-product-btn"><button>Quick View</button></div>
                    </div>
                    <div class="product-name">{{ product.name }}</div>
                    <div class="product-price">{{ product.price }} $</div>
                </div>
            </div>
        </div>
        <div class="btn-product" @click="moveProducts(1)">
            <button class="next-btn">
                <ion-icon name="chevron-forward-outline"></ion-icon>
            </button>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    data() {
        return {
            current_products: [],
            products: [],
            current: 0,
        }
    },
    components: {

    },
    mounted() {
        return this.getProducts();
    },
    methods: {
        getProducts() {
            axios
                .get('api/v1/products/')
                .then(response => {
                    this.products = response.data;
                    this.current_products = this.products.slice(this.current, (this.current + 4));
                })
                .catch(error => {
                    console.log(error)
                });

        },
        moveProducts(val) {
            this.current = this.current + val;
            if ((this.current + 4) > this.products.length) {
                this.current = this.products.length - 4;
            }
            if (this.current < 0) {
                this.current = 0;
            }
            this.getProducts();
        }
    }
}
</script>
<style>
</style>