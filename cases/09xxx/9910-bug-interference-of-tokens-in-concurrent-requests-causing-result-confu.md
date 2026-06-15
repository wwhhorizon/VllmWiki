# vllm-project/vllm#9910: [Bug]: Interference of Tokens in Concurrent Requests Causing Result Confusion in Version 0.6.3

| 字段 | 值 |
| --- | --- |
| Issue | [#9910](https://github.com/vllm-project/vllm/issues/9910) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Interference of Tokens in Concurrent Requests Causing Result Confusion in Version 0.6.3

### Issue 正文摘录

### Your current environment ```text python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8083 --model Qwen2.5-72B-Chat-AWQ --tensor-parallel-size 4 --dtype half --trust-remote-code ``` ### 🐛 Describe the bug In version 0.6.3, when multiple requests are made simultaneously, the tokens between requests can affect each other, leading to a mix-up in the results among different requests.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: thon -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8083 --model Qwen2.5-72B-Chat-AWQ --tensor-parallel-size 4 --dtype half --trust-remote-code ``` ### 🐛 Describe the bug In version 0.6.3, when multiple req...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Interference of Tokens in Concurrent Requests Causing Result Confusion in Version 0.6.3 bug;stale ### Your current environment ```text python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8083 --mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nterference of Tokens in Concurrent Requests Causing Result Confusion in Version 0.6.3 bug;stale ### Your current environment ```text python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8083 --model Qwen2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 0.0 --port 8083 --model Qwen2.5-72B-Chat-AWQ --tensor-parallel-size 4 --dtype half --trust-remote-code ``` ### 🐛 Describe the bug In version 0.6.3, when multiple requests are made simultaneously, the tokens between requ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
