# vllm-project/vllm#14819: [Feature]: specify model only in config.yaml

| 字段 | 值 |
| --- | --- |
| Issue | [#14819](https://github.com/vllm-project/vllm/issues/14819) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: specify model only in config.yaml

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It would be nice not to need anything but a config file to start `serve`: ```sh vllm serve --config scenario.yaml ``` Right now, the `model_tag` appears to be required via the CLI. Why not allow this via a config file too? For example: ```yaml model: Qwen/Qwen2.5-Coder-7B # ... args ``` Furthermore, the web based docs for `vllm serve` don't list the `model_tag` as required: https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#vllm-serve and instead suggest I can use `--model` and thus based on the [config section](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#configuration-file) I assume that would map to `model: Qwen/Qwen2.5-Coder-7B`? This would be a great way to encapsulate everything I need for a particular serve "environment" into a config file to quickly start different scenarios. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: specify model only in config.yaml good first issue;feature request ### 🚀 The feature, motivation and pitch It would be nice not to need anything but a config file to start `serve`: ```sh vllm serve --config s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: specify model only in config.yaml good first issue;feature request ### 🚀 The feature, motivation and pitch It would be nice not to need anything but a config file to start `serve`: ```sh vllm serve --config s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: specify model only in config.yaml good first issue;feature request ### 🚀 The feature, motivation and pitch It would be nice not to need anything but a config file to start `serve`: ```sh vllm serve --config s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: serve` don't list the `model_tag` as required: https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#vllm-serve and instead suggest I can use `--model` and thus based on the [config section](https://docs....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
