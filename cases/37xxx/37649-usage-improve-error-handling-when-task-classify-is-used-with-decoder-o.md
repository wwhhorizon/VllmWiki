# vllm-project/vllm#37649: [Usage]: Improve error handling when task='classify' is used with decoder-only models (e.g., Qwen, Llama, Mistral)

| 字段 | 值 |
| --- | --- |
| Issue | [#37649](https://github.com/vllm-project/vllm/issues/37649) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Improve error handling when task='classify' is used with decoder-only models (e.g., Qwen, Llama, Mistral)

### Issue 正文摘录

### Your current environment **Title:** Improve error handling when `task='classify'` is used with decoder-only models (e.g., Qwen, Llama, Mistral) **Body:** ### 🐞 Problem Description When initializing an `LLM` instance with `task='classify'` on a **decoder-only causal language model** (such as `Qwen/Qwen2.5-0.5B-Instruct`, `meta-llama/Llama-3-8B`, or `mistralai/Mistral-7B-v0.1`), vLLM fails during model loading with a cryptic error: ``` ValueError: Following weights were not initialized from checkpoint: {'score.weight'} RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} ``` This occurs because: - The `task='classify'` option triggers the use of a classification head (`score` layer). - However, standard Causal LM checkpoints (like those from Qwen, Llama, Mistral) **do not contain a `score.weight` parameter**, as they are not trained for sequence classification. - vLLM attempts to construct a model with this missing head and only fails at weight-loading time. ### 🔁 Reproduction Code ```python from vllm import LLM, SamplingParams prompts = ['hello'] sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=1024, stop=[]) llm...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ]: Improve error handling when task='classify' is used with decoder-only models (e.g., Qwen, Llama, Mistral) usage ### Your current environment **Title:** Improve error handling when `task='classify'` is used with decod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ls at weight-loading time. ### 🔁 Reproduction Code ```python from vllm import LLM, SamplingParams prompts = ['hello'] sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=1024, stop=[]) llm = LLM(mod...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: dd more details, but this version clearly explains the problem, provides reproducible code, proposes a solution, and aligns with vLLM’s goal of being user-friendly and robust. Let me know if you'd like a Chinese version...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Behavior vLLM should **validate compatibility between `task` and model architecture early** (e.g., in `LLM.__init__` or engine args parsing) and raise a clear, actionable error such as: ```text ValueError: The 'classify...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Improve error handling when task='classify' is used with decoder-only models (e.g., Qwen, Llama, Mistral) usage ### Your current environment **Title:** Improve error handling when `task='classify'` is used with...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
