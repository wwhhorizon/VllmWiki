# vllm-project/vllm#20265: [RFC]: Online inference benchmark tool for multi-turn conversations

| 字段 | 值 |
| --- | --- |
| Issue | [#20265](https://github.com/vllm-project/vllm/issues/20265) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Online inference benchmark tool for multi-turn conversations

### Issue 正文摘录

### Motivation. With the recent addition of the KV Connector API ([PR #15960](https://github.com/vllm-project/vllm/pull/15960)) and the growing adoption of KV cache offloading strategies, there is an increasing need for benchmarking tools that simulate realistic multi-turn chat interactions. KV cache offloading works best when cached data can be reused, but still needs to be retrieved from the offloading backend. This approach is particularly beneficial for multi-turn conversations, which rely on KV cache reuse. However, even with APC enabled, long pauses between conversation turns often cause the necessary KV blocks to be evicted from GPU memory. Currently, the vLLM library lacks a dedicated benchmarking suite that emulates realistic full-session conversations, including system prompts and chat history. This RFC proposes a benchmark tool that simulates real-world, multi-client behavior using REST API calls (OpenAI API). It measures key performance metrics such as: * Time to First Token (TTFT). * Time Per Output Token (TPOT). * End-to-End Latency. * Throughput (requests per second). This tool is designed to: * Identify performance bottlenecks in cache-heavy deployments. * Evaluate...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: [RFC]: Online inference benchmark tool for multi-turn conversations RFC ### Motivation. With the recent addition of the KV Connector API ([PR #15960](https://github.com/vllm-project/vllm/pull/15960)) and the growing ado...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: ://github.com/vllm-project/vllm/pull/15960)) and the growing adoption of KV cache offloading strategies, there is an increasing need for benchmarking tools that simulate realistic multi-turn chat interactions. KV cache...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: data can be reused, but still needs to be retrieved from the offloading backend. This approach is particularly beneficial for multi-turn conversations, which rely on KV cache reuse. However, even with APC enabled, long...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: led, long pauses between conversation turns often cause the necessary KV blocks to be evicted from GPU memory. Currently, the vLLM library lacks a dedicated benchmarking suite that emulates realistic full-session conver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: prompt/response (`--print-content`). - Saves updated conversations with model completions (`--output-file`). - Optional answer verification against expected dataset responses (`--verify-output`). (Should be used with te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
