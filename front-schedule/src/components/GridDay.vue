<template>
<div class="container">
    <div v-for="s in schedule" @click="showTime(s)">
        <my-button
            style="
                width: 97%;
                margin-bottom: .1rem;
                text-align: left;
            "
        >
        <div class="lol">
            <span>{{ s.name }}</span>
            <div class="time">
                <p >{{ s.time1 }}</p>
                <p >{{ s.time2 }}</p>
            </div>
        </div>
        </my-button>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            time1: Number,
            finalTime: String
        }
    },
    props: {
        schedule: {
            type: Array,
            required: true,
        }

    },
    methods: {
        showTime(s) {
            this.time1 = Date.parse('2011-04-23T' + s.time1 + ':00')
            console.log(this.time1)
            this.finalTime = Date.now() - this.time1
            window.alert("До начала занятия: " + new Date(this.finalTime).getHours() + ' часа');    
        }
    },
}
</script>

<style scoped>
.lol {
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.container {
    align-content: center;
}
.time {
    font-size: medium;
}
</style>