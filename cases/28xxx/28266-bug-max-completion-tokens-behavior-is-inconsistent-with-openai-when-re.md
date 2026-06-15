# vllm-project/vllm#28266: [Bug]: `max_completion_tokens` behavior is inconsistent with OpenAI when reasoning-parser is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#28266](https://github.com/vllm-project/vllm/issues/28266) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `max_completion_tokens` behavior is inconsistent with OpenAI when reasoning-parser is enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using vLLM's OpenAI-compatible server with the --reasoning-parser argument enabled, the behavior of the max_completion_tokens parameter differs slightly from the standard OpenAI API. ### Expected Behavior When using openai's api, max_completion_tokens only limit the number of tokens for the final user-facing content that is generated after the "reasoning" phase. In other words, tokens generated for reasoning_content should not be counted against the max_completion_tokens quota. ### Actual Behavior max_completion_tokens appears to be treated as a max_tokens for the entire generation process. https://github.com/vllm-project/vllm/blob/c0a4b95d6474c72799cd8af4421ce922654c850e/vllm/entrypoints/openai/serving_engine.py#L940 It limits the sum of both the reasoning_content and the final content. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: x_completion_tokens only limit the number of tokens for the final user-facing content that is generated after the "reasoning" phase. In other words, tokens generated for reasoning_content should not be counted against t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pi;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
