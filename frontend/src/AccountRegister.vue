<script>
//import emitter from './main.js'
export default {
	props: ['accountregister', 'zmitter'],


	methods: {
	accountregistershowindex(i) {
			  //console.log(this.accountregister.data[1][i]);
//console.log(i)
//console.log(this.accountregister.data)
			return {
			  //date: this.accountregister.data[1][i][0],
			  //description: this.accountregister.data[1][i][2],
			  //quantity: this.accountregister.data[1][i][3].pamount[0].aquantity.floatingPoint,
			  //account: this.accountregister.data[1][i][3].paccount,
			  //balance: this.accountregister.data[1][i][4][0].aquantity.floatingPoint,


			  date: 			this.accountregister.data[i].tdate,
			  description: 		this.accountregister.data[i].tdescription,
			  comment:	 		this.accountregister.data[i].tcomment,
			  quantity: 		this.accountregister.data[i].tpostings[1].pamount[0].aquantity.floatingPoint,
			  account: 			this.accountregister.data[i].tpostings[0].paccount,
			  postingaccounts: 	this.accountregister.data[i].tpostings.map( (p) => p.paccount),
			  postingquantities:this.accountregister.data[i].tpostings.map( (p) => p.pamount[0].aquantity.floatingPoint),
			  postings:			this.accountregister.data[i].tpostings.map( (p) => {return { quantity: p.pamount[0].aquantity.floatingPoint, account: p.paccount }}),
			  balance: 		"nobal",

			}

		}
	},


	data() {
		return {
			//zmitter: emitter
		}
	}


}
</script>

<template>


	<div v-if="true">
	{{}}
	</div>
	<div v-if="false">
		<pre>{{accountregister.data[0].tcomment}}</pre>
		<pre>{{accountregister.data[0].tpostings[0].paccount}}</pre>
		<pre>{{accountregister.data[0].tpostings[1].paccount}}</pre>
		<pre>{{accountregister.data[0].tpostings[1].pamount[0].aquantity.floatingPoint}}</pre>
		<pre>{{accountregister.data[0].tcomment}} </pre>
		<pre>{{accountregister.data[0].tdate }} </pre>
		<pre>{{accountregister.data[0]}}</pre>
	</div>


	<div v-if="true" class="m-1 p-1 border-black border bg-gray-100 rounded-lg">
		<div class="bg-blue-100 flex flex-row justify-evenly">
			<div class="text-lg font-bold px-2 bg-yellow-100 "> {{accountregister.accountname}}</div>
			<div class="text-xs font-bold px-2 "> {{accountregister.startdate}}</div>
			<div class="text-xs font-bold px-2 "> {{accountregister.enddate}}</div>
			<div @click="zmitter.emit('closeaccountregister', accountregister)" class="text-xs font-bold px-2 border border-black bg-red-200"> X </div>
			 
		</div>
		<div>
		<div v-for="(v,i) in accountregister.data" class="border border-black p-2 rounded-lg bg-blue-50">
			<div class="flex flex-row bg-blue-100">
				<div>{{accountregistershowindex(i).date}}</div>
				<div class="ml-8">{{accountregistershowindex(i).description}}</div>
			</div>
			<pre class="my-2 ml-8">{{accountregistershowindex(i).comment.split('\n').filter( (l) => l!="").join("\n")}}</pre>
				<tr v-for="(posting,postingindex) in accountregistershowindex(i).postings"
					:class="postingindex==0? ['border-black','border-t' ] : []">
						<td class="break-words p-1 px-4 m-1 " :class="accountregister.accountname == posting.account? ['bg-blue-100']:[]"> {{posting.account}}      </td>   
						<td class="break-words p-1 px-4 m-1 font-bold text-green-800 "> {{ postingindex==0? '$'+posting.quantity : ""}}    </td>  
				</tr>
		</div>
		</div>
	</div>
</template>
