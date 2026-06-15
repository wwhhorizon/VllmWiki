# vllm-project/vllm#43412: [Bug]: When will the RTX Pro 6000 support the deepseek-v4-flash model? There are too many versions of the vLLM framework right now, and I’m wondering when a vLLM image specifically optimized for the Pro 6000 will be released.

| 字段 | 值 |
| --- | --- |
| Issue | [#43412](https://github.com/vllm-project/vllm/issues/43412) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When will the RTX Pro 6000 support the deepseek-v4-flash model? There are too many versions of the vLLM framework right now, and I’m wondering when a vLLM image specifically optimized for the Pro 6000 will be released.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug root@user:/data# nvidia-smi Fri May 22 17:13:39 2026 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 580.95.05 Driver Version: 580.95.05 CUDA Version: 13.0 | +-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA RTX PRO 6000 Blac... Off | 00000000:16:00.0 Off | 0 | | N/A 27C P8 40W / 600W | 14MiB / 97887MiB | 0% Default | | | | Disabled | +-----------------------------------------+------------------------+----------------------+ | 1 NVIDIA RTX PRO 6000 Blac... Off | 00000000:27:00.0 Off | 0 | | N/A 27C P8 161W / 600W | 14MiB / 97887MiB | 0% Default | | | | Disabled | +-----------------------------------------+------------------------+----------------------+ | 2 NVIDIA RTX PRO 6000 Blac... Off | 00000000:98:00.0 Off | 0 | | N/A 26C P8 37W / 600W | 14MiB / 97887MiB | 0% Default | | | | Disa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: the RTX Pro 6000 support the deepseek-v4-flash model? There are too many versions of the vLLM framework right now, and I’m wondering when a vLLM image specifically optimized for the Pro 6000 will be released. bug ### Yo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: When will the RTX Pro 6000 support the deepseek-v4-flash model? There are too many versions of the vLLM framework right now, and I’m wondering when a vLLM image specifically optimized for the Pro 6000 will be rel...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: GI CI PID Type Process name GPU Memory | | ID ID Usage | |=========================================================================================| | 0 N/A N/A
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: When will the RTX Pro 6000 support the deepseek-v4-flash model? There are too many versions of the vLLM framework right now, and I’m wondering when a vLLM image specifically optimized for the Pro 6000 will be rel...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance ci_build;model_support cuda env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
