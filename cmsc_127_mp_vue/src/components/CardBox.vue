<template>
<div @click="$router.push({path: '' + card.get_absolute_url, append: false})" class="wrapper column is-3 position-relative" style="top: 20px;">
  <figure class="image">
    <img :src="card.image" id="card-img" />
  </figure>

  <div class="image-text">
    <p class="is-size-5"><b>{{ card.name }}</b></p>
  </div>
</div>
</template>

<script>

export default {
  name: "CardBox",
  props: {
    card: Object,
    myDetails: Object
  },
};
</script>

<style scoped>
.wrapper:hover {
  cursor: pointer;
}
.image {
  max-width: 240px;
  width: 240px;
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
  border-radius: 10px;
  position: relative;
  top: 50px;
  left: 20px;
}
.image-text {
  z-index: 10;
  position: absolute;
  color: white;
  text-align: left;
  overflow: hidden;
  top: 110px;
  left: 20px;
  min-width: 220px;
  width: 220px;
  min-height: 70px;
  height: 70px;
  max-height: 70px;
}
#card-img {
  max-width: 240px;
  width: 240px;
  max-height: 160px;
  height: 160px;
  border-radius: 10px;
}
.button {
  width: 90%;
}
</style>
