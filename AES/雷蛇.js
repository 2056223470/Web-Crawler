const CryptoJS = require('crypto-js')
window = global
!function(e) {
                function r(r) {
                    for (var n, o, f = r[0], u = r[1], d = r[2], b = 0, l = []; b < f.length; b++)
                        o = f[b],
                        Object.prototype.hasOwnProperty.call(a, o) && a[o] && l.push(a[o][0]),
                        a[o] = 0;
                    for (n in u)
                        Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                    for (i && i(r); l.length; )
                        l.shift()();
                    return c.push.apply(c, d || []),
                    t()
                }
                function t() {
                    for (var e, r = 0; r < c.length; r++) {
                        for (var t = c[r], n = !0, f = 1; f < t.length; f++) {
                            var u = t[f];
                            0 !== a[u] && (n = !1)
                        }
                        n && (c.splice(r--, 1),
                        e = o(o.s = t[0]))
                    }
                    return e
                }
                var n = {}
                  , a = {
                    7: 0
                }
                  , c = [];
                function o(r) {
                    if (n[r])
                        return n[r].exports;
                    var t = n[r] = {
                        i: r,
                        l: !1,
                        exports: {}
                    };
                    console.log(r)
                    return e[r].call(t.exports, t, t.exports, o),
                    t.l = !0,
                    t.exports
                }
                o.e = function(e) {
                    var r = []
                      , t = a[e];
                    if (0 !== t)
                        if (t)
                            r.push(t[2]);
                        else {
                            var n = new Promise((function(r, n) {
                                t = a[e] = [r, n]
                            }
                            ));
                            r.push(t[2] = n);
                            var c, f = document.createElement("script");
                            f.charset = "utf-8",
                            f.timeout = 120,
                            o.nc && f.setAttribute("nonce", o.nc),
                            f.src = function(e) {
                                return "https://razerid-assets.razerzone.com/static/js/" + ({}[e] || e) + "." + {
                                    0: "6879de06",
                                    1: "253a8428",
                                    2: "ec7bf6d4",
                                    3: "22e9417d",
                                    4: "f9476f63",
                                    5: "997332cd",
                                    9: "693ddfb9",
                                    10: "46132b97",
                                    11: "8e34f897",
                                    12: "66489680",
                                    13: "f3add49c",
                                    14: "5361bf1e",
                                    15: "28556800",
                                    16: "0cc65bfc",
                                    17: "209b53ac",
                                    18: "27a80403",
                                    19: "052da78d",
                                    20: "5c72ce15",
                                    21: "7c40f6bc",
                                    22: "1167b926",
                                    23: "1572ba16",
                                    24: "e8b2c2c1",
                                    25: "0756c509",
                                    26: "de7ebc18",
                                    27: "0316a765",
                                    28: "99eb17fe",
                                    29: "bdcf02eb",
                                    30: "62622154",
                                    31: "e5905175",
                                    32: "ffe859d1",
                                    33: "78761ac5",
                                    34: "f0dbc430",
                                    35: "965a2d51",
                                    36: "d992b84d",
                                    37: "0acfb663",
                                    38: "765dfbe4",
                                    39: "ac0f7a48",
                                    40: "aa3c37be",
                                    41: "b6663eb6",
                                    42: "c542e5dd",
                                    43: "75718143",
                                    44: "5217110b",
                                    45: "3fbcc33f",
                                    46: "b213ab72",
                                    47: "ab26d26e",
                                    48: "b7f53030",
                                    49: "96a2fb7e",
                                    50: "ae442c52",
                                    51: "1a243d17",
                                    52: "9f5f0615",
                                    53: "fc1f1173",
                                    54: "baacb306",
                                    55: "d17598b1",
                                    56: "4dc8b2fa",
                                    57: "d770f2f6",
                                    58: "934250b1",
                                    59: "61bc6378",
                                    60: "8ea99f1a",
                                    61: "5136c9bd",
                                    62: "1f21c17a",
                                    63: "19710d5e",
                                    64: "27c03e46",
                                    65: "abcbf4c0",
                                    66: "d9c43655",
                                    67: "ed5235ae",
                                    68: "64053ccb",
                                    69: "adb6e1af",
                                    70: "944e04f4",
                                    71: "d9351456",
                                    72: "bae4e101",
                                    73: "55b3fcd8"
                                }[e] + ".chunk.js"
                            }(e);
                            var u = new Error;
                            c = function(r) {
                                f.onerror = f.onload = null,
                                clearTimeout(d);
                                var t = a[e];
                                if (0 !== t) {
                                    if (t) {
                                        var n = r && ("load" === r.type ? "missing" : r.type)
                                          , c = r && r.target && r.target.src;
                                        u.message = "Loading chunk " + e + " failed.\n(" + n + ": " + c + ")",
                                        u.name = "ChunkLoadError",
                                        u.type = n,
                                        u.request = c,
                                        t[1](u)
                                    }
                                    a[e] = void 0
                                }
                            }
                            ;
                            var d = setTimeout((function() {
                                c({
                                    type: "timeout",
                                    target: f
                                })
                            }
                            ), 12e4);
                            f.onerror = f.onload = c,
                            document.head.appendChild(f)
                        }
                    return Promise.all(r)
                }
                ,
                o.m = e,
                o.c = n,
                o.d = function(e, r, t) {
                    o.o(e, r) || Object.defineProperty(e, r, {
                        enumerable: !0,
                        get: t
                    })
                }
                ,
                o.r = function(e) {
                    "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                        value: "Module"
                    }),
                    Object.defineProperty(e, "__esModule", {
                        value: !0
                    })
                }
                ,
                o.t = function(e, r) {
                    if (1 & r && (e = o(e)),
                    8 & r)
                        return e;
                    if (4 & r && "object" == typeof e && e && e.__esModule)
                        return e;
                    var t = Object.create(null);
                    if (o.r(t),
                    Object.defineProperty(t, "default", {
                        enumerable: !0,
                        value: e
                    }),
                    2 & r && "string" != typeof e)
                        for (var n in e)
                            o.d(t, n, function(r) {
                                return e[r]
                            }
                            .bind(null, n));
                    return t
                }
                ,
                o.n = function(e) {
                    var r = e && e.__esModule ? function() {
                        return e.default
                    }
                    : function() {
                        return e
                    }
                    ;
                    return o.d(r, "a", r),
                    r
                }
                ,
                o.o = function(e, r) {
                    return Object.prototype.hasOwnProperty.call(e, r)
                }
                ,
                o.p = "/",
                o.oe = function(e) {
                    throw console.error(e),
                    e
                }
                ;
                var f = this["webpackJsonprazer-id"] = this["webpackJsonprazer-id"] || []
                  , u = f.push.bind(f);
                f.push = r,
                f = f.slice();
                for (var d = 0; d < f.length; d++)
                    r(f[d]);
                var i = u;
                // t()
                jzq = o
            }
