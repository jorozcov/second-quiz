<template>
    <div class = 'chart-container' ref="chart"></div>
</template>

<script>
import * as d3 from 'd3';

export default {
name: 'MainChart',
props: {
    info_chart: String
},
updated() {
    this.createPieChart();
},
methods: {
    createPieChart() {
    const data = JSON.parse(this.info_chart);

    const width = 400;
    const height = 400;
    const radius = Math.min(width, height) / 2;

    const color = d3.scaleOrdinal(d3.schemeCategory10);

    const arc = d3.arc()
        .outerRadius(radius - 10)
        .innerRadius(0);

    const pie = d3.pie()
        .sort(null)
        .value(d => d.Total);

    // Clear existing content
    d3.select(this.$refs.chart).select('svg').remove();

    const svg = d3.select(this.$refs.chart)
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr('transform', `translate(${width / 2},${height / 2})`);

    const g = svg.selectAll('.arc')
        .data(pie(data))
        .enter().append('g')
        .attr('class', 'arc');

    g.append('path')
        .attr('d', arc)
        .style('fill', d => color(d.data.Year));

    g.append('text')
        .attr('transform', d => `translate(${arc.centroid(d)})`)
        .attr('dy', '.35em')
        .style('text-anchor', 'middle')
        .html(d => `<tspan x="0">${d.data.Year}</tspan><tspan x="0" dy="1.2em">Births: ${d.data.Total}</tspan>`);
    }
}
};
</script>

<style scoped>
.chart-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Optional: Adjust the height to your preference */
}
</style>
