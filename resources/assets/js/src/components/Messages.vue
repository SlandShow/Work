<template>
    <div class="messages">
        <message 
          v-for='message in messages'
          v-bind:key="message.id"
        ></message>
    </div>
</template>

<script>
import axios from 'axios'
import Message from './Message'
    export default {
        name: 'messages',
        data () {
            return {
                messages: [1],
                data: {}
            }
        },
        mounted () {
            this.get_messages()
        },
        methods: {
            // FIXME:
            get_messages: function(){
                this.intervalid1 = setInterval(() => {
                    console.log('get')
                    this.messages.push('3')
                    axios.get('api/mark_read?id={}')
                      .then((responce) => {
                      this.data = responce.data
                      })
                      .catch((error) => {
                      console.log(error)
                    })
                }, 10000)
            }
        },
        components: {
            Message
        } 
    }
</script>

<style scoped>

</style>