<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image mb-4">
                <img @click="!card.is_history ? $router.push({path: '' + card.get_absolute_url, append: false}) : $router.push({path: '/history/' + card.get_absolute_url, append: false})" :src="card.image" id='card-img'>
            </figure>

            <h3 class="is-size-4">{{ card.name }}</h3>
            <p class="is-size-6 has-text-grey">{{ !card.is_history ? 'Active' : 'Inactive' }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SearchCard',
    props: {
        card: Object
    }
}
</script>

<style scoped>
  .box {
    max-width: 200px;
    width: 200px;
    background-color: hsl(0, 0%, 21%);
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
</style>