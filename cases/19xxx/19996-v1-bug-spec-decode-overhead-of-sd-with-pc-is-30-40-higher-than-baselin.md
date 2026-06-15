# vllm-project/vllm#19996: [V1][Bug][Spec Decode]: Overhead of SD with PC is 30-40% higher than baseline

| 字段 | 值 |
| --- | --- |
| Issue | [#19996](https://github.com/vllm-project/vllm/issues/19996) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cache |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [V1][Bug][Spec Decode]: Overhead of SD with PC is 30-40% higher than baseline

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Setup: * H100 80GB * llama 3.1 8b * MTBench It seems that overhead of eagle on ttft is 30-40% especially in cases when Prompt caching benefits the model with good cache hits. mtbench | ttft (ms) | | -- | -- | -- | -- BS | baseline | eagle | Degradation BS 4 - first run | 14.55 | 18.77 | 1.290034364 BS 4 - repeat run | 14.26 | 18.56 | 1.301542777 `BS 4 first run` means BS is 4 and for a freshly started server we send the MTBench dataset once. `BS 4 repeat run` means BS is 4 and for the same server we send the MTBench dataset again. The hope is that the ttft of `4 repeat run` will be much lower than `4 first run` since the server has processed MTBench once already. Serve log contains this > INFO 06-23 14:21:48 [gpu_worker.py:232] Available KV cache memory: 51.63 GiB INFO 06-23 14:21:48 [kv_cache_utils.py:716] GPU KV cache size: 410,128 tokens INFO 06-23 14:21:48 [kv_cache_utils.py:720] Maximum concurrency for 131,072 tokens per request: 3.13x which means the kv cache can store 400k unique tokens. MTBench has 80 prompts and total context tokens in this dataset is 8k. With generating 100 tokens per prompt, total tokens that would res...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [V1][Bug][Spec Decode]: Overhead of SD with PC is 30-40% higher than baseline bug ### Your current environment ### 🐛 Describe the bug Setup: * H100 80GB * llama 3.1 8b * MTBench It seems that overhead of eagle on ttft i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 3.1 8b * MTBench It seems that overhead of eagle on ttft is 30-40% especially in cases when Prompt caching benefits the model with good cache hits. mtbench | ttft (ms) | | -- | -- | -- | -- BS | baseline | eagle | Degra...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: our current environment ### 🐛 Describe the bug Setup: * H100 80GB * llama 3.1 8b * MTBench It seems that overhead of eagle on ttft is 30-40% especially in cases when Prompt caching benefits the model with good cache hit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ne bug ### Your current environment ### 🐛 Describe the bug Setup: * H100 80GB * llama 3.1 8b * MTBench It seems that overhead of eagle on ttft is 30-40% especially in cases when Prompt caching benefits the model with go...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: generating 100 tokens per prompt, total tokens that would reside in the block pool would be 8k + 80*100 = 16k which is less than 400k tokens. However, 1. ttft has 2 component: a. prefill b. scheduler/sampler/other overh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
