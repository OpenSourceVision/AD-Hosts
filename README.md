# Hosts Ad Blocker 🚫🔒

[![更新状态](https://github.com/OpenSourceVision/hosts-ad-blocker/workflows/Update%20Hosts%20Rules/badge.svg)](https://github.com/OpenSourceVision/hosts-ad-blocker/actions)
[![最新版本](https://img.shields.io/github/v/release/OpenSourceVision/hosts-ad-blocker)](https://github.com/OpenSourceVision/hosts-ad-blocker/releases/latest)
[![下载次数](https://img.shields.io/github/downloads/OpenSourceVision/hosts-ad-blocker/total)](https://github.com/OpenSourceVision/hosts-ad-blocker/releases)

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
3. 替换系统中的 hosts 文件

### 方法二：使用原始链接

```bash
# 下载最新版本
curl -L https://github.com/your-username/hosts-ad-blocker/releases/latest/download/hosts -o hosts
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

## 📜 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

## 🙏 致谢

感谢所有规则来源项目的维护者们，为网络安全和广告屏蔽做出的贡献！

---

⭐ 如果这个项目对您有帮助，请给它一个 Star！

💬 有问题或建议？欢迎提交 [Issue](https://github.com/your-username/hosts-ad-blocker/issues)！
