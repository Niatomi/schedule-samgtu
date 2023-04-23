<template>
<div class="footer">
    <div class="author">
        Created by Niatomi
    </div>
</div>
</template>

<script>
export default {
    name: 'Footer'
}

</script>


<style>
.footer {
  position: fixed;
  left: 0;
  bottom: 0; 
  width: 100%;
  background: -webkit-linear-gradient(315deg,#42d392 25%,#647eff);
  color: white;
  text-align: center;
}

.author {
    margin-top: .5rem;
    margin-bottom: .5rem;
}
</style>
