<template>
	<div class="wrapper">
		<h2 class="title">Our Team</h2>
		<p class="short-desc">True Talents</p>
		<div class="team">
			<div class="member-profile" v-for="account in current_accounts" :key="account">
				<div class="profile-img">
					<img :src="account.get_avatar" alt="person1" />
				</div>
				<h3 class="member-name">
					{{ account.first_name + " " + account.last_name }}
				</h3>
				<p class="member-role">Customer Service Representative</p>
			</div>
		</div>
	</div>
</template>
<script>
	import axios from "axios";
	export default {
		data() {
			return {
				accounts: {},
				current_accounts: {},
			};
		},
		methods: {
			getFullName(account) {
				return account.firstName + " " + account.lastName;
			},
			getAccounts() {
				axios
					.get("api/v1/accounts/")
					.then((response) => {
						this.accounts = response.data;
						this.current_accounts = this.accounts.slice(1, this.accounts.length);
					})
					.catch((error) => {
						console.log(error);
					});
			},
		},
		mounted() {
			return this.getAccounts();
		},
	};
</script>
<style scoped></style>