# vllm-project/vllm#15123: [RFC]: layer-wise kv cache offloading to enable larger batches

| 字段 | 值 |
| --- | --- |
| Issue | [#15123](https://github.com/vllm-project/vllm/issues/15123) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: layer-wise kv cache offloading to enable larger batches

### Issue 正文摘录

### Motivation. I tested on some large models like qwen-32B on H100. There are totally 64 layers. The compute cost for each layer is about 470 μs, and the transfer of the kv cache tensor for a layer is 10 ms. If we offload the gpu kv cache to cpu, and load it back ahead of 32 layers, we can enable double batches. Is there anyone doing the same thing? I draw a picture with 6 layers and 2 blocks share the same gpu cache. ![Image](https://github.com/user-attachments/assets/0f871ced-0b0c-4b05-be48-8bfce2a619c9) ### Proposed Change. The kv cache manager and the attention layer ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: FC;stale ### Motivation. I tested on some large models like qwen-32B on H100. There are totally 64 layers. The compute cost for each layer is about 470 μs, and the transfer of the kv cache tensor for a layer is 10 ms. I...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [RFC]: layer-wise kv cache offloading to enable larger batches RFC;stale ### Motivation. I tested on some large models like qwen-32B on H100. There are totally 64 layers. The compute cost for each layer is about 470 μs,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: enable larger batches RFC;stale ### Motivation. I tested on some large models like qwen-32B on H100. There are totally 64 layers. The compute cost for each layer is about 470 μs, and the transfer of the kv cache tensor...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: here anyone doing the same thing? I draw a picture with 6 layers and 2 blocks share the same gpu cache. ![Image](https://github.com/user-attachments/assets/0f871ced-0b0c-4b05-be48-8bfce2a619c9) ### Proposed Change. The...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: layer-wise kv cache offloading to enable larger batches RFC;stale ### Motivation. I tested on some large models like qwen-32B on H100. There are totally 64 layers. The compute cost for each layer is about 470 μs,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
