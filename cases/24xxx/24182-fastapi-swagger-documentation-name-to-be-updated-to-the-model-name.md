# vllm-project/vllm#24182: FastAPI Swagger Documentation Name to be Updated to the Model Name

| 字段 | 值 |
| --- | --- |
| Issue | [#24182](https://github.com/vllm-project/vllm/issues/24182) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> FastAPI Swagger Documentation Name to be Updated to the Model Name

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In my organization we are hosting multiple hugging face models via our HGX machines and leveraging vllm docker images. So when I open all those links - I need to check the model name parameter to understand what address is hosting which one. The reason is when I open the swagger docs - it just shows "FASTAPI". Is there a way for the model name to show up rather than FastAPI in the docs so it is easier for users who are playing with multiple models hosted via different ports? Is there a current way for me to achieve this so I can test? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ng multiple hugging face models via our HGX machines and leveraging vllm docker images. So when I open all those links - I need to check the model name parameter to understand what address is hosting which one. The reas...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: stAPI Swagger Documentation Name to be Updated to the Model Name feature request;stale ### 🚀 The feature, motivation and pitch In my organization we are hosting multiple hugging face models via our HGX machines and leve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: FastAPI Swagger Documentation Name to be Updated to the Model Name feature request;stale ### 🚀 The feature, motivation and pitch In my organization we are hosting multiple hugging face models via our HGX machines and le...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ifferent ports? Is there a current way for me to achieve this so I can test? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
