<template>
  <div class="q-pa-md">
    <q-table
      hide-bottom
      separator="cell"
      dense
      :rows="rows"
      :columns="columns"
      row-key="id"
      style="border-radius: 0"
    >
      <template v-slot:header="props">
        <q-tr :props="props">
          <q-th
            v-for="col in props.cols"
            :key="col.name"
            :props="props"
            class="bg-grey-4"
            style="font-size: 0.5vw; font-weight: Bold"
          >
            <q-btn class="header_button">{{ col.label }}</q-btn>
          </q-th>
        </q-tr>
      </template>

      <template v-slot:body="props">
        <q-tr :props="props">
          <q-td v-for="col in props.cols" :key="col.name" :props="props">
            <!-- adding expandable button to H/M/L rows and rest keep as it is -->
            <q-btn v-if="col.value === 'HIGH'  || col.value === 'MEDIUM' || col.value === 'LOW' " class="parent_button" >
              <div class="expandable-btn">
                <q-btn                  
                  color="black"
                  class="header_row"
                  round
                  dense
                  @click="
                    props.expand = !props.expand;
                    loadInnerRow(props.row, props);
                  "
                  :icon="props.expand ? 'remove' : 'add'"
                />{{ col.value }}
              </div>
            </q-btn>
            <q-btn v-else-if="col.name === '#Orgs'" @click="selectTier(props.row.Tier.charAt(0))" class="parent_button">
              {{ col.value.toLocaleString("en-US") }}
            </q-btn>
            <q-btn v-else class="parent_button">
              {{ col.value.toLocaleString("en-US") }}
            </q-btn>
          </q-td>
        </q-tr>

        <!-- On expanding props  -->
        <q-tr v-show="props.expand" v-if="props.row.sub" :props="props">
          <!-- <pre>{{props}}</pre>           -->
          <!-- <template v-if= "props.row.sub">           -->
          <!-- Adding fields in inner row -->
          <q-td
            ><div class="inner_button">
              {{ props.row.sub[0].toLocaleString("en-IN") }}
            </div>
          </q-td>
          <q-td
            ><div
              class="inner_button styled-td-yellow"
              :style="{
                width: (props.row.sub[1] / props.row.orgs) * 100 + '%',
              }"
              style="background-color: #fff2cc"
              @click="selectTier(props.row.sub[0])"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub[1] / props.row.orgs) * 100 + '%',
              }"
            >
              {{ props.row.sub[1].toLocaleString("en-IN") }}
            </div>
          </q-td>
          <q-td
            ><div
              class="inner_button styled-td-grey"
              :style="{
                width: (props.row.sub[2] / props.row.accounts) * 100 + '%',
              }"
              style="background-color: #ededed"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub[2] / props.row.accounts) * 100 + '%',
              }"
            >
              {{ props.row.sub[2].toLocaleString("en-IN") }}
            </div>
          </q-td>
          <q-td
            ><div
              class="inner_button styled-td-grey"
              :style="{
                width: (props.row.sub[3] / props.row.hcps) * 100 + '%',
              }"
              style="background-color: #ededed"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub[3] / props.row.hcps) * 100 + '%',
              }"
            >
              {{ props.row.sub[3].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td
            ><div
              class="inner_button styled-td-grey"
              :style="{
                width: (props.row.sub[4] / props.row.sales) * 100 + '%',
              }"
              style="background-color: #ededed"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub[4] / props.row.sales) * 100 + '%',
              }"
            >
              {{ props.row.sub[4].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td
            ><div class="inner_button">{{ props.row.sub[5] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub[6] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub[7] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub[8] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub[9] }}</div></q-td
          >

        </q-tr>

        <q-tr v-show="props.expand" v-if="props.row.sub2" :props="props">
          <!-- <template v-if= "props.row.sub2">          -->

          <q-td
            ><div class="inner_button">
              {{ props.row.sub2[0].toLocaleString("en-US") }}
            </div></q-td
          >
          <q-td
            ><div
              class="inner_button styled-td-yellow"
              :style="{
                width: (props.row.sub2[1] / props.row.orgs) * 100 + '%',
              }"
              @click="selectTier(props.row.sub2[0])"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub2[1] / props.row.orgs) * 100 + '%',
              }"
            >
              {{ props.row.sub2[1].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td style="text-align: right"
            ><div
              class="inner_button styled-td-grey"
              :style="{
                width: (props.row.sub2[2] / props.row.accounts) * 100 + '%',
              }"
              style="background-color: #ededed"
            ></div>

            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub2[2] / props.row.accounts) * 100 + '%',
              }"
            >
              {{ props.row.sub2[2].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td
            ><div
              class="inner_button styled-td-grey"
              :style="{
                width: (props.row.sub2[3] / props.row.hcps) * 100 + '%',
              }"
              style="background-color: #ededed"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub2[3] / props.row.hcps) * 100 + '%',
              }"
            >
              {{ props.row.sub2[3].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td
            ><div
              class="inner_button styled-td-grey"
              :style="{
                width: (props.row.sub2[4] / props.row.sales) * 100 + '%',
              }"
              style="background-color: #ededed"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub2[4] / props.row.sales) * 100 + '%',
              }"
            >
              {{ props.row.sub2[4].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td
            ><div class="inner_button">{{ props.row.sub2[5] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub2[6] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub2[7] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub2[8] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub2[9] }}</div></q-td
          >

          <!-- </template>    -->
        </q-tr>

        <q-tr v-show="props.expand" v-if="props.row.sub3" :props="props">
          <!-- <template v-if= "props.row.sub3">          -->
          <!-- {{props.expand=inner_row}} -->
          <q-td
            ><div class="inner_button">
              {{ props.row.sub3[0].toLocaleString("en-US") }}
            </div></q-td
          >
          <q-td
            ><div
              class="inner_button styled-td-yellow"
              :style="{
                width: (props.row.sub3[1] / props.row.orgs) * 100 + '%',
              }"
              style="background-color: #fff2cc"
              @click="selectTier(props.row.sub3[0])"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub3[1] / props.row.orgs) * 100 + '%',
              }"
            >
              {{ props.row.sub3[1].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td
            ><div
              class="inner_button styled-td-grey"
              :style="{
                width: (props.row.sub3[2] / props.row.accounts) * 100 + '%',
              }"
              style="background-color: #ededed"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub3[2] / props.row.accounts) * 100 + '%',
              }"
            >
              {{ props.row.sub3[2].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td
            ><div
              class="inner_button styled-td-grey"
              :style="{
                width: (props.row.sub3[3] / props.row.hcps) * 100 + '%',
              }"
              style="background-color: #ededed"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub3[3] / props.row.hcps) * 100 + '%',
              }"
            >
              {{ props.row.sub3[3].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td
            ><div
              class="inner_button styled-td-grey"
              :style="{
                width: (props.row.sub3[4] / props.row.sales) * 100 + '%',
              }"
              style="background-color: #ededed"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub3[4] / props.row.sales) * 100 + '%',
              }"
            >
              {{ props.row.sub3[4].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td
            ><div class="inner_button">{{ props.row.sub3[5] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub3[6] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub3[7] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub3[8] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub3[9] }}</div></q-td
          >

          <!-- </template>    -->
        </q-tr>

        <q-tr v-show="props.expand" v-if="props.row.sub4" :props="props">
          <!-- <template v-if= "props.row.sub4">          -->
          <q-td
            ><div class="inner_button">
              {{ props.row.sub4[0].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td
            ><div
              class="inner_button styled-td-yellow"
              :style="{
                width: (props.row.sub4[1] / props.row.orgs) * 100 + '%',
              }"
              style="background-color: #fff2cc"
              @click="selectTier(props.row.sub4[0])"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub4[1] / props.row.orgs) * 100 + '%',
              }"
            >
              {{ props.row.sub4[1].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td
            ><div
              class="inner_button styled-td-grey"
              :style="{
                width: (props.row.sub4[2] / props.row.accounts) * 100 + '%',
              }"
              style="background-color: #ededed"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub4[2] / props.row.accounts) * 100 + '%',
              }"
            >
              {{ props.row.sub4[2].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td
            ><div
              class="inner_button styled-td-grey"
              :style="{
                width: (props.row.sub4[3] / props.row.hcps) * 100 + '%',
              }"
              style="background-color: #ededed"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub4[3] / props.row.hcps) * 100 + '%',
              }"
            >
              {{ props.row.sub4[3].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td
            ><div
              class="inner_button styled-td-grey"
              :style="{
                width: (props.row.sub4[4] / props.row.sales) * 100 + '%',
              }"
              style="background-color: #ededed"
            ></div>
            <div
              class="value"
              :style="{
                width: 100 - (props.row.sub4[4] / props.row.sales) * 100 + '%',
              }"
            >
              {{ props.row.sub4[4].toLocaleString("en-US") }}
            </div>
          </q-td>
          <q-td
            ><div class="inner_button">{{ props.row.sub4[5] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub4[6] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub4[7] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub4[8] }}</div></q-td
          >
          <q-td
            ><div class="inner_button">{{ props.row.sub4[9] }}</div></q-td
          >

          <!-- </template>    -->
        </q-tr>
      </template>
    </q-table>
  </div>
