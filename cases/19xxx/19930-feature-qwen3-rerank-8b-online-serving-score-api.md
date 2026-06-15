# vllm-project/vllm#19930: [Feature]: Qwen3-Rerank-8B online serving score API

| 字段 | 值 |
| --- | --- |
| Issue | [#19930](https://github.com/vllm-project/vllm/issues/19930) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Qwen3-Rerank-8B online serving score API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The latest Qwen3-Rerank-8B model is not supported by accessing the online serving API. When I run vllm serve Qwen/Qwen3-Reranker-8B --task score --port 7001, and request the score API service similar to https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_cross_encoder_score.py, the error occurred is {'object': 'error', 'message': 'The model does not support Score API', 'type': 'BadRequestError', 'param': None, 'code': 400}. ### Alternatives Use HF implementation instead for now. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Qwen3-Rerank-8B online serving score API feature request ### 🚀 The feature, motivation and pitch The latest Qwen3-Rerank-8B model is not supported by accessing the online serving API. When I run vllm serve Qw...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Qwen3-Rerank-8B online serving score API feature request ### 🚀 The feature, motivation and pitch The latest Qwen3-Rerank-8B model is not supported by accessing the online serving API. When I run vllm serve Qw...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: score API feature request ### 🚀 The feature, motivation and pitch The latest Qwen3-Rerank-8B model is not supported by accessing the online serving API. When I run vllm serve Qwen/Qwen3-Reranker-8B --task score --port 7...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
