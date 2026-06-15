# vllm-project/vllm#26600: [Bug]: RunAI model streamer breaks in 0.11

| 字段 | 值 |
| --- | --- |
| Issue | [#26600](https://github.com/vllm-project/vllm/issues/26600) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RunAI model streamer breaks in 0.11

### Issue 正文摘录

### Your current environment vLLM 0.11.0 ### 🐛 Describe the bug When trying to use Run.AI model streamer on vLLM 0.11 it breaks. It seems to break with every new minor release of vLLM, same thing happened previously from 0.9.x to 0.10.x. `vllm serve s3:// --load-format runai_streamer` ``` Repo id must be in the form 'repo_name' or 'namespace/repo_name': 's3://XXXXXXXXX'. Use `repo_type` argument if needed. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: RunAI model streamer breaks in 0.11 bug;stale ### Your current environment vLLM 0.11.0 ### 🐛 Describe the bug When trying to use Run.AI model streamer on vLLM 0.11 it breaks. It seems to break with every new mino...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: RunAI model streamer breaks in 0.11 bug;stale ### Your current environment vLLM 0.11.0 ### 🐛 Describe the bug When trying to use Run.AI model streamer on vLLM 0.11 it breaks. It seems to break with every new mino...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
