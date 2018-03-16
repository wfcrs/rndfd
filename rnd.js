// const foods = {
//   // foodname: weight
//   shuijiao: 1,
//   tieban: 3,
//   erlou: 3,
//   jipaifan: 3
// }

// const dict = {
//   // foodname: dictionary
//   shuijiao: '水饺',
//   tieban: '铁板',
//   erlou: '二楼',
//   jipaifan: '鸡排饭'
// }

let jsondir = "https://github.com/wfcrs/rndfd/raw/master/foods.json"

function getKeys() {
  var xmlhttp;
  if (window.XMLHttpRequest) xmlhttp = new XMLHttpRequest();
  else xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
  xmlhttp.open("GET", jsondir, false);
  xmlhttp.send();
  return JSON.parse(xmlhttp.responseText)
}

let sum = 0

let foods = getKeys();
Object.keys(foods).map((v, i) => (sum += foods[v].weight))
console.log(
  'Array contains',
  Object.keys(foods).length,
  'foods. Weight sum is',
  sum
)
let r = Math.random() * sum
console.log('r =', r)
let selectedFood
for (let food of Object.keys(foods)) {
  r -= foods[food]
  if (r <= 0) {
    selectedFood = foods[food].name
    break
  }
}
console.log('--------\n')
console.log(selectedFood, '\n\n')