</template>

<script>
// import axios from 'axios'
import { ref } from "vue";

const columns = [
  { name: "Tier", label: "Tier", align: "left", field: "Tier" },
  {
    name: "#Orgs",
    align: "center",
    label: "#Orgs",
    field: "orgs",
    classes: "myOrg",
  },
  {
    name: "#Accounts",
    label: "#Accounts",
    field: "accounts",
    classes: "myAcc",
  },
  { name: "#HCPs", label: "#HCPs", field: "hcps", classes: "myHcp" },
  {
    name: "Product sales",
    label: "Product sales",
    field: "sales",
    classes: "mySales",
  },
  {
    name: "%Potential",
    label: "%Potential",
    field: "potential",
    format: (val) => `${val}%`,
  },
  {
    name: "%Product A sales",
    label: "%Product A sales",
    field: "product_a",
    format: (val) => `${val}%`,
  },
  {
    name: "%Product B sales",
    label: "%Product B sales",
    field: "product_b",
    format: (val) => `${val}%`,
  },
  {
    name: "%Diagnosed Patients",
    label: "%Diagnosed Patients",
    field: "diagnosis",
    format: (val) => `${val}%`,
  },
  {
    name: "%Treated Patients",
    label: "%Treated Patients",
    field: "treated",
    format: (val) => `${val}%`,
  },
];

