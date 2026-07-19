# Web 逆向分析与爬虫实战积累

> 个人 Web 逆向分析与数据采集实战项目集，按加密类型与业务场景分类整理，涵盖 JS 扣码、Webpack 模块还原、Python 联调请求及基础爬虫脚本。

---

## 项目简介

本仓库记录了 2025 年 2 月至今的逆向分析与爬虫实践案例。每个子目录对应一类技术场景或具体站点，核心工作包括：

- 浏览器抓包与断点调试，定位加密/签名逻辑
- 从混淆或 Webpack 打包代码中还原关键函数
- 使用 Node.js / PyExecJS 在 Python 中调用 JS 加密逻辑
- 编写完整的数据采集脚本（部分案例仅保留算法还原，不含实际请求）

---

## 目录结构

```
.
├── 基础/                    # 基础爬虫与数据采集
│   ├── 12306查询/           # 列车余票查询（含软件设计课设版）
│   ├── 优品ppt下载/
│   ├── 梨视频下载/
│   ├── 九九美剧下载/
│   ├── 药品信息下载/
│   ├── 王者皮肤/
│   └── 素材/                # 爬取过程中使用的 CSV 等辅助数据
├── MD5/                     # MD5 及变种签名
├── AES/                     # AES 对称加密
├── SHA系列/                 # SHA256 / SHA512 等哈希签名
├── RSA/                     # RSA 非对称加密
├── webpack/                 # Webpack 打包站点逆向
├── JS/                      # 纯 JS 环境加密逻辑
├── 混淆/                    # 代码混淆站点
├── 多流程/                  # 请求参数与响应均为加密的复合流程
└── 验证码登录/              # 浏览器自动化 + 滑块验证码识别
```

---

## 技术栈

| 类别 | 工具 / 库 |
|------|-----------|
| 语言 | Python 3、JavaScript (Node.js) |
| HTTP | requests、requests-html |
| JS 执行 | PyExecJS、subprocess + Node.js |
| 加密 | crypto-js、Node.js crypto、pycryptodome |
| 浏览器自动化 | DrissionPage（验证码登录案例） |
| 验证码识别 | 超级鹰 API（坐标类题目） |
| 数据存储 | CSV、MongoDB（12306 课设版） |
| 其他 | YAML 配置、观察者模式（课设架构） |

---

## 案例清单

### 基础爬虫

| 案例 | 说明 | 时间 |
|------|------|------|
| [12306 列车查询](基础/12306查询(25-4-4)/) | 车站编码解析、余票接口请求；课设版采用观察者模式 + MongoDB 持久化 | 2025-04 |
| [优品 PPT 批量下载](基础/优品ppt下载(25-4-5)/) | 批量下载 PPT 资源 | 2025-04 |
| [梨视频批量下载](基础/梨视频下载(25-4-5)/) | 视频资源批量采集 | 2025-04 |
| [九九美剧下载](基础/九九美剧下载(25-4-13)/) | 美剧资源批量下载 | 2025-04 |
| [药品信息下载](基础/药品信息下载(25-4-12)/) | 药品数据批量采集 | 2025-04 |
| [王者英雄海报抓取](基础/王者皮肤/) | 游戏英雄海报图片采集 | 2025-04 |

### MD5 系列

| 案例 | 站点 | 要点 | 时间 |
|------|------|------|------|
| [酷狗评论](MD5/kugou.py) | 酷狗音乐搜索 | 请求参数按固定顺序拼接后 MD5 生成 `signature` | 2025-02 |
| [99 通行证](MD5/99通行证.js) | 游戏平台登录 | 标准 MD5，明文拼接后哈希 | 2025-06 |
| [乐居](MD5/乐居.js) | 房产 SSO 登录 | MD5 混合 Base64 | 2025-06 |

### Webpack 系列

| 案例 | 站点 | 要点 | 时间 |
|------|------|------|------|
| [宝树号](webpack/宝树号/) | 宝宝树开放平台 | Webpack 模块还原 | 2025-05 |
| [五矿信息采购](webpack/五矿(25-5-16)/) | 五矿集团采购平台 | Webpack + Python 联调请求 | 2025-05 |
| [大风车](webpack/大风车.js) | 搜车网登录 | Webpack + RSA 复合加密 | 2025-06 |
| [财联社](webpack/财联社.js) | 财经资讯 | Webpack 打包逆向 | 2025-06 |

### AES 系列

| 案例 | 站点 | 要点 | 时间 |
|------|------|------|------|
| [网易云评论](AES/网易云评论.py) | 网易云音乐 | 双层 AES-CBC 解密评论接口响应数据 | 2025-02 |
| [雷蛇](AES/雷蛇.js) | Razer ID 登录 | Webpack 嵌套 + AES，逻辑较复杂 | 2025-06 |
| [随行易](AES/随行易.js) | 随行易平台 | 推测加密流程并代码模拟 | 2025-06 |

### SHA 系列

