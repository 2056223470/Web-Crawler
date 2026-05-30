window = global
const crypto = require('crypto')

var t = "/api/home/getnewsflash?firstrankindex=&lastrankindex=1749201240765&lastranktime=1749201240765&pagesize=10"
// var n = "{}"
//
// var c1 = {
//     "n": 20,
//     "codes": {
//         "0": "W",
//         "1": "l",
//         "2": "k",
//         "3": "B",
//         "4": "Q",
//         "5": "g",
//         "6": "f",
//         "7": "i",
//         "8": "i",
//         "9": "r",
//         "10": "v",
//         "11": "6",
//         "12": "A",
//         "13": "K",
//         "14": "N",
//         "15": "k",
//         "16": "4",
//         "17": "L",
//         "18": "1",
//         "19": "8"
//     }
// }
//
// function b1() {
//     for (var e = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase(), t = e + e, n = "", i = 0; i < t.length; ++i) {
//         var o = t[i].charCodeAt() % c1.n;
//         n += c1.codes[o]
//     }
//     console.log(n)
//     return n
// }
//
// function o1() {
//     return (0, a1)(t + n, (0, b1)(t)).toLowerCase().substr(8, 20)
// }
//
// function a1(e, key) {
//     return crypto.createHmac('sha512', key).update(e).digest('hex')
// }
//
// i = (0, o1)(t, undefined) // 验证正确
function r1() {
                var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
                  , key2 = "e0cf3d056ae41150752b3e052fa7a26c"
                  , n = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
                  , i = JSON.stringify(e).toLowerCase();
                console.log(e,key2,n,i)
                return (0,
                a2)(n + "pathString" + i + key2, (0,
                o2)(n))
            }
function a2(e, key) {
                return crypto.createHmac('sha512', key).update(e).digest('hex')
            }

function o2() {
    for (var e = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase(), t = e + e, n = "", i = 0; i < t.length; ++i) {
        var o = t[i].charCodeAt() % a3.n;
        n += a3.codes[o]
    }
    console.log("n2"+ n)
    return n
}

a3 = {
    "n": 20,
    "codes": {
        "0": "W",
        "1": "l",
        "2": "k",
        "3": "B",
        "4": "Q",
        "5": "g",
        "6": "f",
        "7": "i",
        "8": "i",
        "9": "r",
        "10": "v",
        "11": "6",
        "12": "A",
        "13": "K",
        "14": "N",
        "15": "k",
        "16": "4",
        "17": "L",
        "18": "1",
        "19": "8"
    }
}

function d1() {
                var list = ["w", "i", "n", "d", "o", "w", ".", "t", "i", "d"];
                return eval(list.join(""))
            }
// 42ebd7650b5ebc17ab495bfd02defa31c83f6a75f778ddf4c6c5d2019641911f08c30da43a0ce97eccf1e7aec829a3a28159518d7280cc29fa1bd293651e1ebe
u = (0, r1)(t, undefined, (0, d1)());

// console.log(i)
console.log(u)




