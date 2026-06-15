# vllm-project/vllm#14693: [Bug]: When using VLLM to run the BGE-reranker-v2-me3 model to process rerank business, an error often occurs: The model does not support the Rerank (Score) API

| 字段 | 值 |
| --- | --- |
| Issue | [#14693](https://github.com/vllm-project/vllm/issues/14693) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When using VLLM to run the BGE-reranker-v2-me3 model to process rerank business, an error often occurs: The model does not support the Rerank (Score) API

### Issue 正文摘录

### Your current environment ubuntu vllm: 0.7.3 gpu: 4090(24gb) * 2 ![Image](https://github.com/user-attachments/assets/f1d906d5-57a8-46a8-a163-3ae9a02c1ec7) ### 🐛 Describe the bug I referred to the VLLM official website documentation and used the following interfaces to call them, but often encountered error messages. api: http://xxx.xxx.xxx:port/v2/rerank or http://xxx.xxx.xxx:port/v1/rerank or http://xxx.xxx.xxx:port/rerank ![Image](https://github.com/user-attachments/assets/ac09959a-3ef6-4064-b51f-3a01516bc9ed) After calling the request, subordinate errors frequently occur:The model does not support the Rerank (Score) API. It's strange that sometimes it's normal and there's no pattern found. How can I solve this problem? thanks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rror often occurs: The model does not support the Rerank (Score) API bug;stale ### Your current environment ubuntu vllm: 0.7.3 gpu: 4090(24gb) * 2 ![Image](https://github.com/user-attachments/assets/f1d906d5-57a8-46a8-a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 8-a163-3ae9a02c1ec7) ### 🐛 Describe the bug I referred to the VLLM official website documentation and used the following interfaces to call them, but often encountered error messages. api: http://xxx.xxx.xxx:port/v2/rer...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: When using VLLM to run the BGE-reranker-v2-me3 model to process rerank business, an error often occurs: The model does not support the Rerank (Score) API bug;stale ### Your current environment ubuntu vllm: 0.7.3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
