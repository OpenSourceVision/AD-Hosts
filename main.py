#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hosts Ad Blocker Rules Aggregator
自动抓取和合并多个来源的 hosts 广告屏蔽规则
"""

import requests
import re
import os
import logging
from datetime import datetime
from typing import List, Set
import time

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('update.log'),
        logging.StreamHandler()
    ]
)

class HostsUpdater:
    def __init__(self):
        # 常用的 hosts 广告规则源
        self.sources = [
            {
                'name': 'StevenBlack/hosts',
                'url': 'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
                'description': '综合广告和恶意软件屏蔽'
            },
            {
                'name': 'AdguardTeam/AdguardFilters',
                'url': 'https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/adservers.txt',
                'description': 'Adguard 广告服务器列表'
            },
            {
                'name': 'privacy-protection-tools/anti-AD',
                'url': 'https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-domains.txt',
                'description': '中文广告域名屏蔽'
            },
            {
                'name': 'EasyList China',
                'url': 'https://easylist-downloads.adblockplus.org/easylistchina.txt',
                'description': 'EasyList 中国补充规则'
            },
            {
                'name': 'ChinaList AD',
                'url': 'https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt',
                'description': '中文网站广告过滤规则'
            }
        ]
        
        self.blocked_domains = set()
        self.stats = {
            'total_sources': len(self.sources),
            'successful_sources': 0,
            'total_domains': 0,
            'unique_domains': 0,
            'update_time': None
        }

    def fetch_hosts_from_url(self, url: str, source_name: str) -> Set[str]:
        """从URL获取hosts规则"""
        domains = set()
        try:
            logging.info(f"正在获取 {source_name} 的规则...")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            content = response.text
            
            # 解析不同格式的规则
            for line in content.split('\n'):
                line = line.strip()
                
                # 跳过注释行和空行
                if not line or line.startswith('#') or line.startswith('!'):
                    continue
                
                # 提取域名的不同模式
                domain = self.extract_domain(line)
                if domain:
                    domains.add(domain)
            
            logging.info(f"从 {source_name} 获取到 {len(domains)} 个域名")
            return domains
            
        except Exception as e:
            logging.error(f"获取 {source_name} 失败: {str(e)}")
            return set()

    def extract_domain(self, line: str) -> str:
        """从不同格式的规则中提取域名"""
        # 移除注释
        line = re.sub(r'#.*$', '', line).strip()
        
        # hosts 格式: 0.0.0.0 domain.com 或 127.0.0.1 domain.com
        hosts_match = re.match(r'^(?:0\.0\.0\.0|127\.0\.0\.1)\s+(.+)$', line)
        if hosts_match:
            domain = hosts_match.group(1).strip()
            return self.validate_domain(domain)
        
        # 纯域名格式
        if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', line):
            return self.validate_domain(line)
        
        # Adblock 格式: ||domain.com^ 或 ||domain.com
        adblock_match = re.match(r'^\|\|(.+?)[\^$]*$', line)
        if adblock_match:
            domain = adblock_match.group(1)
            # 移除路径部分，只保留域名
            domain = domain.split('/')[0]
            return self.validate_domain(domain)
        
        # EasyList 格式处理更多情况
        # 处理 @@||domain.com^ (白名单，跳过)
        if line.startswith('@@'):
            return None
            
        # 处理 domain.com## (元素隐藏规则，跳过)
        if '##' in line or '#@#' in line:
            return None
            
        # 处理 /regex/ 格式 (跳过正则表达式)
        if line.startswith('/') and line.endswith('/'):
            return None
        
        return None

    def validate_domain(self, domain: str) -> str:
        """验证域名格式"""
        if not domain:
            return None
            
        # 基本域名格式验证
        domain_pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$'
        
        if re.match(domain_pattern, domain) and len(domain) <= 253:
            # 排除本地域名和无效域名
            if not any(x in domain.lower() for x in ['localhost', '127.0.0.1', '0.0.0.0', 'local']):
                return domain.lower()
        
        return None

    def update_hosts(self):
        """更新 hosts 规则"""
        logging.info("开始更新 hosts 规则...")
        self.blocked_domains.clear()
        
        successful_sources = 0
        
        for source in self.sources:
            try:
                domains = self.fetch_hosts_from_url(source['url'], source['name'])
                if domains:
                    self.blocked_domains.update(domains)
                    successful_sources += 1
                    
                # 添加延迟避免请求过快
                time.sleep(2)
                
            except Exception as e:
                logging.error(f"处理源 {source['name']} 时出错: {str(e)}")
        
        # 更新统计信息
        self.stats.update({
            'successful_sources': successful_sources,
            'total_domains': len(self.blocked_domains),
            'unique_domains': len(self.blocked_domains),
            'update_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        })
        
        logging.info(f"规则更新完成! 共获取 {len(self.blocked_domains)} 个唯一域名")

    def generate_hosts_file(self) -> str:
        """生成 hosts 文件内容"""
        header = f"""# Hosts Ad Blocker Rules (Chinese Enhanced)
