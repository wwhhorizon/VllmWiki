# vllm-project/vllm#7918: [Bug]: vllm:num_requests_waiting is not being published at /metrics endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#7918](https://github.com/vllm-project/vllm/issues/7918) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm:num_requests_waiting is not being published at /metrics endpoint

### Issue 正文摘录

### 🐛 Describe the bug Data for vllm:num_requests_waiting is missing. vllm:num_requests_waiting is not being published at /metrics endpoint docker image for vllm : vllm-openai:v0.5.3.post1 ``` # HELP vllm:num_requests_waiting Number of requests waiting to be processed. # TYPE vllm:num_requests_waiting gauge vllm:num_requests_waiting{model_name="/data/models/model-gemma2-a100/experiment-it1"} 0.0 ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vllm:num_requests_waiting is not being published at /metrics endpoint bug;stale ### 🐛 Describe the bug Data for vllm:num_requests_waiting is missing. vllm:num_requests_waiting is not being published at /metrics e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng gauge vllm:num_requests_waiting{model_name="/data/models/model-gemma2-a100/experiment-it1"} 0.0 ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cessed. # TYPE vllm:num_requests_waiting gauge vllm:num_requests_waiting{model_name="/data/models/model-gemma2-a100/experiment-it1"} 0.0 ``` ### Before submitting a new issue... - [X] Make sure you already searched for...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vllm:num_requests_waiting is not being published at /metrics endpoint docker image for vllm : vllm-openai:v0.5.3.post1 ``` # HELP vllm:num_requests_waiting Number of requests waiting to be processed. # TYPE vllm:num_req...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: s_waiting gauge vllm:num_requests_waiting{model_name="/data/models/model-gemma2-a100/experiment-it1"} 0.0 ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
