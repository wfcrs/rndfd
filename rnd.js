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

let json = ""

let sum = 0
Object.values(foods).map((v, i) => (sum += v))
console.log(
  'Array contains',
  Object.values(foods).length,
  'foods. Weight sum is',
  sum
)
let r = Math.random() * sum
console.log('r =',r)
let selectedFood
for (let food of Object.keys(foods)) {
  r -= foods[food]
  if (r <= 0) {
    selectedFood = dict[food]
    break
  }
}
console.log('--------\n')
console.log(selectedFood,'\n\n')