# 自动生成的广告屏蔽规则文件 (中文增强版)
# 更新时间: {self.stats['update_time']}
# 规则来源: {self.stats['successful_sources']}/{self.stats['total_sources']} 个源
# 屏蔽域名: {self.stats['unique_domains']} 个
#
# 使用方法:
# 1. 备份现有的 hosts 文件
# 2. 将此文件内容追加到系统 hosts 文件中
# 3. Windows: C:\\Windows\\System32\\drivers\\etc\\hosts
# 4. Linux/macOS: /etc/hosts
#
# 项目地址: https://github.com/your-username/hosts-ad-blocker
# ============================================================

"""
        
        # 添加基本的本地解析
        content = header + """# 本地解析
127.0.0.1 localhost
127.0.0.1 localhost.localdomain
127.0.0.1 local
255.255.255.255 broadcasthost
::1 localhost
::1 ip6-localhost
::1 ip6-loopback
fe80::1%lo0 localhost

# ============================================================
# 广告和恶意软件屏蔽规则 (中文增强版)
# ============================================================

"""
        
        # 按字母顺序排序域名
        sorted_domains = sorted(self.blocked_domains)
        
        for domain in sorted_domains:
            content += f"0.0.0.0 {domain}\n"
        
        return content

    def save_hosts_file(self, filename: str = 'hosts'):
        """保存 hosts 文件"""
        content = self.generate_hosts_file()
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logging.info(f"hosts 文件已保存为 {filename}")
            
            # 保存统计信息
            self.save_stats()
            
        except Exception as e:
            logging.error(f"保存 hosts 文件失败: {str(e)}")

    def save_stats(self):
        """保存更新统计信息"""
        stats_content = f"""# Hosts Ad Blocker 更新统计 (中文增强版)

**最后更新时间**: {self.stats['update_time']}

**规则源状态**: {self.stats['successful_sources']}/{self.stats['total_sources']} 个源成功获取

**屏蔽域名数量**: {self.stats['unique_domains']} 个

## 规则来源

"""
        
        for i, source in enumerate(self.sources, 1):
            stats_content += f"{i}. **{source['name']}** - {source['description']}\n"
            stats_content += f"   - URL: {source['url']}\n\n"
        
        try:
            with open('README_STATS.md', 'w', encoding='utf-8') as f:
                f.write(stats_content)
        except Exception as e:
            logging.error(f"保存统计信息失败: {str(e)}")

def main():
    """主函数"""
    try:
        updater = HostsUpdater()
        updater.update_hosts()
        updater.save_hosts_file()
        
        logging.info("=" * 50)
        logging.info("更新完成!")
        logging.info(f"成功源: {updater.stats['successful_sources']}/{updater.stats['total_sources']}")
        logging.info(f"屏蔽域名: {updater.stats['unique_domains']} 个")
        logging.info("=" * 50)
        
    except Exception as e:
        logging.error(f"更新过程中出现错误: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
