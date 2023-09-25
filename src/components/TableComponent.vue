<template>
  <q-table
    :rows="parentRows"
    row-key="id"
    :columns="columns"
    dense
    separator="cell"
  >
    <template v-slot:body-cell="{ row }">
      <q-tr :props="rowProps(row)">
        <q-td v-for="col in columns" :key="col.name">
          {{ row[col.name] }}
        </q-td>
      </q-tr>
      <q-tr v-if="row.childrenVisible">
        <q-td :colspan="columns.length">
          <div class="child-table">
            <!-- Render child rows here -->
            <div v-for="child in row.children" :key="child.id" class="child-row">
              {{ child.name }}
            </div>
          </div>
        </q-td>
      </q-tr>
    </template>
  </q-table>
</template>

<script>
export default {
  props: {
    expand: Boolean, // Prop to control initial expansion
  },
  data() {
    return {
      parentRows: [
        {
          id: 1,
          name: 'Parent 1',
          children: [
            { id: 11, name: 'Child 1-1' },
            { id: 12, name: 'Child 1-2' },
          ],
          childrenVisible: this.expand, // Initial expansion state
        },
        // ... other parent rows ...
      ],
      columns: [
        { name: 'name', label: 'Name', align: 'left', field: 'name' },
        { name: 'age', label: 'age', align: 'left', field: 'age'  },
        { name: 'Accounts', label: 'account', align: 'left', field: 'account'  },
      ],
    };
  },
  methods: {
    rowProps(row) {
      return {
        props: {
          expandable: row.children && row.children.length > 0,
        },
        on: {
          click: () => {
            // Toggle expansion logic here
            if (row.children) {
              row.childrenVisible = !row.childrenVisible;
            }
          },
        },
      };
    },
  },
};
</script>

<style>
.child-table {
  margin-left: 20px; /* Indent child rows */
}
.child-row {
  padding: 5px;
}
</style>
