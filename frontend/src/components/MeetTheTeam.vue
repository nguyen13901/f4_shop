<template>
<div id="meet-the-team">
    <our-team></our-team>
</div>
</template>
<script>
import OurTeam from "../pages/meet_the_team/OurTeam.vue";
export default {
    components: {
        "OurTeam": OurTeam,
    }
}
</script>
<style scoped>
@import "../css/meet-the-team.css";
</style>