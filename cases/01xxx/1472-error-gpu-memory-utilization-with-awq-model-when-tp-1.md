# vllm-project/vllm#1472: Error gpu memory utilization with awq model when tp>1.

| 字段 | 值 |
| --- | --- |
| Issue | [#1472](https://github.com/vllm-project/vllm/issues/1472) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Error gpu memory utilization with awq model when tp>1.

### Issue 正文摘录

Right now vLLM will allocate 90% gpu memory for each accessible gpu card, but when launch server with awq model, it will became a unknow behavior. I run awq format codellama-13b(6.8GB) model on L4(24GB) and A40(48GB), and the gpu memory utilization is different, and `----gpu-memory-utilization` and `--swap-space` parameter is invalid in this situation. On L4(24GB) it will pre-allocate ~10GB gpu memory: ![image](https://github.com/vllm-project/vllm/assets/37237570/75feecb3-c5fd-44da-8b3b-145c33e56932) And when I send a request, it will increase ~2GB, the gpu memory usage come to ~12GB: ![image](https://github.com/vllm-project/vllm/assets/37237570/1792ef25-5498-4407-be7a-b201a7d5b92c) On A40(48GB) it will pre-allocate ~31GB gpu memory: ![image](https://github.com/vllm-project/vllm/assets/37237570/7466b9ea-8bb9-4ef4-bac9-045259bbba60) And when I send the same request that I sent to L4, it will also increase ~2GB, the gpu memory usage come to ~33GB: ![image](https://github.com/vllm-project/vllm/assets/37237570/61b39fbf-cb5c-4ced-ba56-6128d3c4acdc) The only pattern I found in the phenomenon is they both allocate 1946MB gpu memory after I send a request to the server. In general, vLLM w...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Error gpu memory utilization with awq model when tp>1. Right now vLLM will allocate 90% gpu memory for each accessible gpu card, but when launch server with awq model, it will became a unknow behavior. I run awq format...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: /assets/37237570/75feecb3-c5fd-44da-8b3b-145c33e56932) And when I send a request, it will increase ~2GB, the gpu memory usage come to ~12GB: ![image](https://github.com/vllm-project/vllm/assets/37237570/1792ef25-5498-44...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: Error gpu memory utilization with awq model when tp>1. Right now vLLM will allocate 90% gpu memory for each accessible gpu card, but when launch server with awq model, it will became a unknow behavior. I run awq format...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ct/vllm/assets/37237570/f299895c-82b3-4e11-bfa4-95df4f257f80) But can't reproduce this on llama-2-13b-hf awq model. @WoosukKwon @zhuohan123 Do you have any ideads about this issue? performance attention_kv_cache;distrib...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: mance attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory cache;quantization Right now vLLM will allocate 90% gpu memory for each accessible gpu card, but when launch server...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
