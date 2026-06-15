# vllm-project/vllm#9405: [Feature]: Option For Automatic Function Calling For CohereForAI/c4ai-command-r-plus-08-2024

| 字段 | 值 |
| --- | --- |
| Issue | [#9405](https://github.com/vllm-project/vllm/issues/9405) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Option For Automatic Function Calling For CohereForAI/c4ai-command-r-plus-08-2024

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I deployed the **c4ai-command-r-plus-08-2024** model locally using vLLM. I would like to enable the **Automatic Function Calling** feature, so I set the following flags: _--enable-auto-tool-choice --chat-template [path/to/local/tokenizer_config.json_ As described in the documentation, I need to specify another flag: **--tool-call-parser** or a name registered under _--tool-parser-plugin_. However, there is no option available for the c4ai-command-r-plus-08-2024 model from Cohere (the available options are: hermes, internlm, llama3_json, mistral ). Could you please add support for the c4ai-command-r-plus-08-2024 model? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: re, motivation and pitch I deployed the **c4ai-command-r-plus-08-2024** model locally using vLLM. I would like to enable the **Automatic Function Calling** feature, so I set the following flags: _--enable-auto-tool-choi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tic Function Calling For CohereForAI/c4ai-command-r-plus-08-2024 feature request;stale ### 🚀 The feature, motivation and pitch I deployed the **c4ai-command-r-plus-08-2024** model locally using vLLM. I would like to ena...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /tokenizer_config.json_ As described in the documentation, I need to specify another flag: **--tool-call-parser** or a name registered under _--tool-parser-plugin_. However, there is no option available for the c4ai-com...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
