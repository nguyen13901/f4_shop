<template>
    <div id="contact-page">
        <contact-info></contact-info>
        <branch-info></branch-info>
    </div>
</template>

<script>
import ContactInfo from '../pages/contact_page/ContactInfo.vue';
import BranchInfo from '../pages/contact_page/BranchInfo.vue';

export default {
    components: {
        'ContactInfo': ContactInfo,
        'BranchInfo': BranchInfo,
    }
}
</script>
<style scoped>
@import "../css/contact.css";
</style>