# vllm-project/vllm#16634: [Feature]: Support for Raw Prompt Input Bypassing Template Rendering

| 字段 | 值 |
| --- | --- |
| Issue | [#16634](https://github.com/vllm-project/vllm/issues/16634) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for Raw Prompt Input Bypassing Template Rendering

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi vLLM team! First, thank you for your incredible work on this project - it's become an essential tool for my llm workflow. I'd like to propose a feature that would add flexibility for users working with custom fine-tuned models. Currently, when using the OpenAI-compatible API endpoint, prompts are automatically rendered through chat templates. While this works well for standard use cases, **many fine-tuned models require highly customized prompt formats that don't align with template conventions. This is particularly common with domain-specific models, instruction-tuned variants, and models using non-standard special tokens.** **Problem Statement:** Template rendering can become a friction point when: 1. Working with models trained on unique prompt structures 2. Using proprietary fine-tuned models with fixed formatting requirements 3. Implementing research prototypes requiring direct control over input **Proposed Solution:** Add an optional API parameter (e.g., use_template: bool or raw_prompt: bool) that allows users to: 1. Bypass template rendering entirely 2. Submit already-formatted prompts directly to the model 3. Maintain existing te...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: fine-tuned models with fixed formatting requirements 3. Implementing research prototypes requiring direct control over input **Proposed Solution:** Add an optional API parameter (e.g., use_template: bool or raw_prompt:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ture that would add flexibility for users working with custom fine-tuned models. Currently, when using the OpenAI-compatible API endpoint, prompts are automatically rendered through chat templates. While this works well...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: gn with template conventions. This is particularly common with domain-specific models, instruction-tuned variants, and models using non-standard special tokens.** **Problem Statement:** Template rendering can become a f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ture]: Support for Raw Prompt Input Bypassing Template Rendering feature request ### 🚀 The feature, motivation and pitch Hi vLLM team! First, thank you for your incredible work on this project - it's become an essential...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
