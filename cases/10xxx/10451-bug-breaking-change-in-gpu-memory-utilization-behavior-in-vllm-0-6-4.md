# vllm-project/vllm#10451: [Bug]: Breaking Change in `gpu_memory_utilization` Behavior in vLLM 0.6.4

| 字段 | 值 |
| --- | --- |
| Issue | [#10451](https://github.com/vllm-project/vllm/issues/10451) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Breaking Change in `gpu_memory_utilization` Behavior in vLLM 0.6.4

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We encountered significant changes in the behavior of the `gpu_memory_utilization` parameter between vLLM 0.6.3 and vLLM 0.6.4. This change has introduced challenges in deploying multiple models on a shared GPU due to how memory usage is calculated and allocated. In vLLM 0.6.3, `gpu_memory_utilization` acted as a limit for the memory used by the model itself, making it easier to allocate resources for multiple models running on the same GPU. However, in vLLM 0.6.4, the behavior of this parameter was altered to act as a global GPU memory utilization limit. This change fundamentally impacts scenarios where multiple models are deployed, as it now accounts for all GPU memory usage, including memory allocated by other processes. The way `peak_memory` is calculated differs significantly between versions, leading to discrepancies in GPU memory management. --- #### **Peak Memory Calculations** 1. **vLLM 0.6.3** In vLLM 0.6.3, the `peak_memory` is calculated as: ```python peak_memory = self.init_gpu_memory - free_gpu_memory ``` - `init_gpu_memory`: Memory used by the GPU before vLLM starts. - `free_gpu_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: sses. The way `peak_memory` is calculated differs significantly between versions, leading to discrepancies in GPU memory management. --- #### **Peak Memory Calculations** 1. **vLLM 0.6.3** In vLLM 0.6.3, the `peak_memor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nclude all GPU memory allocations: ```python peak_memory = torch.cuda.memory_stats()["allocated_bytes.all.peak"] # Include non-Torch memory allocations torch.cuda.empty_cache() torch_allocated_bytes = torch.cuda.memory_...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: LLM 0.6.4, the behavior of this parameter was altered to act as a global GPU memory utilization limit. This change fundamentally impacts scenarios where multiple models are deployed, as it now accounts for all GPU memor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: on_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory;speculative_decoding cache;cuda;operator;triton build_error env_dependency Your current environment
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ;model_support;scheduler_memory;speculative_decoding cache;cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