//numbers below are only dummby values
const rows = ref([
  {
    id: "1",
    Tier: "HIGH",
    name: "nishant",
    orgs: 45,
    accounts: 150,
    hcps: 340,
    sales: 15635,
    potential: "",
    product_a: "",
    product_b: "",
    diagnosis: "",
    treated: ""

    //sub: ["D10", 40, 100, 100, 9000, "29%"],
    // sub2:['D9',45,110,150,2000,'34%'],
    // sub3:['D8',45,12,200,3000,'20%']
  },
  {
    id: "2",
    Tier: "MEDIUM",
    name: "nishant",
    orgs: 185,
    accounts: 548,
    hcps: 870,
    sales: 6750,
    potential: "",
    product_a: "",
    product_b: "",
    diagnosis: "",
    treated: "",
    // sub:['D7',100,110,600,5000,'10%'],
    // sub2:['D6',120,150,500,2000,'64%'],
    // sub3:['D5',120,150,500,2000,'64%']
  },
  {
    id: "3",
    Tier: "LOW",
    name: "nishant",
    orgs: 185,
    accounts: 548,
    hcps: 870,
    sales: 6750,
    potential: "",
    product_a: "",
    product_b: "",
    diagnosis: "",
    treated: "",
    // sub:['D4',100,110,600,5000,'10%'],
    // sub2:['D3',120,150,500,2000,'64%'],
    // sub3:['D2',120,150,500,2000,'64%'],
    // sub4:['D1',120,150,500,2000,'64%']
  },
  {
    id: "4",
    Tier: "-",
    name: "nishant",
    orgs: 185,
    accounts: 548,
    hcps: 870,
    sales: 6750,
    potential: "",
    product_a: "",
    product_b: "",
    diagnosis: "",
    treated: "",
  },
  {
    id: "5",
    Tier: "Total",
    name: "nishant",
    orgs: 185,
    accounts: 548,
    hcps: 870,
    sales: 6750,
    potential: "",
    product_a: "",
    product_b: "",
    diagnosis: "",
    treated: "",
  },
]);

const rowTier= ''

