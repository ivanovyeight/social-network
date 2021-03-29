<template>
  <v-container>
    <v-card class="mb-2">
      <v-container class="mb-2">
        <div id="card-element" class="mb-2"></div>
        <!-- Elements will create input elements here -->
        <v-btn block @click="addPaymentMethod()">
          Add Card
        </v-btn>
      </v-container>

      <v-container  v-if="paymentMethods.length > 0">
        <v-row>
          <v-col
            cols="12"
            md="6"
            class="col-md-6 text-center"
            v-for="(card, index) in paymentMethods"
            :key="card.id"
          >
            <v-card outlined>
              <v-btn text disabled>
                {{
                  `${card["card"]["brand"]} Valid until: ${card["card"]["exp_month"]}/${card["card"]["exp_year"]}. Last 4: ${card["card"]["last4"]}`
                }}
              </v-btn>

              <v-btn text plain @click="deletePaymentMethod(card.id, index)"
                >Remove Card</v-btn
              >
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
    <v-btn block class="mb-2" @click="getSubscriptionPlans()"
      >Subscribe To Premium</v-btn
    >

    <v-stepper
      v-model="subscriptionStep"
      v-if="subscribeToPremiumModeActive == true"
    >
      <v-stepper-header>
        <v-stepper-step :complete="subscriptionStep > 1" step="1">
          Select Plan
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step :complete="subscriptionStep > 2" step="2">
          Select Payment Method
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="3">
          Confirm
        </v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <span v-for="plan in plans" :key="plan.id">
            <v-card
              rounded-lg
              @click="selectedPlan = plan.id"
              :class="selectedPlan == plan.id ? 'indigo darken-1' : ''"
            >
              <v-container class="my-2">
                {{
                  `${plan["nickname"]}: ${plan["unit_amount"] / 100}$ per ${
                    plan["recurring"]["interval"]
                  }`
                }}
              </v-container>
            </v-card>
          </span>

          <v-btn
            block
            class="my-2"
            :disabled="!selectedPlan"
            @click="subscriptionStep = 2"
          >
            Continue
          </v-btn>
        </v-stepper-content>

        <v-stepper-content step="2">
          <v-card
            :class="selectedPaymentMethod == card.id ? 'indigo darken-3' : ''"
            @click="selectedPaymentMethod = card.id"
            v-for="card in paymentMethods"
            :key="card.id"
          >
            <v-container class="my-2">
              {{
                `${card["card"]["brand"]} Valid until: ${card["card"]["exp_month"]}/${card["card"]["exp_year"]}. Last 4: ${card["card"]["last4"]}`
              }}
            </v-container>
          </v-card>

          <v-btn
            block
            class="my-2"
            :disabled="!selectedPaymentMethod"
            @click="subscriptionStep = 3"
          >
            Continue
          </v-btn>

          <v-btn @click="subscriptionStep = 1" block>
            Back
          </v-btn>
        </v-stepper-content>

        <v-stepper-content step="3">
          <v-btn block class="mt-2" @click="createSubscription()">
            Subscribe
          </v-btn>

          <v-btn @click="subscriptionStep = 2" block class="mt-2">
            Back
          </v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </v-container>
</template>

<script>
import http from "../plugins/http";
export default {
  components: {},
  data() {
    return {
      paymentMethods: [],
      stripe: "",
      card: "",
      plans: [],
      selectedPlan: "",
      selectedPaymentMethod: "",
      subscriptionStep: 1,
      subscribeToPremiumModeActive: false
    };
  },
  mounted() {
    this.stripe = window.Stripe(
      "pk_test_51FnL8pBruBQCsvNcvDTG9cqhAHYAdCkWneSXGhdCmdCsjfF4cjupkTVyz2QIajxtzFJCYEK03gKCLsysSJ3eP9Pn00dTSmwnjl"
    );
    let elements = this.stripe.elements();
    this.card = elements.create("card");
    this.card.mount("#card-element");
    this.getPaymentMethods();
  },
  methods: {
    getPaymentMethods() {
      http
        .get("http://localhost:8000/payments/payment-methods/")
        .then(response => (this.paymentMethods = response.data.data));
    },
    addPaymentMethod() {
      http
        .get("http://localhost:8000/payments/payment-methods/setup-token/")
        .then(response => {
          let setupIntentSecret = response.data;

          this.stripe.confirmCardSetup(setupIntentSecret, {
            payment_method: {
              card: this.card,
              billing_details: {
                name: "Test User"
              }
            }
          });
          // .then(this.card.clear());
        })
        .then(
          setTimeout(() => {
            this.getPaymentMethods();
          }, 5000)
        );
    },
    deletePaymentMethod(card, index) {
      let body = {
        payment_method_id: card
      };

      http.post("http://localhost:8000/payments/payment-methods/delete/", body);
      this.paymentMethods.splice(index, 1);
    },
    getSubscriptionPlans() {
      this.subscribeToPremiumModeActive = !this.subscribeToPremiumModeActive;
      http
        .get("http://localhost:8000/payments/subscriptions/")
        .then(response => (this.plans = response.data.data));
    },
    createSubscription() {
      let body = {
        price: this.selectedPlan,
        default_payment_method: this.selectedPaymentMethod
      };

      http.post("http://localhost:8000/payments/subscriptions/create/", body);
    }
  },
  computed: {}
};
</script>
