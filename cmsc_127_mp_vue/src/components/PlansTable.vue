<template>
<table style="width: 100%;">
    <thead>
        <tr>
            <th>Book</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Total</th>
        </tr>
    </thead>
    <tbody>
        <tr
            v-for="item in order.items"
            v-bind:key="item.book.id"
        >
            <td class="book-title">{{ item.book.title }}</td>
            <td>${{ item.book.price }}</td>
            <td>{{ item.quantity }}</td>
            <td>${{ getItemTotal(item).toFixed(2) }}</td>
        </tr>
    </tbody>
</table>
</template>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  background: #34495e;
  color: #f3f3f3;
}

td, th {
  padding: 8px;
  text-align: left;
}
</style>