window = global;
JSEncrypt = require('jsencrypt')

function doEncrypt(_0x50b4aa) {
    let _0x520b8d = new JSEncrypt();
    _0x520b8d['setPublicKey']('-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQChOdMggWiQCf1eEEpm5d+3iWHC3/w+lHQbMqHVEftwoRixm4Sd1iZjRdaeHJd0bClIHMCzzTQKO9bdiz+PdjuZwlTZEYCV6zzgT5Q9fPpbjtvYSK8XyzNSpjhDmNyLeuBoS+JNkdLzHoJisLuNZpVKlhh0d022/hLfd1FRnS+QtwIDAQAB-----END PUBLIC KEY-----');
    return _0x520b8d["encrypt"](_0x50b4aa)["trim"]();
}
function rsaEncrypts(_0x46f1de) {
    let _0x48b3b9 = "www.chaoslib.com"
    let _0x42e010 = 1750523935098
    let _0x29da7b = "123456(||::||)www.chaoslib.com(||::||)1750523935098"
    return doEncrypt(_0x29da7b);
}

console.log(rsaEncrypts('123456'))