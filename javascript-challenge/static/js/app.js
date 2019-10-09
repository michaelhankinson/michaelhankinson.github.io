// from data.js
var tableData = data;

// D3 select
var tbody = d3.select("tbody");
var submit = d3.select("#filter-btn");

updateTable(tableData);

// console.log(tableData)

// Update table with a new dataset
function updateTable(dataset) {
  tbody.html('');
  dataset.forEach((toBeDefined) => {
    var row = tbody.append("tr");
    Object.entries(toBeDefined).forEach(([key,value]) => {
      var cell = tbody.append("td");
      cell.text(value);
    });
  });
}
// Filter date function (just compare a string)
function filterByDate(data) {
  var input = d3.select('#datetime').property("value");
  console.log(input, data)
    var filteredData = data.filter(d => d.datetime === input);
    console.log("Filter", filteredData)
    return filteredData;
}

// First update table of original data
submit.on("click", function() {
  // Filter data by datetime and update the table
  var result = filterByDate(tableData);
  console.log("Click Working")
  updateTable(result); 
});