| 案例 | 站点 | 要点 | 时间 |
|------|------|------|------|
| [企查查](SHA系列/企查查.js) | 企业信息查询 | SHA512 签名 | 2025-06 |
| [广东公共资源交易平台](SHA系列/广东公共交易平台.js) | 政府采购 | 异步跟栈 + SHA256 | 2025-06 |

### RSA 系列

| 案例 | 站点 | 要点 | 时间 |
|------|------|------|------|
| [监心系统](RSA/监心系统.js) | 博声远程心电监测 | RSA 登录加密 | 2025-06 |
| [百城招聘](RSA/百城招聘.js) | 招聘平台 | 标准 RSA | 2025-06 |
| [五百丁](RSA/五百丁.js) | 简历制作 | RSA 参数模拟 | 2025-06 |
| [混沌书院](RSA/混沌书院.js) | 在线教育 | RSA 加密 | — |
| [网上管家婆](RSA/网上管家婆.js) | 电商 ERP | RSA 加密 | — |

### 其他类型

| 分类 | 案例 | 站点 | 要点 | 时间 |
|------|------|------|------|------|
| 纯 JS | [国家开放大学](JS/国家开放大学/) | 国开登录 | 独立 JS 加密环境 | 2025-05 |
| 混淆 | [湖师大登录](混淆/湖师大登录.js) | 继续教育学院 | 混淆代码还原 | 2025-06 |
| 多流程 | [真气网](多流程/真气网/) | 环境监测 | 请求 param 与响应均为加密，含 Python 联调 | 2025-06 |

---

## 典型实现模式

### 1. MD5 参数签名（以酷狗为例）

```python
# MD5/kugou.py
# 将请求参数按固定顺序拼接为字符串，MD5 哈希后作为 signature 附带到 URL
data = f'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014...keyword={music_name}...NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
signature = hashlib.md5(data.encode('utf-8')).hexdigest()
url = f'https://complexsearch.kugou.com/v2/search/song?...&signature={signature}'
```

### 2. 双层 AES-CBC 解密（以网易云为例）

```python
# AES/网易云评论.py
# 评论接口响应经两次 AES-CBC 解密（不同 Key，相同 IV）得到明文 JSON
dec1 = aes_cbc_decrypt(ciphertext, key="b5F8rL2a4OQxSuKz", iv="0102030405060708")
dec2 = aes_cbc_decrypt(dec1,       key="0CoJUm6Qyw8W8jud", iv="0102030405060708")
```

### 3. Python 调用 Node.js（以五矿为例）

```python
# webpack/五矿(25-5-16)/request.py
# 通过 subprocess 调用 Node.js 执行 params.js，获取签名后发送 HTTP 请求
result = run_js_file("getParams", url=target_url)
requests.post(url, data=result)
```

### 4. PyExecJS 联调（以真气网为例）

```python
# 多流程/真气网/request.py
ctx = execjs.compile(js_code)
param = ctx.call('getParam', 'POST', payload)
response = requests.post(url, data={"param": param})
```

### 5. 12306 课设架构（观察者模式）

课设版在基础查询之上增加了设计模式实践：

- `TrainQuery` — 核心查询逻辑
- `QuerySubject` / `LoggingObserver` — 观察者模式解耦
- `ResultProcessorFactory` — 工厂模式处理结果
- `MongoDBManager` — 查询结果持久化

---

## 环境要求

```bash
# Python 依赖（按需安装）
pip install requests requests-html pyyaml pymongo execjs pycryptodome

# Node.js 依赖（部分 JS 案例需要）
npm install crypto-js
```

> 部分案例依赖系统已安装的 Node.js，PyExecJS 需配置对应 JS 运行时（推荐 Node）。

---

## 使用说明

1. 进入对应案例目录，阅读 JS / Python 文件中的注释
2. 带 `config.yaml` 的项目需先修改配置（如 Cookie、下载路径等）
3. 逆向案例通常只保留算法还原代码，**不包含有效 Cookie 或账号信息**
4. 带 `(AI版)` 后缀的文件为借助 AI 辅助重构/优化的版本，可与原版对照学习

---

## 免责声明

本项目所有代码**仅供个人学习与技术研究**，请勿用于任何商业或非法用途。使用本项目代码访问第三方网站时，请遵守目标网站的 robots 协议、用户协议及相关法律法规。因不当使用造成的任何后果，由使用者自行承担。

---

## 更新记录

| 时间 | 内容 |
|------|------|
| 2025-02 | 早期案例：酷狗 MD5 签名、网易云双层 AES 解密 |
| 2025-04 | 基础爬虫系列（12306、视频/PPT/药品下载等） |
| 2025-05 | Webpack 系列、国开 JS 逆向 |
| 2025-06 | SHA / RSA / 混淆 / 多流程加密案例集中突破 |

---

## License

本项目采用 [MIT License](LICENSE) 开源。代码仅供学习交流，请勿用于违法用途。
