# vllm-project/vllm#38182: [Bug]: Based on Qwen3.5-35B-A3B, why does enabling MTP speculative decoding actually reduce the prefix cache hit rate?

| 字段 | 值 |
| --- | --- |
| Issue | [#38182](https://github.com/vllm-project/vllm/issues/38182) |
| 状态 | open |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Based on Qwen3.5-35B-A3B, why does enabling MTP speculative decoding actually reduce the prefix cache hit rate?

### Issue 正文摘录

### Your current environment My ENV： +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 570.133.20 Driver Version: 570.133.20 CUDA Version: 12.8 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA H20-3e On | 00000000:08:00.0 Off | 0 | | N/A 41C P0 121W / 500W | 131191MiB / 143771MiB | 0% Default | | | | Disabled | +-----------------------------------------+------------------------+----------------------+ +-----------------------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=========================================================================================| | 0 N/A N/A 99363 C VLLM::EngineCore 13118... | +-----------------------------------------------------------------------------------------+ ### 🐛 Describe the bug Based on Qwen3.5...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ----------------------------+ | NVIDIA-SMI 570.133.20 Driver Version: 570.133.20 CUDA Version: 12.8 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: --------------------------------------------------------------+ | NVIDIA-SMI 570.133.20 Driver Version: 570.133.20 CUDA Version: 12.8 | |-----------------------------------------+------------------------+---------------...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: -35B-A3B, why does enabling MTP speculative decoding actually reduce the prefix cache hit rate? bug ### Your current environment My ENV： +---------------------------------------------------------------------------------...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Based on Qwen3.5-35B-A3B, why does enabling MTP speculative decoding actually reduce the prefix cache hit rate? bug ### Your current environment My ENV： +----------------------------------------------------------...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Based on Qwen3.5-35B-A3B, why does enabling MTP speculative decoding actually reduce the prefix cache hit rate? bug ### Your current environment My ENV： +----------------------------------------------------------...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
