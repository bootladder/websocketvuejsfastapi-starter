<script>
import { ref } from 'vue'
import AccountRegister from './AccountRegister.vue'
import BalanceReport from './BalanceReport.vue'
import {useEnvironmentStore} from './main.js'

//import emitter from './main.js'
import mitt from 'mitt'
//export default emitter
//export default {
//	emitter:zemitter
//}

const backendhosturl = 'http://localhost:6080' 


export default {
	props: {envkey:String},
	components: {
		AccountRegister,
		BalanceReport
	},
	setup (props) {
		const environment = useEnvironmentStore()
		console.log("WATT")
		console.log(props.envkey)
		const emitter = mitt()
		return {env: environment[props.envkey], zmitter: emitter}
	},

	methods: {},

  mounted() {

	this.zmitter.on('foo', e => console.log('foo', e) );
	this.zmitter.on('bar', e => {this.env.clickhistory.push(e); this.env.clickhistory = this.env.clickhistory.slice(-10) });
	this.zmitter.on('closeaccountregister', acct => { 
		this.env.clickhistory.push(acct.accountname) 
		this.env.tempregisters.forEach( (t,i) => {
			if(t == acct){ this.env.tempregisters.splice(i,1) }
		})
	})

	this.zmitter.on('balancereportaddaccount', name => {
		console.log("ADD ACCOUNT " + name) ; 
		this.env.balancereportrequestmodel.accountlist = this.env.balancereportrequestmodel.accountlist.filter( (n,i) => { return n !== name; } )
		this.env.balancereportrequestmodel.accountlist.push(name)

		fetch(backendhosturl+'/2022/balancereportjson', {
		  method: 'POST',
		  headers: { 'Content-Type': 'application/json', },
		  body: JSON.stringify(this.env.balancereportrequestmodel),
		})
		  .then((response) => response.json()).then((data) => {this.env.balancereportjson= data});
	})
	this.zmitter.on('balancereportnestingclick', name => {console.log("YASYAYJKL") ; })

	this.zmitter.on('accountnameclick', name => {

		const newaccountregister = {
			accountname : name,
			startdate: '2022-01-01',
			enddate: '2023-01-01',
			data: {},
		};

			fetch(backendhosturl + '/2022/accountprintjson', {
			  method: 'POST',
			  headers: { 'Content-Type': 'application/json', },
			  body: JSON.stringify(newaccountregister),
			})
			  .then((response) => response.json()).then((data) => {newaccountregister.data = data; return newaccountregister})

		.then( (d) => {
			this.env.tempregisters.unshift(newaccountregister)	
		})

		this.env.clickhistory.push(name)
	})

	this.zmitter.on('balancereportaccountnameclick', name => {
		//console.log("SLDKTGJS" + name)
		this.env.balancereportrequestmodel.accountlist = this.env.balancereportrequestmodel.accountlist.filter( (n,i) => { return n !== name; } )

		fetch(backendhosturl + '/2022/balancereportjson', {
		  method: 'POST',
		  headers: { 'Content-Type': 'application/json', },
		  body: JSON.stringify(this.env.balancereportrequestmodel),
		})
		  .then((response) => response.json()).then((data) => {this.env.balancereportjson= data});
	})



	this.zmitter.emit('foo', { a: 'b' });
	this.zmitter.emit('bar', 'yay');


	fetch(backendhosturl + '/2022/balancereportjson', {
	  method: 'POST',
	  headers: { 'Content-Type': 'application/json', },
	  body: JSON.stringify(this.env.balancereportrequestmodel),
	})
	  .then((response) => response.json()).then((data) => {this.env.balancereportjson= data});




	this.env.tempregisters.forEach( (t) => {
			fetch(backendhosturl + '/2022/accountprintjson', {
			  method: 'POST',
			  headers: { 'Content-Type': 'application/json', },
			  body: JSON.stringify(t),
			})
			  .then((response) => response.json()).then((data) => {t.data = data});

		})


  }
}


</script>

<template>
  <div class="w-auto flex flex-col border border-black p-1 m-1 rounded-lg bg-gray-100">

	<div @click="zmitter.emit('bar', 'fuckyeah')"> {{clickhistory}} </div>

	<div class="flex flex-row">
		<template v-if="this.env.balancereportjson[0]">
			<div>
			<BalanceReport :balancereportjson="this.env.balancereportjson" :balancereportrequestmodel="this.env.balancereportrequestmodel" :zmitter="zmitter"/>
			</div>
		</template>

		<template v-if="env.tempregisters.length > 0">
			<div class="flex flex-row flex-wrap">
				<AccountRegister :accountregister="env.tempregisters[0]" :zmitter="zmitter" />
			</div>
		</template>
	</div>


	<template v-if="env.tempregisters.length > 0">
		<div class="flex flex-row flex-wrap">
			<AccountRegister v-for="(t, i) in env.tempregisters" :accountregister="t" :zmitter="zmitter" />
		</div>
	</template>


  </div>

</template>

