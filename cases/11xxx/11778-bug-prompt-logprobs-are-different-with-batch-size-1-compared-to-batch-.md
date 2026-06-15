# vllm-project/vllm#11778: [Bug]: prompt logprobs are different with batch_size > 1 compared to batch_size=1

| 字段 | 值 |
| --- | --- |
| Issue | [#11778](https://github.com/vllm-project/vllm/issues/11778) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;nondeterministic |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: prompt logprobs are different with batch_size > 1 compared to batch_size=1

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm interested in getting log-likelihoods of the prompt token (the usecase is RLHF). I get different results with `llm.generate` when I batch prompts compared to when I don't. The difference are big enough to make sure that this is not just GPU non-determinism that I observe (e.g. -1.75 and -2.119, -8.14 and -8.23) Here's the code that reproduce the issue. ```python from vllm import SamplingParams, LLM, TokensPrompt model_name = "deepseek-ai/deepseek-math-7b-instruct" entries = [ {"input_ids": [100000, 5726, 25, 2461, 317, 254, 23764, 280, 254, 1353]}, {"input_ids": [100000, 5726, 25, 42131, 628, 67, 25111, 90, 17, 20]} ] sampling_params = SamplingParams(max_tokens=1, prompt_logprobs=True) local_llm = LLM(model=model_name, dtype='bfloat16') def process_locally(entries): result = [] for entry in entries: gen_result = local_llm.generate(TokensPrompt(prompt_token_ids=entry["input_ids"]), sampling_params) result.append({ "content": [ {"logprob": lp[input_id].logprob} for input_id, lp in zip(entry["input_ids"][1:], gen_result[0].prompt_logprobs[1:]) if lp is not None ] }) return result def process_l...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: I observe (e.g. -1.75 and -2.119, -8.14 and -8.23) Here's the code that reproduce the issue. ```python from vllm import SamplingParams, LLM, TokensPrompt model_name = "deepseek-ai/deepseek-math-7b-instruct" entries = [...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: -8.23) Here's the code that reproduce the issue. ```python from vllm import SamplingParams, LLM, TokensPrompt model_name = "deepseek-ai/deepseek-math-7b-instruct" entries = [ {"input_ids": [100000, 5726, 25, 2461, 317,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ms(max_tokens=1, prompt_logprobs=True) local_llm = LLM(model=model_name, dtype='bfloat16') def process_locally(entries): result = [] for entry in entries: gen_result = local_llm.generate(TokensPrompt(prompt_token_ids=en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rence are big enough to make sure that this is not just GPU non-determinism that I observe (e.g. -1.75 and -2.119, -8.14 and -8.23) Here's the code that reproduce the issue. ```python from vllm import SamplingParams, LL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: compared to batch_size=1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm interested in getting log-likelihoods of the prompt token (the usecase is RLHF). I get diffe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
