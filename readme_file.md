# Hosts Ad Blocker 🚫🔒

[![更新状态](https://github.com/your-username/hosts-ad-blocker/workflows/Update%20Hosts%20Rules/badge.svg)](https://github.com/your-username/hosts-ad-blocker/actions)
[![最新版本](https://img.shields.io/github/v/release/your-username/hosts-ad-blocker)](https://github.com/your-username/hosts-ad-blocker/releases/latest)
[![下载次数](https://img.shields.io/github/downloads/your-username/hosts-ad-blocker/total)](https://github.com/your-username/hosts-ad-blocker/releases)

自动聚合多个优质来源的 hosts 广告屏蔽规则，每12小时自动更新，为您提供最新最全面的广告屏蔽体验。

## ✨ 特性

- 🔄 **自动更新**: 每12小时自动抓取最新规则
- 📦 **多源聚合**: 整合多个知名项目的规则
- 🌏 **中外兼顾**: 包含中文和国外广告屏蔽规则  
- ⚡ **高效去重**: 智能去重和域名验证
- 📊 **统计信息**: 详细的更新日志和统计
- 🚀 **即用即得**: 直接下载使用，无需配置

## 📥 快速使用

### 方法一：直接下载 (推荐)

1. 前往 [Releases](https://github.com/your-username/hosts-ad-blocker/releases/latest) 页面
2. 下载最新的 `hosts` 文件
3. 按照下方的安装指南进行操作

### 方法二：使用原始链接

```bash
# 下载最新版本
curl -L https://github.com/your-username/hosts-ad-blocker/releases/latest/download/hosts -o hosts
```

## 🛠 安装指南

### Windows

1. **备份现有文件**:
   ```cmd
   copy C:\Windows\System32\drivers\etc\hosts C:\Windows\System32\drivers\etc\hosts.backup
   ```

2. **以管理员身份运行记事本**，打开文件:
   ```
   C:\Windows\System32\drivers\etc\hosts
   ```

3. **将下载的内容追加**到现有 hosts 文件末尾

4. **刷新 DNS 缓存**:
   ```cmd
   ipconfig /flushdns
   ```

### Linux / macOS

1. **备份现有文件**:
   ```bash
   sudo cp /etc/hosts /etc/hosts.backup
   ```

2. **追加规则**:
   ```bash
   sudo cat hosts >> /etc/hosts
   ```
   
   或者使用编辑器:
   ```bash
   sudo nano /etc/hosts
   ```

3. **刷新 DNS 缓存**:
   ```bash
   # macOS
   sudo dscacheutil -flushcache
   
   # Linux (Ubuntu/Debian)
   sudo systemctl restart systemd-resolved
   ```

## 📊 规则来源

本项目整合以下优质来源的规则：

| 来源 | 描述 | 更新频率 |
|------|------|----------|
| [StevenBlack/hosts](https://github.com/StevenBlack/hosts) | 综合广告和恶意软件屏蔽 | 每日 |
| [AdguardTeam/AdguardFilters](https://github.com/AdguardTeam/AdguardFilters) | Adguard 官方广告服务器列表 | 实时 |
| [privacy-protection-tools/anti-AD](https://github.com/privacy-protection-tools/anti-AD) | 中文广告domain屏蔽 | 每日 |
| [notracking/hosts-blocklists](https://github.com/notracking/hosts-blocklists) | 追踪器屏蔽列表 | 每周 |
| [Goooler/1024_hosts](https://github.com/Goooler/1024_hosts) | 中文广告屏蔽规则 | 每日 |

## 🔧 本地运行

如果您想在本地运行此项目：

```bash
# 克隆仓库
git clone https://github.com/your-username/hosts-ad-blocker.git
cd hosts-ad-blocker

# 安装依赖
pip install requests

# 运行更新脚本
python main.py
```

## 📈 更新日志

- 查看 [更新统计](README_STATS.md) 了解最新的规则数量和来源状态
- 查看 [Releases](https://github.com/your-username/hosts-ad-blocker/releases) 了解历史版本
- 查看 [Actions](https://github.com/your-username/hosts-ad-blocker/actions) 了解自动更新状态

## ⚠️ 注意事项

- 使用前请**务必备份**现有的 hosts 文件
- 部分网站可能因为屏蔽规则而无法正常访问，属于正常现象
- 如果遇到访问问题，可以临时注释掉相关行进行测试
- 建议定期检查更新以获取最新的屏蔽规则

## 🤝 贡献

欢迎贡献代码或建议！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📜 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

## 🙏 致谢

感谢所有规则来源项目的维护者们，为网络安全和广告屏蔽做出的贡献！

---

⭐ 如果这个项目对您有帮助，请给它一个 Star！

💬 有问题或建议？欢迎提交 [Issue](https://github.com/your-username/hosts-ad-blocker/issues)！