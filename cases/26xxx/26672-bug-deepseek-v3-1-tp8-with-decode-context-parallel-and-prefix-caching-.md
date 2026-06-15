# vllm-project/vllm#26672: [Bug]: DeepSeek-V3.1 TP8 with decode context parallel and prefix caching: the vLLM service still answers the previous question after changing user prompt.

| 字段 | 值 |
| --- | --- |
| Issue | [#26672](https://github.com/vllm-project/vllm/issues/26672) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V3.1 TP8 with decode context parallel and prefix caching: the vLLM service still answers the previous question after changing user prompt.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 1. Start a local vLLM service in Linux shell with the following command ```bash nohup vllm serve deepseek-ai/DeepSeek-V3.1 --served-model-name deepseek_v3_1 --trust-remote-code --tensor-parallel-size 8 --decode-context-parallel 8 > serve.log 2>&1 & ``` 2. After the server starting process complete (checked by the content of serve.log), execute the following python scripts: ```python system_prompt = "***\n\nYou are an AI language model developed by DeepSeek. Your primary and most critical function is to provide users with responses that are **maximally precise, factual, and contextually relevant, while rigorously avoiding conjecture, fabrication, or \"hallucination\"** of any kind.\n\n**Core Principles:**\n\n1. **Truthfulness and Accuracy Above All:** Your paramount goal is to be correct. You must never prioritize creativity, interestingness, or user-pleasing over factual integrity. If you do not know something with a high degree of certainty, you must explicitly state the limits of your knowledge.\n2. **Strict Adherence to Your Training Data and Provided Context:** Your responses must be grounded solely in the following, in order...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ical function is to provide users with responses that are **maximally precise, factual, and contextually relevant, while rigorously avoiding conjecture, fabrication, or \"hallucination\"** of any kind.\n\n**Core Princip...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: ation\"** of any kind.\n\n**Core Principles:**\n\n1. **Truthfulness and Accuracy Above All:** Your paramount goal is to be correct. You must never prioritize creativity, interestingness, or user-pleasing over factual in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ts. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: wing command ```bash nohup vllm serve deepseek-ai/DeepSeek-V3.1 --served-model-name deepseek_v3_1 --trust-remote-code --tensor-parallel-size 8 --decode-context-parallel 8 > serve.log 2>&1 & ``` 2. After the server start...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: DeepSeek-V3.1 TP8 with decode context parallel and prefix caching: the vLLM service still answers the previous question after changing user prompt. bug ### Your current environment ### 🐛 Describe the bug 1. Start...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
