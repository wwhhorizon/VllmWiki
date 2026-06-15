# vllm-project/vllm#8719: [Misc]: Uneven performance

| 字段 | 值 |
| --- | --- |
| Issue | [#8719](https://github.com/vllm-project/vllm/issues/8719) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: Uneven performance

### Issue 正文摘录

### Anything you want to discuss about vllm. I'm using VLLM on NVIDIA A100 as: ``` vllm serve iqbalamo93/Meta-Llama-3.1-8B-Instruct-GPTQ-Q_8 --dtype auto --api-key none --port 6666 --max-model-len 16384 --gpu_memory_utilization 0.6 --enable-prefix-caching --use-v2-block-manager --enable-chunked-prefill --max-num-batched-tokens 1024 --disable-log-requests ``` This is a batch operation, with the same CoT prompt analyzing different texts with very different sizes, so I'm not sure if that hinders the performance. The first turn of the chat is always the same so prompt caching should play a big deal (and it does). However, both the prompt throughput and the generation throughput vary a lot. GPU usage as measured by `nvtop` also varies a lot - it's rarely 100% and on occasion dips to 60%. Messages are being fed to the vllm's OpenAI API with fast producers that can saturate anything, so I think the number of messages in Pending should be maxed-out, not varying like it does. Here's a portion from the logs. ``` Sep 22 23:46:41 ml2-1-a100-1 vllm[361682]: INFO: 127.0.0.1:58286 - "POST /v1/chat/completions Sep 22 23:46:42 ml2-1-a100-1 vllm[361991]: INFO 09-22 23:46:42 metrics.py:351] Avg prom...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tion 0.6 --enable-prefix-caching --use-v2-block-manager --enable-chunked-prefill --max-num-batched-tokens 1024 --disable-log-requests ``` This is a batch operation, with the same CoT prompt analyzing different texts wit...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 100 as: ``` vllm serve iqbalamo93/Meta-Llama-3.1-8B-Instruct-GPTQ-Q_8 --dtype auto --api-key none --port 6666 --max-model-len 16384 --gpu_memory_utilization 0.6 --enable-prefix-caching --use-v2-block-manager --enable-ch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e ### Anything you want to discuss about vllm. I'm using VLLM on NVIDIA A100 as: ``` vllm serve iqbalamo93/Meta-Llama-3.1-8B-Instruct-GPTQ-Q_8 --dtype auto --api-key none --port 6666 --max-model-len 16384 --gpu_memory_u...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: 230.6 tokens/s, Running: 16 reqs, Swapped: 0 reqs, Pending: 11 reqs, GPU KV cache usage: 87.1%, CPU KV cache usage: 0.0%. Sep 22 23:46:42 ml2-1-a100-1 vllm[361991]: INFO 09-22 23:46:42 metrics.py:367] Prefix cache hit r...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: -len 16384 --gpu_memory_utilization 0.6 --enable-prefix-caching --use-v2-block-manager --enable-chunked-prefill --max-num-batched-tokens 1024 --disable-log-requests ``` This is a batch operation, with the same CoT promp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
