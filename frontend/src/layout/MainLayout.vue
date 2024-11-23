<template>
    <div class="page">
        <HeaderComponent />
        <router-view />
    </div>
</template>

<script>
import HeaderComponent from '@/components/HeaderComponent.vue';

export default {
    name: 'MainLayout',
    components: {
        HeaderComponent
    },
}
</script>