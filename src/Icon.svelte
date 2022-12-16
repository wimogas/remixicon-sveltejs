<script>
  export let data = ''
  export let viewBox = extractViewBox(data)
  
  $: elements = data
    .replace(/<svg ([^>]*)>/, '')
    .replace('</svg>', '')
  function extractViewBox(svg) {
    const regex = /viewBox="([\d\- \.]+)"/
    const res = regex.exec(svg)
    if (!res) return '0 0 512 512' 
    return res[1]
  }
</script>

<style>
  svg {
    stroke: currentColor;
    fill: currentColor;
    stroke-width: 0;
    width: 100%;
    height: auto;
    max-height: 100%;
  }  
</style>

<svg
  xmlns="http://www.w3.org/2000/svg"
  {viewBox}
  {...$$restProps}
>
  {@html elements}
</svg>
