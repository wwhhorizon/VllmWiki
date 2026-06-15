# vllm-project/vllm#18156: [Bug]: Can't serve Qwen3-AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#18156](https://github.com/vllm-project/vllm/issues/18156) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Can't serve Qwen3-AWQ

### Issue 正文摘录

### Your current environment vllm 0.8.5.post1 (latest) ### 🐛 Describe the bug Can't serve Qwen3-AWQ `cognitivecomputations/Qwen3-235B-A22B-AWQ ` on 4A10? each A10 GPU has 24G RAM? so we have 24*4 G? I couldn't serve it on 4A10 it always give me OOM. ``` VLLM_USE_V1=0 vllm serve cognitivecomputations/Qwen3-235B-A22B-AWQ --tensor-parallel-size 4 --max-model-len 8192 --gpu-memory-utilization 0.95 --distributed-executor-backend mp ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Can't serve Qwen3-AWQ bug;stale ### Your current environment vllm 0.8.5.post1 (latest) ### 🐛 Describe the bug Can't serve Qwen3-AWQ `cognitivecomputations/Qwen3-235B-A22B-AWQ ` on 4A10? each A10 GPU has 24G RAM?...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ax-model-len 8192 --gpu-memory-utilization 0.95 --distributed-executor-backend mp ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: G RAM? so we have 24*4 G? I couldn't serve it on 4A10 it always give me OOM. ``` VLLM_USE_V1=0 vllm serve cognitivecomputations/Qwen3-235B-A22B-AWQ --tensor-parallel-size 4 --max-model-len 8192 --gpu-memory-utilization...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Can't serve Qwen3-AWQ bug;stale ### Your current environment vllm 0.8.5.post1 (latest) ### 🐛 Describe the bug Can't serve Qwen3-AWQ `cognitivecomputations/Qwen3-235B-A22B-AWQ ` on 4A10? each A10 GPU has 24G RAM?...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
