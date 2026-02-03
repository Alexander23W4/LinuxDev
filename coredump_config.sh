#!/bin/bash
# 永久开启传统 core dump（开发环境标准）
set -e

echo "配置 core dump 永久文件模式..."

# core_pattern
sudo bash -c 'echo "kernel.core_pattern = core.%e.%p.%t" >> /etc/sysctl.conf'
sudo sysctl -p

# core 大小限制
sudo bash -c 'cat >> /etc/security/limits.conf << "EOF"
* soft core unlimited
* hard core unlimited
EOF'

echo "✓ 配置完成！重启/重新登录后生效"
echo "验证命令：cat /proc/sys/kernel/core_pattern && ulimit -c"


