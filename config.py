# 讯飞开放平台配置
XFYUN_CONFIG = {
    'appid': 'xxxxx',
    'secret_key': 'xxxxxxxxxxxxxxxxxxxxxxx'
}

# 文件上传配置
UPLOAD_CONFIG = {
    'allowed_extensions': {'wav', 'mp3', 'm4a', 'flac', 'aac'},  # 允许的文件类型
    'max_file_size': 100 * 1024 * 1024  # 最大文件大小(100MB)
} 