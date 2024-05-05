<template>
  <cv-modal v-bind="props">
    <template v-slot:label>
      <slot name="label"></slot>
    </template>
    <template v-slot:title>
      <slot name="title"></slot>
    </template>
    <template v-slot:content>
      <p>
        <slot name="content"></slot>
      </p>
    </template>
    <template v-slot:other-button>SAVE SESSION</template>
    <template v-slot:secondary-button>RESTART TIMER</template>
    <template v-slot:primary-button>EXIT</template>
  </cv-modal>
</template>


<script setup>

// const visible = ref(true)
const props = defineProps({
  visible: {
    type: Boolean,
    default: true
  },
  other: {
    type: [String, Number],
    default: 'xs'
  }
})

</script>