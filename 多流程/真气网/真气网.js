const CryptoJS = require('crypto-js');
const Base64 = require('js-base64').Base64;
const Crypto = require('crypto-js');

// 创建全局window对象
global.window = global;
global.document = {
    documentElement: {
        style: {}
    }
};
global.navigator = {
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
};

akb33 = "32223"
akb34 = "N4EDAQpO2ejqgCoX"
akb35 = "=qoKNLgdAjJbU8zx"
akb36 = "mAkJqt8coXQ96zML"
akb48 = "t4ABRmeN"
var AES = {
        encrypt: function(text) {
            var secretkey = (CryptoJS.MD5(akb34).toString()).substr(16, 16);
            var secretiv = (CryptoJS.MD5(akb35).toString()).substr(0, 16);
            secretkey = CryptoJS.enc.Utf8.parse(secretkey);
            secretiv = CryptoJS.enc.Utf8.parse(secretiv);
            var result = CryptoJS.AES.encrypt(text, secretkey, {
                iv: secretiv,
                mode: CryptoJS.mode.CBC,
                padding: CryptoJS.pad.Pkcs7
            });
            return result.toString()
        },
    };
var DES = {
    encrypt: function(text) {
        var secretkey = (CryptoJS.MD5(akb36).toString()).substr(0, 16);
        var secretiv = (CryptoJS.MD5(akb48).toString()).substr(24, 8);
        secretkey = CryptoJS.enc.Utf8.parse(secretkey);
        secretiv = CryptoJS.enc.Utf8.parse(secretiv);
        var result = CryptoJS.DES.encrypt(text, secretkey, {
            iv: secretiv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return result.toString()
    },
};
function ObjectSort(obj) {
        var newObject = {};
        Object.keys(obj).sort().map(function(key) {
            newObject[key] = obj[key]
        });
        return newObject
    }


function MyEncode(str) {
    var arr = akb33.split('')
    arr.forEach(times => {
        switch (times) {
        case "1":
            str = AES.encrypt(str)
            break;
        case "2":
            str = DES.encrypt(str)
            break;
        case "3":
            str = Base64.encode(str)
            break;
        }
    }
    )
    return str;
}
function getParam(method, obj) {
    var appId = '4f0e3a273d547ce6b7147bfa7ceb4b6e';
    var timestamp = new Date().getTime();
    var need = {
        appId: appId,
        method: method,
        timestamp: timestamp,
        clienttype: 'WEB',
        object: obj,
        secret: CryptoJS.MD5(appId + method + timestamp + 'WEB' + JSON.stringify(ObjectSort(obj)))
    };
    return MyEncode(JSON.stringify(need))
}

result = getParam("GETCITYAQIRANK",{order: 'desc'})
console.log(result)

// 导出getParam函数
module.exports = {
    getParam: getParam
};