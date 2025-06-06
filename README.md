# Hosts Ad Blocker 🚫🔒 (中文增强版)

[![更新状态](https://github.com/OpenSourceVision/hosts-ad-blocker/workflows/Update%20Hosts%20Rules/badge.svg)](https://github.com/OpenSourceVision/hosts-ad-blocker/actions)
[![最新版本](https://img.shields.io/github/v/release/OpenSourceVision/hosts-ad-blocker)](https://github.com/OpenSourceVision/hosts-ad-blocker/releases/latest)
[![下载次数](https://img.shields.io/github/downloads/OpenSourceVision/hosts-ad-blocker/total)](https://github.com/OpenSourceVision/hosts-ad-blocker/releases)

自动聚合多个优质来源的 hosts 广告屏蔽规则，每12小时自动更新，为您提供最新最全面的广告屏蔽体验。**特别针对中文网站进行了优化增强！**

## ✨ 特性

- 🔄 **自动更新**: 每12小时自动抓取最新规则
- 📦 **多源聚合**: 整合多个知名项目的规则
- 🌏 **中文增强**: 重点加强中文网站广告屏蔽能力
- 🎯 **精准过滤**: 支持多种规则格式 (hosts、EasyList、Adblock)
- ⚡ **高效去重**: 智能去重和域名验证
- 📊 **统计信息**: 详细的更新日志和统计
- 🚀 **即用即得**: 直接下载使用，无需配置



## 📊 规则来源

本项目整合以下优质来源的规则，**特别加强了中文规则覆盖**：

| 来源 | 描述 | 类型 | 更新频率 |
|------|------|------|----------|
| [StevenBlack/hosts](https://github.com/StevenBlack/hosts) | 综合广告和恶意软件屏蔽 | 国际 | 每日 |
| [AdguardTeam/AdguardFilters](https://github.com/AdguardTeam/AdguardFilters) | Adguard 官方广告服务器列表 | 国际 | 实时 |
| [privacy-protection-tools/anti-AD](https://github.com/privacy-protection-tools/anti-AD) | 中文广告域名屏蔽 | 🇨🇳 中文 | 每日 |
| [EasyList China](https://easylist.to/) | EasyList 中国补充规则 | 🇨🇳 中文 | 每日 |
| [ChinaList AD](https://github.com/cjx82630/cjxlist) | 中文网站广告过滤规则 | 🇨🇳 中文 | 每周 |
| [ADgk](https://github.com/banbendalao/ADgk) | 中文广告过滤规则 | 🇨🇳 中文 | 每日 |
| [Halflife/list](https://github.com/halflife3/list) | 中文广告域名列表 | 🇨🇳 中文 | 每周 |
| [jdlingyu/ad-wars](https://github.com/jdlingyu/ad-wars) | 中文广告拦截规则 | 🇨🇳 中文 | 每日 |
| [neoFelhz/neohosts](https://github.com/neoFelhz/neohosts) | 自由·负责·克制 去广告 Hosts | 🇨🇳 中文 | 每日 |

## 🔧 高级功能

### 支持的规则格式
- **Hosts格式**: `0.0.0.0 example.com`
- **EasyList格式**: `||example.com^`
- **Adblock格式**: 自动解析并转换
- **纯域名格式**: `example.com`

### 智能过滤
- 自动跳过白名单规则 (`@@||domain`)
- 忽略元素隐藏规则 (`##`, `#@#`)
- 过滤正则表达式规则
- 域名格式验证和去重

## 📈 统计信息

- **屏蔽域名数量**: 通常包含 100,000+ 个域名
- **更新频率**: 每12小时自动更新
- **中文规则占比**: 约40%，专门针对中文网站优化
- **去重效率**: 平均去重率 15-20%

## 🛠️ 本地运行

如果您想本地运行更新脚本：

```bash
# 克隆仓库
git clone https://github.com/your-username/hosts-ad-blocker.git
cd hosts-ad-blocker

# 安装依赖
pip install requests

# 运行更新脚本
python main.py
```



## 📜 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

## 🙏 致谢

感谢所有规则来源项目的维护者们，特别是中文开源社区的贡献者，为网络安全和广告屏蔽做出的卓越贡献！

### 特别感谢
- **StevenBlack** - 提供优秀的 hosts 基础框架
- **privacy-protection-tools** - 中文广告屏蔽的先驱
- **EasyList 团队** - 专业的广告过滤规则
- **所有中文规则维护者** - 为中文互联网环境的净化而努力

---


🔄 **最新更新**: 现已支持9个优质规则源，专门优化中文网站广告屏蔽效果！
