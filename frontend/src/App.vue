<script>
import { ref } from 'vue'

var host = window.location.host; 
const hostwithoutport = host.split(':')[0]
const backendhosturlwebsocket = 'ws://'+hostwithoutport+':7080/ws'


export default {
	setup () {
        const datamodel = ref({"blah":"more"})
        const connection = null
		return {
				datamodel,
				connection,
		}
	},

  mounted() {

    console.log("Starting connection to WebSocket Server")
    this.connection = new WebSocket(backendhosturlwebsocket)

    this.connection.onmessage = (event) => {
      console.log(event);
      this.datamodel = event.data
    }

    this.connection.onopen = function(event) {
      console.log(event)
      console.log("Successfully connected to the echo websocket server...")
    }

  }
}


</script>

<template>
    <div class="border border-black text-center font-bold bg-orange-300 rounded-lg"> Hello Websocket </div>
	<div class="flex flex-row m-2 p-2">
        <pre>{{datamodel}}</pre>
	</div>
</template>

