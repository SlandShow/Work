<template>
    <div class="message">
        <b-card class="mb-2">
        <p class="card-text">{{data.text}}</p>
        <p>{{data.msg_date}}</p>
            <b-button @click="readed">Прочитано</b-button>
        </b-card>
    </div>
</template>

<script>
    // import axios from 'axios'
    export default {
        name: 'message',
        data () {
            return {
                data: {},
            }
        },
        methods: {
            readed: function() {
                console.log('Message readed')
                // FIXME:
                // axios.call('api/mark_read?id={}')
                // this.data.readed = true
            }
        }
    }
</script>

<style scoped>

</style>