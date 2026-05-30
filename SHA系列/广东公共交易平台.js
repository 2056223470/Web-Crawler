// 加密确认无误
const CryptoJS = require('crypto-js');

data = {
    "type": "trading-type",
    "openConvert": false,
    "keyword": "",
    "siteCode": "44",
    "secondType": "A",
    "tradingProcess": "",
    "thirdType": "[]",
    "projectType": "",
    "publishStartTime": "",
    "publishEndTime": "",
    "pageNo": 3,
    "pageSize": 10
}

// 生成13位时间戳
// const a = Date.now();

// SHA256加密函数
function eF(str) {
    return CryptoJS.SHA256(str).toString();
}

function qF(e) {
    let t = "";
    return typeof e == "object" ? t = Object.keys(e).map(n => `${n}=${e[n]}`).sort().join("&") : typeof e == "string" && (t = e.split("&").sort().join("&")),
    t
}
function D1(e={}) {
    const {p: t, t: n, n: u, k: o} = e
      , r = qF(t);
    return eF(u + o + decodeURIComponent(r) + n)
}

// 将data对象转换为URL参数字符串
const dataStr = Object.entries(data)
    .map(([key, value]) => `${key}=${value}`)
    .join('&');

var p = D1({
    p: dataStr,
    t: 1749725624106,
    n: "CIvWglfUkZ56kOpd",
    k: "k8tUyS$m"
});
console.log(p.toString())