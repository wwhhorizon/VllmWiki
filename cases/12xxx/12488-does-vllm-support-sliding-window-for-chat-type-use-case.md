# vllm-project/vllm#12488: Does vLLM support Sliding Window for chat type use case?

| 字段 | 值 |
| --- | --- |
| Issue | [#12488](https://github.com/vllm-project/vllm/issues/12488) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Does vLLM support Sliding Window for chat type use case?

### Issue 正文摘录

> > https://docs.vllm.ai/en/latest/models/performance.html Decrease **max_num_seqs** or max_num_batched_tokens. This can reduce the number of concurrent requests in a batch, thereby requiring less KV cache space. > > https://docs.vllm.ai/en/latest/models/engine_args.html --**max-model-len** Model context length. If unspecified, will be automatically derived from the model config. > > Thank you for your reply. If max-model-len is set to 8192, is the latest 8192 characters always set as context? That is, no matter how long the user input is, vllm always intercepts the length of the max-model-len processing behind it. > > The sliding window mechanism you are talking about, can anyone confirm if vLLM has implemented it? I see a vLLM engine argument, > > --disable-sliding-window > Disables sliding window, capping to sliding window size. > > Which leaves me with an assumption that sliding window is implemented. But when I use any model (for example, Qwen/Qwen2.5-Coder-32B-Instruct-AWQ) from Open-WebUI or Continue.dev (vs code extension), whenever I approach --max-model-len vLLM throws an error like so. > > ``` > ERROR 01-27 12:14:24 serving_chat.py:181] raise ValueError( > ERROR 01-27 1...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Window for chat type use case? stale > > https://docs.vllm.ai/en/latest/models/performance.html Decrease **max_num_seqs** or max_num_batched_tokens. This can reduce the number of concurrent requests in a batch, thereby...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Does vLLM support Sliding Window for chat type use case? stale > > https://docs.vllm.ai/en/latest/models/performance.html Decrease **max_num_seqs** or max_num_batched_tokens. This can reduce the number of concurrent req...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: odels/engine_args.html --**max-model-len** Model context length. If unspecified, will be automatically derived from the model config. > > Thank you for your reply. If max-model-len is set to 8192, is the latest 8192 cha...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: f the max-model-len processing behind it. > > The sliding window mechanism you are talking about, can anyone confirm if vLLM has implemented it? I see a vLLM engine argument, > > --disable-sliding-window > Disables slid...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: uce the number of concurrent requests in a batch, thereby requiring less KV cache space. > > https://docs.vllm.ai/en/latest/models/engine_args.html --**max-model-len** Model context length. If unspecified, will be autom...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
