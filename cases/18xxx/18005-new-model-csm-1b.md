# vllm-project/vllm#18005: [New Model]: CSM 1b

| 字段 | 值 |
| --- | --- |
| Issue | [#18005](https://github.com/vllm-project/vllm/issues/18005) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: CSM 1b

### Issue 正文摘录

### The model to consider. It would be nice to support csm 1b, a very cool tts model that just got recent support in transformers. It has 2 llama type autoregressive models(1b and 100m) that can be optimized with vllm. Csm support pr: https://github.com/huggingface/transformers/pull/36719 Transformers model: https://huggingface.co/eustlb/csm-1b ### The closest model vllm already supports. Llama as csm has 2 llama type models. ### What's your difficulty of supporting the model you want? Should not be very difficult as it’s llama architecture with some processing. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: CSM 1b stale ### The model to consider. It would be nice to support csm 1b, a very cool tts model that just got recent support in transformers. It has 2 llama type autoregressive models(1b and 100m) that ca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [New Model]: CSM 1b stale ### The model to consider. It would be nice to support csm 1b, a very cool tts model that just got recent support in transformers. It has 2 llama type autoregressive models(1b and 100m) that ca...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: CSM 1b stale ### The model to consider. It would be nice to support csm 1b, a very cool tts model that just got recent support in transformers. It has 2 llama type autoregressive models(1b and 100m) that ca...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
