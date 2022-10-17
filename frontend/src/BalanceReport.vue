<script>
import { ref } from 'vue'
//import emitter from './main.js'
import {useEnvironmentStore} from './main.js'
export default {
	props: ['balancereportrequestmodel','balancereportjson', 'zmitter'],


	methods: {
	showindex(i) {
//console.log(this.balancereportjson[0][i])
			return {
			  fullname: this.balancereportjson[0][i][0],
			  name: this.balancereportjson[0][i][1],
			  nesting: this.balancereportjson[0][i][2],
			  quantity: this.balancereportjson[0][i][3][0].aquantity.floatingPoint,
			}

		},
	wtf(i) {
		const retclass = 'pl-'+(12*(this.showindex(i).nesting))
		return retclass
	}
	
	},

	setup(props) {
		const environment = useEnvironmentStore()
		return {
			//zmitter: emitter,
			isAccountSelectorActive: ref(false),
			//accountnames: environment.accountnames.map( (n) => n.split(':')[0] )
			accountnames: ['Assets','Liabilities','Equity','Income','Expense'],
		}
	}


}
</script>




<template>
    <div class=" m-3  p-2 border border-black rounded-lg">

		<div>
			<div class="text-lg font-bold"> Balance Report:  </div>
			<div class="flex flex-row">
				<div class="m-1 p-1 bg-green-100 border border-black flex flex-row "> 
					<div v-for="(accountname,i) in balancereportrequestmodel.accountlist" class="bg-red-100 p-1 m-1 text-xs ">
						<span> {{accountname}}  </span>  <span class=" px-2 font-bold" @click="zmitter.emit('balancereportaccountnameclick', accountname)"> x </span>
					</div>
					<div class="text-sm  ml-4 my-1.5 bg-red-100 border border-black rounded-md"
						> 
						<div v-if=isAccountSelectorActive class="z-10 absolute bg-yellow-200 border border-black p-1"> 
							<div class="hover:bg-red-300 border border-black" @click="isAccountSelectorActive = !isAccountSelectorActive ">Cancel</div>
							<div v-for="(name, i) in accountnames" class="hover:bg-red-300 border border-black" 
									@click="isAccountSelectorActive = !isAccountSelectorActive; zmitter.emit('balancereportaddaccount', name)"
									>
							{{name}}
							</div>
						</div>
						<div v-else class="px-2 font-bold text-lg hover:bg-red-300" @click="this.isAccountSelectorActive = !this.isAccountSelectorActive " > + </div>
					</div>
				</div> 

				<div class="m-1 p-1 bg-green-100 border border-black "> {{balancereportrequestmodel.startdate}}    </div> 
				<div class="m-1 p-1 bg-green-100 border border-black "> {{balancereportrequestmodel.enddate}}      </div> 
				<div class="m-1 p-1 bg-green-100 border border-black "> {{balancereportrequestmodel.depth}}      </div> 
			</div>
		</div>

		<div class="flex flex-row">
			<div>
				<template v-for="(val,i) in balancereportjson[0]">
				<div v-if="showindex(i).nesting < balancereportrequestmodel.depth"  
						class="border-y border-black my-1 bg-blue-100 hover:bg-red-100 flex flex-row" 
						:class="showindex(i).nesting == 0 ? [ 'bg-blue-400', 'mt-8' ] : ['']">

					<div @click="zmitter.emit('accountnameclick', showindex(i).fullname)"   
						:class="['font-bold']" > 
						<span>	{{"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp".repeat(showindex(i).nesting)}} </span> 
						<span v-if="showindex(i).nesting == 0" class="mx-1" @click="zmitter.emit('balancereportnestingclick', showindex(i).name)" > V </span>
						<span class="mx-3" > {{showindex(i).name}} </span>
					</div>
					<div >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>
				</div>
				</template>
			</div>

			<div>
				<template v-for="(val,i) in balancereportjson[0]">
				<div v-if="showindex(i).nesting < balancereportrequestmodel.depth"  
					class="border-y border-black my-1 bg-blue-100" 
					:class="showindex(i).nesting == 0 ? [ 'bg-blue-400', 'mt-8' ] : ['']">

					<div class="w-48" :class="['font-bold' ]"> ${{showindex(i).quantity}}  </div>
				</div>
				</template>
			</div>
		</div>
    </div>
</template>
