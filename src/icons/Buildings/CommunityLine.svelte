<script>
  import svg from 'remixicon/icons/Buildings/community-line.svg?raw';
  import Icon from '../../Icon.svelte';
  export let size = '20px';
  export let color = '#2E383A';
</script>

<div style:width={size} style:height={size} style:color>
  <Icon data={svg} />
</div>
