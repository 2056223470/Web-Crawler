from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64  # 新增 base64 模块


# 加密函数（返回 Base64 字符串）
def aes_cbc_encrypt(plaintext: str, key: str, iv: str) -> str:
    # 将 UTF-8 字符串转换为字节并检查长度
    key_bytes = key.encode('utf-8')
    iv_bytes = iv.encode('utf-8')
    assert len(key_bytes) == 16, "Key 必须是 16 字节的 UTF-8 字符串"
    assert len(iv_bytes) == 16, "IV 必须是 16 字节的 UTF-8 字符串"

    # 创建 AES-CBC 加密器并加密
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))

    # 将字节转换为 Base64 字符串
    return base64.b64encode(ciphertext).decode('utf-8')


# 解密函数（接受 Base64 字符串输入）
def aes_cbc_decrypt(ciphertext_b64: str, key: str, iv: str) -> str:
    # 将 UTF-8 字符串转换为字节并检查长度
    key_bytes = key.encode('utf-8')
    iv_bytes = iv.encode('utf-8')
    assert len(key_bytes) == 16, "Key 必须是 16 字节的 UTF-8 字符串"
    assert len(iv_bytes) == 16, "IV 必须是 16 字节的 UTF-8 字符串"

    # 将 Base64 字符串解码为字节
    ciphertext = base64.b64decode(ciphertext_b64)

    # 创建 AES-CBC 解密器并解密
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data.decode('utf-8')

def wyy_decrypt(ciphertext_b64):
    dec1 = aes_cbc_decrypt(ciphertext_b64,"b5F8rL2a4OQxSuKz","0102030405060708")
    dec2 = aes_cbc_decrypt(dec1,"0CoJUm6Qyw8W8jud","0102030405060708")
    print(dec2)


# 示例用法
if __name__ == "__main__":
    wyy_decrypt("f2iyhnabPMRewRZodfnl0o/9tRE1e0s8rV1g0K+UwN++djNhSlNsobHz5flciiQoPTMB5ICcjCRjfpxOLJmmM9gOocT3yRTrlFeJPhsJhFETywtx6ZNBmiKATaFMVRhBcGD8qweozubdEDLux5K1i1ctTEy04E7S30hsBQT5MxEeHTUkOzBbCeeQokv/k+PX51ztlDDcM18b+NCGnoE6BnlNdVuUwtP3HKDsO6Tpg+oHconXHBI9pbN0e7ZttegCzSKp3cCnMQJHT/4ej4PoLF4lrmW37NxofqvUF96tNwESnKARY0SQV1Gqlnocr2urf8VveUSaGWCVb3HHXQhcP+QV5a7tEqAAqpH0x8C1rW4=")
    # key = "ThisIsASecretKey"  # 16 字节 UTF-8
    # iv = "ThisIsAnIV123456"  # 16 字节 UTF-8
    # plaintext = "Hello, 这是 AES-CBC-128 加密测试！"
    #
    # # 加密（得到 Base64 字符串）
    # ciphertext_b64 = aes_cbc_encrypt(plaintext, key, iv)
    # print("加密结果 (Base64):", ciphertext_b64)
    #
    # # 解密
    # decrypted_text = aes_cbc_decrypt(ciphertext_b64, key, iv)
    # print("解密结果:", decrypted_text)