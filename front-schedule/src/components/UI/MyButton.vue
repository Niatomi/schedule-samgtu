<template>
    <button class="btn">
        <slot></slot>
    </button>
</template>

<script>
export default {
    name: 'my-button'
}
</script>

<style scoped>
.btn {
    z-index: 100;
    font-size: 1.2rem;
    min-width: 4rem;
    min-height: 2rem;
    top:50%;
    background-color: #42d392;
    color: #fff;
    border:none;
    align-items: center;
    border-radius: 10px;
    margin-left: .5rem;
}
.btn:active {
    top:50%;
    background-color:#42d392;
    color: #fff;
    border:none;
}
.btn:hover {
    top:50%;
    background-color: #647eff;
    color: #fff;
    border:none;
}
.btn:active {
    top:50%;
    background-color:#42d392;
    color: #fff;
    border:none;
}
</style>