({
        49: function(T, _, E) {
            "use strict";
            E.d(_, "c", (function() {
                return i
            }
            )),
            E.d(_, "b", (function() {
                return R
            }
            )),
            E.d(_, "a", (function() {
                return o
            }
            ));
            var e = CryptoJS
            const i = (T, _) => e.AES.encrypt(T, _).toString()
              , R = (T, _) => {
                try {
                    const E = e.AES.decrypt(T, _);
                    if (!E)
                        return null;
                    const a = E.toString(e.enc.Utf8);
                    return a || null
                } catch {
                    return null
                }
            }
              , r = T => T.length > 32 ? T.substring(0, 32) : `${T}${"G6jptXCj9kSP2Wu4TCF1HmEZSUmSeGvV".slice(T.length)}`
              , o = (T, _) => {
                const E = r(_)
                  , e = (T => {
                    const _ = "0123456789abcdef";
                    let E = "";
                    for (let e = 0; e < T; ++e)
                        E += _.charAt(Math.floor(16 * Math.random()));
                    return E
                }
                )(16)
                  , a = t.Buffer.from(e)
                  , i = n.a.createCipheriv("aes-256-cbc", E, a);
                let R = i.update(T, "utf-8", "hex");
                return R += i.final("hex"),
                `${e}${R}`
            }
            window.encrypt = i
        },
})


jzq(49)
result = window.encrypt('123|rzrpw_u4dNqrv|1749991671', '{"COP":{"User":{"email":"20223702@csuft.edu.cn"},"ServiceCode":"0060"}}')
console.log(result)