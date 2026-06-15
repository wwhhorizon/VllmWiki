# vllm-project/vllm#11996: [Bug]: The api server /health endpoint is unable to detect when the Worker VllmWorkerProcess has died

| 字段 | 值 |
| --- | --- |
| Issue | [#11996](https://github.com/vllm-project/vllm/issues/11996) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The api server /health endpoint is unable to detect when the Worker VllmWorkerProcess has died

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug docker images: vllm/vllm-openai:v0.6.5 device: 4*A800 model: qwen2.5-72b-qgpt-int4 args: --swap-space 0 --tensor-parallel-size 4 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parse hermes 1. What is the root cause of the Worker VllmWorkerProcess crash? 2. The api server /health endpoint is unable to detect when the Worker VllmWorkerProcess has died. ![image](https://github.com/user-attachments/assets/928d6f18-6bc9-4961-ad51-69787c027052) ![image](https://github.com/user-attachments/assets/ad3cf6a6-dcb5-494b-b575-4760be13d4de) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: llmWorkerProcess has died bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug docker images: vllm/vllm-openai:v0.6.5 device: 4*A800 model: qwen2.5-72b-qgpt-int4 args: --swap...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: onment ### Model Input Dumps _No response_ ### 🐛 Describe the bug docker images: vllm/vllm-openai:v0.6.5 device: 4*A800 model: qwen2.5-72b-qgpt-int4 args: --swap-space 0 --tensor-parallel-size 4 --enable-prefix-caching...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: r images: vllm/vllm-openai:v0.6.5 device: 4*A800 model: qwen2.5-72b-qgpt-int4 args: --swap-space 0 --tensor-parallel-size 4 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parse hermes 1. What is the root...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: de) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: point is unable to detect when the Worker VllmWorkerProcess has died bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug docker images: vllm/vllm-openai:v0.6.5 device: 4*A80...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
