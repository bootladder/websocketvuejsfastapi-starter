<script>
import { ref } from 'vue'

var host = window.location.host; 
const hostwithoutport = host.split(':')[0]
const backendhosturlwebsocket = 'ws://'+hostwithoutport+':7080/ws'


export default {
	setup () {
		return {
			poop: ref("blah")
		}
	},

  mounted() {

    console.log("Starting connection to WebSocket Server")
    this.connection = new WebSocket(backendhosturlwebsocket)

    this.connection.onmessage = function(event) {
      console.log("HURR");
      console.log(event);
      this.poop = event
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
	{{poop}}
	</div>
</template>

