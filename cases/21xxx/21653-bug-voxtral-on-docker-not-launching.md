# vllm-project/vllm#21653: [Bug]: Voxtral on Docker not launching

| 字段 | 值 |
| --- | --- |
| Issue | [#21653](https://github.com/vllm-project/vllm/issues/21653) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Voxtral on Docker not launching

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Trying to launch a container for voxtral with a custom docker image, with updated transformers package, run inot error: Docker command: ```docker command: - "--model" - "mistralai/Voxtral-Mini-3B-2507" ``` Seems that vllm is forwarding the kwargs `'max_loras', '_from_auto'` into the tokenizer. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Voxtral on Docker not launching bug;stale ### Your current environment ### 🐛 Describe the bug Trying to launch a container for voxtral with a custom docker image, with updated transformers package, run inot error...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ackage, run inot error: Docker command: ```docker command: - "--model" - "mistralai/Voxtral-Mini-3B-2507" ``` Seems that vllm is forwarding the kwargs `'max_loras', '_from_auto'` into the tokenizer. ### Before submittin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Voxtral on Docker not launching bug;stale ### Your current environment ### 🐛 Describe the bug Trying to launch a container for voxtral with a custom docker image, with updated transformers package, run inot error...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;frontend_api;model_support cuda build_error;crash env_dependency...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
