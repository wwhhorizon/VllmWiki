# vllm-project/vllm#35295: [Bugfix Proposal]: Support MIG UUIDs in CUDA_VISIBLE_DEVICES (int() conversion and NVML handle resolution)

| 字段 | 值 |
| --- | --- |
| Issue | [#35295](https://github.com/vllm-project/vllm/issues/35295) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bugfix Proposal]: Support MIG UUIDs in CUDA_VISIBLE_DEVICES (int() conversion and NVML handle resolution)

### Issue 正文摘录

### Your current environment 5.14.0-611.27.1.el9_7.x86_64 / RHEL 9.7 (Plow) Python 3.9.25 ### 🐛 Describe the bug Hi team, I’ve reproduced a crash in vLLM 0.15.1 when running on NVIDIA MIG slices with CUDA_VISIBLE_DEVICES set to a MIG UUID (e.g., MIG-xxxx). This appears to affect both single and multi-instance GPU setups. Root cause: In interface.py, vLLM attempts to convert device IDs from CUDA_VISIBLE_DEVICES to int(). This fails for MIG UUIDs, which are strings like MIG-xxxx, resulting in a ValueError. In cuda.py, vLLM uses MIG UUIDs directly as NVML handles. However, for MIG devices, NVML requires resolving the parent GPU handle first before accessing the MIG slice. Proposed fix: In interface.py, detect device IDs starting with "MIG-" and skip the int() conversion, returning the string as-is. In cuda.py, when a device ID starts with "MIG-", resolve the parent GPU handle before using the MIG UUID in NVML calls. This should address this bug as well as related issues such as [#6551](https://github.com/vllm-project/vllm/issues/6551) and [#17047](https://github.com/vllm-project/vllm/issues/17047). I am preparing a minimal, upstream-friendly PR and will link it here once ready. ### B...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bugfix Proposal]: Support MIG UUIDs in CUDA_VISIBLE_DEVICES (int() conversion and NVML handle resolution) bug ### Your current environment 5.14.0-611.27.1.el9_7.x86_64 / RHEL 9.7 (Plow) Python 3.9.25 ### 🐛 Describe the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bugfix Proposal]: Support MIG UUIDs in CUDA_VISIBLE_DEVICES (int() conversion and NVML handle resolution) bug ### Your current environment 5.14.0-611.27.1.el9_7.x86_64 / RHEL 9.7 (Plow) Python 3.9.25 ### 🐛 Describe the...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: / RHEL 9.7 (Plow) Python 3.9.25 ### 🐛 Describe the bug Hi team, I’ve reproduced a crash in vLLM 0.15.1 when running on NVIDIA MIG slices with CUDA_VISIBLE_DEVICES set to a MIG UUID (e.g., MIG-xxxx). This appears to affe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development cuda crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
