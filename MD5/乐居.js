// 引入必要的库
const CryptoJS = require('crypto-js');
const Base64 = require('js-base64').Base64;

function secretMethod(e) {
    // 计算MD5
    const md5Hash = CryptoJS.MD5(e).toString();
    // Base64编码原始输入
    const encodedInput = Base64.encode(e);
    // 组合并返回最终结果
    return Base64.encode(md5Hash.substr(0, 8) + encodedInput + md5Hash.substr(10, 4));
}

// 测试代码
const result = secretMethod("15274992158");
console.log(result);