# vllm-project/vllm#17877: [Bug]: vllm run bge-m3 error

| 字段 | 值 |
| --- | --- |
| Issue | [#17877](https://github.com/vllm-project/vllm/issues/17877) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm run bge-m3 error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Deploy local BGE-M3 using VLLM and start the command as follows： python3 -m vllm.entrypoints.openai.api_server --served-model-name embed --model /app/bge-m3 --gpu-memory-utilization 0.8 --trust-remote-code --port 8080 --task embed 。 Service error: huggingface_hub.errors.HFValidationError: Repo id must be in the from 'repo_name' or 'namespace/repo_name': '/app/bge_m3'. usee 'repo_type' argument if needed。 （This model can run and start normally without using VLLM for testing） environment： VLLM 0.7.3 transformers 4.51.3 torch 2.5.1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: mmand as follows： python3 -m vllm.entrypoints.openai.api_server --served-model-name embed --model /app/bge-m3 --gpu-memory-utilization 0.8 --trust-remote-code --port 8080 --task embed 。 Service error: huggingface_hub.er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 5.1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vllm run bge-m3 error bug;stale ### Your current environment ### 🐛 Describe the bug Deploy local BGE-M3 using VLLM and start the command as follows： python3 -m vllm.entrypoints.openai.api_server --served-model-na...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: f needed。 （This model can run and start normally without using VLLM for testing） environment： VLLM 0.7.3 transformers 4.51.3 torch 2.5.1 ### Before submitting a new issue... - [x] Make sure you already searched for rele...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
