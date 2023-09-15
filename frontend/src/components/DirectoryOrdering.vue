<script>
export default {
  props: {
    orderBy: {
      type: String,
      required: true,
    }
  },
  emits: ['update:orderBy'],
  data() {
    return {
      options: [
        {title: 'Title', value: 'title'},
        {title: 'Created', value: 'createdDate'},
        {title: 'Modified', value: 'modifiedDate'},
        {title: 'Last viewed by me', value: 'lastViewedByMeDate'},
        {title: 'Shared with me', value: 'sharedWithMeDate'},
      ],
    };
  },
  computed: {
    order: {
      get() {
        return this.orderBy.split(' ')[0];
      },
      set(value) {
        this.$emit('update:orderBy', `${value} ${this.direction}`);
      },
    },
    direction: {
      get() {
        return this.orderBy.split(' ')[1];
      },
      set(value) {
        this.$emit('update:orderBy', `${this.order} ${value}`);
      },
    },
  },
}
</script>

<template>
  <div class="directory-ordering">
    <label for="ordering-order">Order by</label>
    <select
      id="ordering-order"
      v-model="order"
      class="ordering-order"
    >
      <option
        v-for="option in options"
        :key="option.value"
        :value="option.value"
      >
        {{ option.title }}
      </option>
    </select>
    <input
      id="ordering-direction"
      v-model="direction"
      class="ordering-direction"
      type="checkbox"
      title="Direction"
      true-value="desc"
      false-value="asc"
    >
  </div>
</template>

<style scoped>
.directory-ordering {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 500;
}

.ordering-order {
  appearance: none;
  padding: 0.5rem 1rem;
  border: 1px solid lightgray;
  border-radius: 15px;
  text-align: center;
  letter-spacing: 0.025em;
  background: ghostwhite;
}

.ordering-direction {
  appearance: none;
}

.ordering-direction::before {
  content: '⇧';
  display: flex;
  justify-content: center;
  align-items: center;
  width: 2rem;
  height: 2rem;
  border: 1px solid lightgray;
  border-radius: 50%;
  font-size: 1.3rem;
  background: ghostwhite;
}

.ordering-direction:checked::before {
  content: '⇩';
}
</style>
