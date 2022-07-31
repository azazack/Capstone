<template lang="pug">
ul.pagination.custom-pagination(v-if="paginate && paginate.last_page > 1")
  li.prev( :class="[firstPageSelected ? 'disabled' : '']")
    a.page-link( @click="prevPage()" @keyup.enter="prevPage()" :tabindex="firstPageSelected ? -1 : 0" ) &lt;
  li.page-item(v-for="page in pages" :class="[page.selected ? 'active' : '', page.disabled ? 'disabled' : '']")
    a( v-if="page.disabled" class="page-link" :tabindex="page.content") {{ page.content }}
    a.page-link( :tabindex="page.content" @click="handlePageSelected(page.index + 1)" @keyup.enter="handlePageSelected(page.index + 1)" v-else) {{ page.content }}
  li.next(:class="[lastPageSelected ? 'disabled' : '']")
    a.page-link( :tabindex="lastPageSelected ? -1 : 0" @click="nextPage()" @keyup.enter="nextPage()") &gt;
</template>

<script lang="ts" setup>
import { computed, ref } from "vue";
const props = defineProps<{ paginate: Paginate }>();
const emit = defineEmits<{
  (e: "page-changed", page: number): void;
}>();
const innerValue = ref(1);
const selected = computed((): number => {
  return props.paginate?.current_page || innerValue.value;
});
const firstPageSelected = computed((): boolean => {
  return selected.value === 1;
});
const lastPageSelected = computed((): boolean => {
  return (
      selected.value === props.paginate.last_page ||
      props.paginate.last_page === 0
  );
});
const pages = computed((): Record<number, unknown> => {
  const items: Record<number, unknown> = {};
  if (props.paginate.last_page <= 4) {
    for (let index = 0; index < props.paginate.last_page; index += 1) {
      items[index] = {
        index,
        content: index + 1,
        selected: index === selected.value - 1,
      };
    }
  } else {
    const halfPageRange = 2;
    const setPageItem = (index: number): void => {
      items[index] = {
        index,
        content: index + 1,
        selected: index === selected.value - 1,
      };
    };
    // 2nd - loop through selected range
    let selectedRangeLow = 0;
    if (selected.value - halfPageRange > 0) {
      selectedRangeLow = selected.value - 1 - halfPageRange;
    }
    let selectedRangeHigh = selectedRangeLow + 5 - 1;
    if (selectedRangeHigh >= props.paginate.last_page) {
      selectedRangeHigh = props.paginate.last_page - 1;
      selectedRangeLow = selectedRangeHigh - 5 + 1;
    }
    for (
        let i = selectedRangeLow;
        i <= selectedRangeHigh && i <= props.paginate.last_page - 1;
        i += 1
    ) {
      setPageItem(i);
    }
  }
  return items;
});
const selectPage = (page: number): void => {
  emit("page-changed", page);
};
const handlePageSelected = (select: number): void => {
  if (selected.value === select) {
    return;
  }
  innerValue.value = select;
  selectPage(select);
};
const prevPage = (): void => {
  if (selected.value <= 1) {
    return;
  }
  handlePageSelected(selected.value - 1);
};
const nextPage = (): void => {
  if (selected.value >= props.paginate.last_page) {
    return;
  }
  handlePageSelected(selected.value + 1);
};
</script>

<style lang="scss">
@import "bootstrap/scss/pagination";
nav.pagination-container {
  text-align: center;
}
ul.pagination.custom-pagination {
  display: inline-flex;
  > li {
    margin-left: 3px;
    margin-right: 3px;
    font-size: smaller;
    width: fit-content;
    height: 32px;
    a {
      cursor: pointer;
      border-radius: 4px;
      border: 1px solid #e1e4e8;
      box-sizing: border-box;
      padding: 12px 14px 12px 13px;
      margin: 0;
      font-weight: bold;
      width: fit-content;
      min-width: 25px;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: $primary-color;
      font-family: $font-family-base;
      font-size: 14px;
      letter-spacing: 0;
      line-height: 20px;
      text-align: center;
    }
    &.active {
      a {
        z-index: unset;
        background-color: $primary-color;
        color: white;
        font-weight: bold;
        &:hover {
          color: #eee;
          background-color: $primary-color;
        }
      }
    }
    &.next,
    &.prev {
      margin-left: 7px;
      margin-right: 7px;
      a {
        font-weight: bold;
        border: 1px solid #e1e4e8;
        box-sizing: border-box;
        padding: 12px 14px 12px 13px;
      }
    }
  }
  .page-item {
    padding: 0;
  }
}
</style>
