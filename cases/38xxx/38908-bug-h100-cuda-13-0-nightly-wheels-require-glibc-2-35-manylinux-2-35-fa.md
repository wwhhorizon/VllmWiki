# vllm-project/vllm#38908: [Bug]: H100 CUDA 13.0 nightly wheels require glibc 2.35 (manylinux_2_35), failing on glibc 2.34 systems

| 字段 | 值 |
| --- | --- |
| Issue | [#38908](https://github.com/vllm-project/vllm/issues/38908) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: H100 CUDA 13.0 nightly wheels require glibc 2.35 (manylinux_2_35), failing on glibc 2.34 systems

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, I am tyring to install the vllm nightly wheels for cuda130 using Python 3.12. However, the installation fails because the cu130 wheels are compiled against glibc 2.35 (tagged manylinux_2_35), making them incompatible with operating systems running glibc 2.34 (such as RHEL 9, Rocky Linux 9, or AlmaLinux 9). Some HPC clusters are not allowed to use docker. Command to reproduce: ``` uv pip install -U vllm \ --force-reinstall \ --torch-backend=auto \ --extra-index-url https://wheels.vllm.ai/nightly/cu130 ``` Output: ``` × No solution found when resolving dependencies: ╰─▶ Because only vllm==0.18.2rc1.dev79+g3bc2734dd.cu130 is available and vllm==0.18.2rc1.dev79+g3bc2734dd.cu130 has no wheels with a matching platform tag (e.g., `manylinux_2_34_x86_64`), we can conclude that all versions of vllm cannot be used. And because you require vllm, we can conclude that your requirements are unsatisfiable. hint: `vllm` was requested with a pre-release marker (e.g., all of: vllm 0.18.2rc1.dev79+g3bc2734dd.cu130 ), but pre-releases weren't enabled (try: `--prerelease=allow`) hint: `vllm` was found on https://wheels.vllm.ai/nightly/cu130, b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Bug]: H100 CUDA 13.0 nightly wheels require glibc 2.35 (manylinux_2_35), failing on glibc 2.34 systems bug ### Your current environment ### 🐛 Describe the bug Hello, I am tyring to install the vllm nightly wheels for c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: H100 CUDA 13.0 nightly wheels require glibc 2.35 (manylinux_2_35), failing on glibc 2.34 systems bug ### Your current environment ### 🐛 Describe the bug Hello, I am tyring to install the vllm nightly wheels for c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: reproduce: ``` uv pip install -U vllm \ --force-reinstall \ --torch-backend=auto \ --extra-index-url https://wheels.vllm.ai/nightly/cu130 ``` Output: ``` × No solution found when resolving dependencies: ╰─▶ Because only...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: aLinux 9). Some HPC clusters are not allowed to use docker. Command to reproduce: ``` uv pip install -U vllm \ --force-reinstall \ --torch-backend=auto \ --extra-index-url https://wheels.vllm.ai/nightly/cu130 ``` Output...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nclude that your requirements are unsatisfiable. hint: `vllm` was requested with a pre-release marker (e.g., all of: vllm 0.18.2rc1.dev79+g3bc2734dd.cu130 ), but pre-releases weren't enabled (try: `--prerelease=allow`)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
