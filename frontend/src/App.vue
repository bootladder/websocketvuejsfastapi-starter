<script>
import { ref } from 'vue'

var host = window.location.host; 
const hostwithoutport = host.split(':')[0]
const backendhosturl = 'http://'+hostwithoutport+':7080'
const backendhosturlwebsocket = 'ws://'+hostwithoutport+':7080/ws'


export default {
	components: {
	},
	setup () {
		return {
			poop: ref("blah")
		}
	},
	methods: {
	},


  mounted() {

    console.log("Starting connection to WebSocket Server")
    this.connection = new WebSocket(backendhosturlwebsocket)

    this.connection.onmessage = function(event) {
      console.log("HURR");
      console.log(event);
    }

    this.connection.onopen = function(event) {
      console.log(event)
      console.log("Successfully connected to the echo websocket server...")
    }

//
//
//
//
//		console.log(backendhosturl + '/getmodel')
//		fetch(backendhosturl + '/getmodel', {
//		  method: 'POST',
//		})
//		  .then((response) => response.json())
//			.then((data) => {this.poop = data });



  }
}


</script>

<template>
    <div class="border border-black text-center font-bold bg-orange-300 rounded-lg"> Rolodex Yep </div>
	<div class="flex flex-row m-2 p-2">
	{{poop}}
	</div>
</template>

