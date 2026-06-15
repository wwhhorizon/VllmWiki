# vllm-project/vllm#3358: Does 'all-reduce kernels are temporarily disabled' is the cause for the more memory requirment?

| 字段 | 值 |
| --- | --- |
| Issue | [#3358](https://github.com/vllm-project/vllm/issues/3358) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support |
| 子分类 |  |
| Operator 关键词 | cache;kernel |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Does 'all-reduce kernels are temporarily disabled' is the cause for the more memory requirment?

### Issue 正文摘录

Hello, I used to use vllm to work with codellama2 13B using only 2 NVIDIA L4 GPU. The engine setup as follow: python -m vllm.entrypoints.openai.api_server --model="codellama/CodeLlama-13b-Instruct-hf" --tensor-parallel-size=2 Recently, it does not work and shows as follow: ValueError: The model's max seq len (16384) is larger than the maximum number of tokens that can be stored in KV cache (14528). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. Thus, I increase the gpu_memory_utilization to 0.95 and it works. However, I need to know how much it was so I can see if I need to redo my experiments again or can mitigate this change. Moreover, does the increase in memory need is due to the following: Custom all-reduce kernels are temporarily disabled due to stability issues. We will re-enable them once the problems are resolved.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ore memory requirment? stale Hello, I used to use vllm to work with codellama2 13B using only 2 NVIDIA L4 GPU. The engine setup as follow: python -m vllm.entrypoints.openai.api_server --model="codellama/CodeLlama-13b-In...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e attention_kv_cache;distributed_parallel;model_support cache;kernel env_dependency;shape Hello,
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 16384) is larger than the maximum number of tokens that can be stored in KV cache (14528). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. Thus, I increase the gpu_mem...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: s are temporarily disabled' is the cause for the more memory requirment? stale Hello, I used to use vllm to work with codellama2 13B using only 2 NVIDIA L4 GPU. The engine setup as follow: python -m vllm.entrypoints.ope...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
