<template>

    <div class="navbar">
            <div class="name">
                <h2>Расписание</h2>
            </div>
            <p>{{ time }}</p>

            <div class="btns">

            </div>
    </div>

</template>

<script>

export default {
    data() {
        return {
            time: '',
            date: new Date(),
    }
},
    methods: {
        async updateTime() {
            this.time = this.date.getHours().toString() + ":" + this.date.getMinutes().toString();
        }
    },
    mounted() {
        this.updateTime();
    },
}
</script>

<style scoped>
.navbar {
    height: 50px;
    background-color: rgb(44, 44, 44);
    box-shadow: 2px 2px 4px #808080;
    display: flex;
    color: aliceblue;
    align-items: center;
    padding: 0 15px;
    justify-content: space-between;

}

</style>