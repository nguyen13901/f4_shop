<template>
    <div id="home">
        <decorate-home></decorate-home>
        <product-home></product-home>
        <introduce-home></introduce-home>
    </div>
</template>

<script>
import DecorateHome from '../pages/homepage/DecorateHome.vue'
import IntroduceHome from '../pages/homepage/IntroduceHome.vue';
import ProductHome from '../pages/homepage/ProductHome.vue';
export default {
    components: {
        "DecorateHome": DecorateHome, 
        "IntroduceHome": IntroduceHome, 
        "ProductHome": ProductHome, 
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