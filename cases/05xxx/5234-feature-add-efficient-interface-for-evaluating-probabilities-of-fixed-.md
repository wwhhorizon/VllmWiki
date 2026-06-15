# vllm-project/vllm#5234: [Feature]: Add efficient interface for evaluating probabilities of fixed prompt-completion pairs

| 字段 | 值 |
| --- | --- |
| Issue | [#5234](https://github.com/vllm-project/vllm/issues/5234) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;sampling_logits |
| 子分类 |  |
| Operator 关键词 | sampling |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Add efficient interface for evaluating probabilities of fixed prompt-completion pairs

### Issue 正文摘录

# Proposed Feature Add an efficient interface for generation probabilities on fixed prompt and completion pairs. For example: ```python # ... load LLM or engine prompt_completion_pairs = [ ("1 + 1 = ", "2"), ("1 + 1 = ", "3"), ] prompts, completions = list(zip(*prompt_completion_pairs)) probs = llm.completion_logprobs(prompts=prompts, completions=completions) ``` Alternatively, the interface could evaluate the probabilities of a fixed prompt with multiple generation options to better leverage prefix caching: ```python prompt = "1 + 1 = " completions = ["2", "3", "4"] probs = llm.completion_logprobs(prompt=prompt, completions=completions) ``` Currently, there are interfaces in class `SamplingParams` to return the log probabilities of prompt (`prompt_logprobs`) and the generated tokens (`logprobs`). However, they are either inefficient or has incomplete support for this use case. # Motivation The motivation of this feature comes from LLM evaluations on multiple-choice questions (e.g., MMLU). vLLM is a popular tool adopted by mainstream LLM evaluation frameworks (e.g., [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)) for this purpose. Using the following...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Feature]: Add efficient interface for evaluating probabilities of fixed prompt-completion pairs feature request;stale # Proposed Feature Add an efficient interface for generation probabilities on fixed prompt and compl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: point python3 vllm/vllm-openai:v0.4.3 /app/profiling.py ``` On a single A100-40G GPU, it runs around **500 seconds** with `prompt_logprobs=1` and only **27 seconds** with no prompt_logprobs. Moreover, we can fit much lo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: , seq_len)).tolist() llm = LLM("mistral-community/Mistral-7B-v0.2", max_model_len=8000, gpu_memory_utilization=0.6) sampling_params = SamplingParams(temperature=0, max_tokens=1, prompt_logprobs=1) start = time.perf_coun...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ce for evaluating probabilities of fixed prompt-completion pairs feature request;stale # Proposed Feature Add an efficient interface for generation probabilities on fixed prompt and completion pairs. For example: ```pyt...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Add efficient interface for evaluating probabilities of fixed prompt-completion pairs feature request;stale # Proposed Feature Add an efficient interface for generation probabilities on fixed prompt and compl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
