<template>
    <div id="home">
        <decorate-home></decorate-home>
        <product-home></product-home>
        <introduce-home></introduce-home>
        <shop-info></shop-info>
    </div>
</template>

<script>
import DecorateHome from '../pages/homepage/DecorateHome.vue'
import IntroduceHome from '../pages/homepage/IntroduceHome.vue';
import ProductHome from '../pages/homepage/ProductHome.vue';
import ShopInfo from '../pages/homepage/ShopInfo.vue';

export default {
    components: {
        "DecorateHome": DecorateHome, 
        "IntroduceHome": IntroduceHome, 
        "ProductHome": ProductHome, 
        "ShopInfo": ShopInfo,
    },
    props: ['products'],
    data() {
        return {

        }
    }
}
</script>
<style scoped>
</style>