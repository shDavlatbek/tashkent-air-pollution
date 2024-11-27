<template>
  <teleport to="body">
    <div class="page page-center">
      <div class="container-tight py-4">
        <div class="empty">
          <div class="empty-header">500</div>
          <p class="empty-title">Xatolik yuz berdi</p>
          <p class="empty-subtitle text-secondary">
            Kechirasiz, lekin serverimizda ichki xatolik yuz berdi
          </p>
          <div class="empty-action">
            <router-link to="/" class="btn btn-primary">
              <!-- Download SVG icon from http://tabler-icons.io/i/arrow-left -->
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M5 12l14 0"></path>
                <path d="M5 12l6 6"></path>
                <path d="M5 12l6 -6"></path>
              </svg>
              Bosh sahifaga qaytish
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </teleport>
</template>

<script>
export default {
  name: 'ServerError',
}
</script>