# vllm-project/vllm#9482: [Usage]: Question Regarding VLLM Rate Limit

| 字段 | 值 |
| --- | --- |
| Issue | [#9482](https://github.com/vllm-project/vllm/issues/9482) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Question Regarding VLLM Rate Limit

### Issue 正文摘录

### Your current environment cpython@3.11.3 vllm==0.6.3 torch==2.4.0 ### How would you like to use vllm Hello, I have a question regarding the VLLM rate limit. I am running the Qwen-2.5 32B model on an A100 80GB * 2 setup. Specifically, I am using VLLM to set up the server and sending several hundred queries asynchronously from the front-end. Each query contains around 4000 to 5000 tokens. The issue I am encountering is that only a portion of the queries are being processed. Could this be related to the VLLM rate limit? I would appreciate any guidance on the appropriate approach to handle this. Thank you. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: regarding the VLLM rate limit. I am running the Qwen-2.5 32B model on an A100 80GB * 2 setup. Specifically, I am using VLLM to set up the server and sending several hundred queries asynchronously from the front-end. Eac...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ello, I have a question regarding the VLLM rate limit. I am running the Qwen-2.5 32B model on an A100 80GB * 2 setup. Specifically, I am using VLLM to set up the server and sending several hundred queries asynchronously...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: limit. I am running the Qwen-2.5 32B model on an A100 80GB * 2 setup. Specifically, I am using VLLM to set up the server and sending several hundred queries asynchronously from the front-end. Each query contains around...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Question Regarding VLLM Rate Limit usage;stale ### Your current environment cpython@3.11.3 vllm==0.6.3 torch==2.4.0 ### How would you like to use vllm Hello, I have a question regarding the VLLM rate limit. I a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
