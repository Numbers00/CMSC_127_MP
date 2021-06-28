<template>
  <div @click="$router.push({path: `/cards/${user.username}/${card.get_absolute_url}/` })" class="wrapper column is-3 position-relative" style="top: 45px;">
    <div class="box" style="border-radius: 10px;">
      <figure class="image mb-4">
        <img :src="card.image" id="card-img" style="border-radius: 10px 10px 0 0;" />
      </figure>

      <h3 class="is-size-4">{{ card.name }}</h3>
      <p class="is-size-6 has-text-grey">{{ card.is_marked ? 'Marked' : 'Unmarked' }}</p>

    </div>
  </div>
</template>

<script>
export default {
  name: "CardBox",
  props: {
    card: Object,
    user: Object
  },
  methods: {
    
  }
};
</script>

<style scoped>
.wrapper {
  margin-right: -124px;
}
.wrapper:hover {
    cursor: pointer;
}
.box {
  max-width: 160px;
  width: 160px;
  background-color: #5cb85c;
  text-align: center;
  color: white;
}
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
#card-img {
  max-width: 200px;
  width: 200px;
  max-height: 200px;
  height: 200px;
}
.button {
  width: 90%;
}
</style>
