# vllm-project/vllm#28835: [Bug]: Illegal Memory Access and Incorrect Output with Long Inputs (>5k tokens) on qweN3-next-80b-instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#28835](https://github.com/vllm-project/vllm/issues/28835) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Illegal Memory Access and Incorrect Output with Long Inputs (>5k tokens) on qweN3-next-80b-instruct

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When deploying the qweN3-next-80b-instruct model with vLLM, an error occurs during inference if the user's input question exceeds 5k tokens in length (inputs shorter than this threshold work normally): Error 1:​ torch.AcceleratorError: CUDA error: an illegal memory access was encountered This error persists even after configuring --compilation_config.cudagraph_mode=PIECEWISEas recommended in the vLLM documentation. Once this error is triggered, the entire vLLM service becomes unresponsive. Error 2:​ When the --enforce-eagerflag is set, the system does not throw an error. However, for questions longer than 5k tokens, the output consists only of exclamation marks !!!!!, though the service remains operational. My environment details are: vLLM version: v0.11.0 CUDA version: 12.8b OS: Ubuntu 22.04 GPU: 8 x H20 GPUs Parallelism Configuration: PP=1, TP=8 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: r than this threshold work normally): Error 1:​ torch.AcceleratorError: CUDA error: an illegal memory access was encountered This error persists even after configuring --compilation_config.cudagraph_mode=PIECEWISEas rec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: egal Memory Access and Incorrect Output with Long Inputs (>5k tokens) on qweN3-next-80b-instruct bug;stale ### Your current environment ### 🐛 Describe the bug When deploying the qweN3-next-80b-instruct model with vLLM,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: hough the service remains operational. My environment details are: vLLM version: v0.11.0 CUDA version: 12.8b OS: Ubuntu 22.04 GPU: 8 x H20 GPUs Parallelism Configuration: PP=1, TP=8 ### Before submitting a new issue......
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tly asked questions. correctness distributed_parallel;model_support cuda mismatch env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rect Output with Long Inputs (>5k tokens) on qweN3-next-80b-instruct bug;stale ### Your current environment ### 🐛 Describe the bug When deploying the qweN3-next-80b-instruct model with vLLM, an error occurs during infer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
