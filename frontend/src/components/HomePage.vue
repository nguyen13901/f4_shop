<template>
    <div id="home">
        <decorate-home></decorate-home>
        <product-home></product-home>
        <introduce-home></introduce-home>
        <shop-info></shop-info>
        <contact-mail></contact-mail>
    </div>
</template>

<script>
import DecorateHome from '../pages/home_page/DecorateHome.vue'
import IntroduceHome from '../pages/home_page/IntroduceHome.vue';
import ProductHome from '../pages/home_page/ProductHome.vue';
import ShopInfo from '../pages/home_page/ShopInfo.vue';
import ContactMail from '../pages/home_page/ContactMail.vue';

export default {
    components: {
        "DecorateHome": DecorateHome, 
        "IntroduceHome": IntroduceHome, 
        "ProductHome": ProductHome, 
        "ShopInfo": ShopInfo,
        "ContactMail": ContactMail,
    },
    data() {
        return {
        }
    }
}
</script>
<style scoped>
@import "../css/home.css";
</style>