# vllm-project/vllm#24875: [Bug]: ARM CPU no longer builds (and x86_64 I think), cmake version issues

| 字段 | 值 |
| --- | --- |
| Issue | [#24875](https://github.com/vllm-project/vllm/issues/24875) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ARM CPU no longer builds (and x86_64 I think), cmake version issues

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug https://github.com/ericcurtin/staging/blob/master/build-vllm.sh ``` ./build-vllm.sh generic + source lib.sh + local containerfile=generic + '[' generic '!=' generic ']' + local uname_m ++ uname -m + uname_m=aarch64 + install_deps + available dnf + command -v dnf + dnf install -y git wget ca-certificates gcc gcc-c++ libSM libXext mesa-libGL jq lsof vim numactl Updating and loading repositories: Repositories loaded. Package "git-2.51.0-2.fc42.aarch64" is already installed. Package "ca-certificates-2024.2.69_v8.0.401-6.fc42.noarch" is already installed. Package "gcc-15.2.1-1.fc42.aarch64" is already installed. Package "gcc-c++-15.2.1-1.fc42.aarch64" is already installed. Package "libSM-1.2.5-2.fc42.aarch64" is already installed. Package "libXext-1.3.6-3.fc42.aarch64" is already installed. Package "mesa-libGL-25.1.7-1.fc42.aarch64" is already installed. Package "jq-1.7.1-11.fc42.aarch64" is already installed. Package "lsof-4.98.0-7.fc42.aarch64" is already installed. Package "vim-enhanced-2:9.1.1723-2.fc42.aarch64" is already installed. Package Arch Version Repository Size Installing: numactl aarch64 2.0.19-2.fc42 fedora 417.2 KiB wg...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: ARM CPU no longer builds (and x86_64 I think), cmake version issues bug ### Your current environment ### 🐛 Describe the bug https://github.com/ericcurtin/staging/blob/master/build-vllm.sh ``` ./build-vllm.sh gene...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ic + '[' generic '!=' generic ']' + local uname_m ++ uname -m + uname_m=aarch64 + install_deps + available dnf + command -v dnf + dnf install -y git wget ca-certificates gcc gcc-c++ libSM libXext mesa-libGL jq lsof vim...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nt: Disable this message with "git config set advice.defaultBranchName false" Initialized empty Git repository in /vllm/.git/ + cd vllm + git remote add origin https://github.com/vllm-project/vllm + git fetch --depth 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t >>> /usr/lib/sysusers.d/20-setup-groups.conf:30: Conflict with earlier configura >>> /usr/lib/sysusers.d/20-setup-users.conf:13: Conflict with earlier configurat >>> /usr/lib/sysusers.d/chrony.conf:2: Conflict with ea...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: .13-linux-aarch64-gnu/bin/python3.11`: system interpreter not explicitly requested DEBUG Found `cpython-3.11.13-linux-aarch64-gnu` at `/opt/venv/bin/python` (first executable in the search path) Using Python 3.11.13 env...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
