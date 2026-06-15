# vllm-project/vllm#15915: [Bug]: stuck on “application startup complete”

| 字段 | 值 |
| --- | --- |
| Issue | [#15915](https://github.com/vllm-project/vllm/issues/15915) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: stuck on “application startup complete”

### Issue 正文摘录

### Your current environment vllm/vllm-openai:v0.7.3 ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/f7136e96-d50b-4acc-b282-765dbd0b73d6) using docker images vllm/vllm-openai:v0.7.3 to deploy DeepSeek-R1-Distill-Qwen-32B on nvidia t4×4×2，but stuck in “application startup complete“. After waiting for 20 minutes, there was still no sign of "uvicorn running on xxx". I set --tensor-parallel-size 4 --pipeline-parallel-size 2 or --tensor-parallel-size 8 --pipeline-parallel-size 1 still nz ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: .com/user-attachments/assets/f7136e96-d50b-4acc-b282-765dbd0b73d6) using docker images vllm/vllm-openai:v0.7.3 to deploy DeepSeek-R1-Distill-Qwen-32B on nvidia t4×4×2，but stuck in “application startup complete“. After w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nz ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sing docker images vllm/vllm-openai:v0.7.3 to deploy DeepSeek-R1-Distill-Qwen-32B on nvidia t4×4×2，but stuck in “application startup complete“. After waiting for 20 minutes, there was still no sign of "uvicorn running o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 32B on nvidia t4×4×2，but stuck in “application startup complete“. After waiting for 20 minutes, there was still no sign of "uvicorn running on xxx". I set --tensor-parallel-size 4 --pipeline-parallel-size 2 or --tensor-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
