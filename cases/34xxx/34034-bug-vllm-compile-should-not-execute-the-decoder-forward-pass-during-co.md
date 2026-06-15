# vllm-project/vllm#34034: [Bug]: vLLM-compile should not execute the decoder forward pass during compilation

| 字段 | 值 |
| --- | --- |
| Issue | [#34034](https://github.com/vllm-project/vllm/issues/34034) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM-compile should not execute the decoder forward pass during compilation

### Issue 正文摘录

### Your current environment main ### 🐛 Describe the bug During cold start compilation, vLLM-compile executes the text decoder forward pass using the max_num_batched_tokens size. I'm not completely sure how long a text decoder forward pass is, but if it is O(1s) then this is unnecessary and will save on compile time. There's one complication in that I don't know when autotuning will happen. I hope that vLLM does warmup of a size before the first cudagraph capture (but also we do compile-time autotuning so I hope that works too...) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ing will happen. I hope that vLLM does warmup of a size before the first cudagraph capture (but also we do compile-time autotuning so I hope that works too...) ### Before submitting a new issue... - [x] Make sure you al...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: vLLM-compile should not execute the decoder forward pass during compilation bug;torch.compile ### Your current environment main ### 🐛 Describe the bug During cold start compilation, vLLM-compile executes the text...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vLLM-compile should not execute the decoder forward pass during compilation bug;torch.compile ### Your current environment main ### 🐛 Describe the bug During cold start compilation, vLLM-compile executes the text...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