export default {
  props: ["stateFilter", "terrFilter", "isStateSelected"],
  
  setup() {
    return {
      columns: columns,
      rows: rows,
      rowTier:rowTier
      // rows:rows
    };
  },
  emits:["row-tier"],
  methods: {

    selectTier(Tier){
        this.rowTier= Tier
        if(this.rowTier =='T'){
          this.$emit('row-tier','Total')
        }
        else if(this.rowTier == '-'){
          this.$emit('row-tier','null')
        }
        else{
          this.$emit('row-tier',this.rowTier)
        }
    
    },


    onChangeLoadTable() {
      this.loadparentrow();
      let rows_tier_H = { Tier: "H" };
      let rows_tier_M = { Tier: "M" };
      let rows_tier_L = { Tier: "L" };
      let prop_pass = { expand: true };
      this.loadInnerRow(rows_tier_H, prop_pass);
      this.loadInnerRow(rows_tier_M, prop_pass);
      this.loadInnerRow(rows_tier_L, prop_pass);
    },

    loadInnerRow(rows, prop) {
  
      let path = "http://127.0.0.1:5000/table/decile/" + (rows.Tier).charAt(0);
      // console.log(path)
      fetch(path, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          state: this.stateFilter,
          terr: this.terrFilter,
          isstateselected: this.isStateSelected,
        }),
      })
        .then((response) => {
          if (response.ok) {
            return response.json();
          }
        })
        .then((data) => {
          console.log(data);
          // Insertion and deletion of rows
          if (rows.Tier.charAt(0) == "H") {
            if (prop.expand) {
              this.rows[0].sub = data.output[0];
              this.rows[0].sub2 = data.output[1];
              this.rows[0].sub3 = data.output[2];
            } else {
              delete this.rows[0].sub;
              delete this.rows[0].sub2;
              delete this.rows[0].sub3;
            }
          } else if (rows.Tier.charAt(0) == "M") {
            if (prop.expand) {
              this.rows[1].sub = data.output[0];
              this.rows[1].sub2 = data.output[1];
              this.rows[1].sub3 = data.output[2];
            } else {
              delete this.rows[1].sub;
              delete this.rows[1].sub2;
              delete this.rows[1].sub3;
            }
          } else if (rows.Tier.charAt(0) == "L") {
            if (prop.expand) {
              this.rows[2].sub = data.output[0];
              this.rows[2].sub2 = data.output[1];
              this.rows[2].sub3 = data.output[2];
              this.rows[2].sub4 = data.output[3];
            } else {
              delete this.rows[2].sub;
              delete this.rows[2].sub2;
              delete this.rows[2].sub3;
              delete this.rows[2].sub4;
            }
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },

    loadparentrow() {
      let path = "http://127.0.0.1:5000/table/tier";
      // console.log("Parent prop",this.$props)

      fetch(path, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          state: this.stateFilter,
          terr: this.terrFilter,
          isstateselected: this.isStateSelected,
        }),
      })
        .then((response) => {
          if (response.ok) {
            return response.json();
          }
        })
        .then((data) => {
          console.log(data);
          for (let i = 0; i < 5; i++) {
            this.rows[i].orgs = data.output[i][1];
            this.rows[i].accounts = data.output[i][2];
            this.rows[i].hcps = data.output[i][3];
            this.rows[i].sales = data.output[i][4];
            this.rows[i].potential = data.output[i][5];
            this.rows[i].product_a = data.output[i][6];
            this.rows[i].product_b = data.output[i][7];
            this.rows[i].diagnosis = data.output[i][8];
            this.rows[i].treated = data.output[i][9];
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },

  mounted() {
    this.loadparentrow();
  },

  watch: {
    // Checking for change in filter value
    stateFilter(newValue, oldValue) {
      if (JSON.stringify(newValue) != JSON.stringify(oldValue)) {
        console.log("state new value",newValue)
        this.onChangeLoadTable();
      }
    },

    terrFilter(newValue, oldValue) {
      if (!this.isStateSelected && JSON.stringify(newValue) != JSON.stringify(oldValue)) {
          console.log("Territory new value",newValue)
          this.onChangeLoadTable();
      }
    },
  },
};
</script>

<style scoped>
.q-td,td{
 
  text-align: center;
}
.header_row{
 
  font-size: 0.5vw;
}
h1 {
  font-size: 0.5vh;
}

.parent_button {
  width: 100%;
  padding: 0;
  margin: 0;
  font-size: 1.9vh;
  color: black;
  background-color: #b9e9fc;
}

.inner_button {
  width: 100%;
  padding: 0;
  margin: 0;
  border: 0.3vh;
  border-style: solid;
  border-color: lightgray;
  height: 100%;
  font-weight: bold;
  font-size: 1.8vh;

  align-items: center;
  justify-content: center;
  background-color: transparent;
}

.header_button {
  width: 100%;
  padding: 0;
  margin: 0;
  border-radius: 0;
  text-align: center;
  border: 0;
  height: 100%;
  font-weight: bold;
  font-size: 2vh;
  color: white;
  background-color: #00a3e0;
}
.expandable-btn {
  display: flex;
  width: 4vw;
  justify-content: space-around;
  height: 100%;
  align-items: center;
}
.q-table--dense .q-table td:first-child,
.q-table--dense .q-table td,
.q-table--dense .q-table td:last-child,
.q-table--dense .q-table th,
.q-table--dense .q-table th:first-child,
.q-table--dense .q-table th:last-child {
  padding: 0;
  margin: 0;
  border: 0;
}
.q-btn-item {
  display: flex;
  justify-content: center;
  align-items: center;
}

.myOrg button {
  background-color: #ffd966;
}
.myAcc button,
.myHcp button,
.mySales button {
  background-color: #ededed;
}
.value {
  display: inline-flex;
  align-items: center;
  justify-content: end;
  height: 100%;
  vertical-align: top;
  text-align: right;
  font-weight: 500;
  }
.styled-td-yellow,
.styled-td-grey {
  display: inline-block;
}
.styled-td-yellow {
  background-color: #fff2cc;
  cursor: pointer;
}


.styled-td-grey {
  background-color: #ededed;
}
</style>
