<template>
<!-- <h1>Nishant</h1> -->
   <div>
    <table>
      <thead>
        <tr>
          <th>Product Name</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td>
            {{ product.name }}
            <span class="expand-icon" @click="toggleRowExpansion(product.id)">
                {{
                    expandedRows.forEach(function(entry) {
                    console.log(entry);
                  })
                }}

              {{ isRowExpanded(product.id) ? '-' : '+' }}
            </span>
          </td>
          <td>{{ product.price }}</td>
          
_
        </tr>

        <tr v-if="expandedRows" >
            <span v-for="product in products" :key="product.id + '-details'">  
                <td colspan="2">
                    <div class="product-details">
                    
                    </div>
                </td>
            </span>   
        </tr>  

      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      products: [
        { id: 1, name: 'Product A', price: 10 },
        { id: 2, name: 'Product B', price: 20 },
        // Additional product data...
      ],
      expandedRows: [],
    };
  },
  methods: {
    toggleRowExpansion(rowId) {
      if (this.expandedRows.includes(rowId)) {
        this.expandedRows = this.expandedRows.filter((id) => id !== rowId);
      } else {
        this.expandedRows.push(rowId);
      }
    },
    isRowExpanded(rowId) {
      return this.expandedRows.includes(rowId);
    },
  },
};
</script>

<style>
.expand-icon {
  cursor: pointer;
  margin-left: 5px;
}
</style>