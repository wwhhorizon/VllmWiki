# vllm-project/vllm#5176: [Usage]:  Prefix caching in VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#5176](https://github.com/vllm-project/vllm/issues/5176) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  Prefix caching in VLLM

### Issue 正文摘录

Can anyone help me with these doubts 1)When i launch open ai compatible VLLM server `python3 -m vllm.entrypoints.openai.api_server --model TheBloke/Mistral-7B-Instruct-v0.2-AWQ --max-model-len 32768 --gpu-memory-utilization 0.8 --quantization awq --enable-prefix-caching` prefix caching is working when i send a batch of requests but not across multiple requests,I observed the GPU KV cache is offloading to 0% immediately after a request is done,Am i missing anything here? 2)Instead of LRU approach can LFU approach be implemented for prefix caching,what would be drawbacks if so? 3)I want to configure my KV cache with a list of prefixes at server startup and prevent offloading them until the server is stopped. Is this possible? Thanks in advance

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: a batch of requests but not across multiple requests,I observed the GPU KV cache is offloading to 0% immediately after a request is done,Am i missing anything here? 2)Instead of LRU approach can LFU approach be implemen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: compatible VLLM server `python3 -m vllm.entrypoints.openai.api_server --model TheBloke/Mistral-7B-Instruct-v0.2-AWQ --max-model-len 32768 --gpu-memory-utilization 0.8 --quantization awq --enable-prefix-caching` prefix c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Prefix caching in VLLM usage;stale Can anyone help me with these doubts 1)When i launch open ai compatible VLLM server `python3 -m vllm.entrypoints.openai.api_server --model TheBloke/Mistral-7B-Instruct-v0.2-AW...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: B-Instruct-v0.2-AWQ --max-model-len 32768 --gpu-memory-utilization 0.8 --quantization awq --enable-prefix-caching` prefix caching is working when i send a batch of requests but not across multiple requests,I observed th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
