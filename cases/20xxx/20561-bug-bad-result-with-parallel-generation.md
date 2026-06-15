# vllm-project/vllm#20561: [Bug]: Bad result with parallel generation.

| 字段 | 值 |
| --- | --- |
| Issue | [#20561](https://github.com/vllm-project/vllm/issues/20561) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Bad result with parallel generation.

### Issue 正文摘录

I think the related issues are: - https://github.com/vllm-project/vllm/issues/15933 - https://github.com/vllm-project/vllm/issues/15730 Although both issues have been closed, one of the comments links to this PR: https://github.com/vllm-project/vllm/pull/15492. However, it seems the issue still persists. The reason I don’t think this is an issue with the LLM is that the results are correct when rollout.n is set to 6 or lower. This appears to be a memory related issue — the results are correct when n or batch_size is smaller or prompt is shorter, or enable_prefix_caching=False. ### Your current environment ### 🐛 Describe the bug Bad result when rollout.n is bigger. ```python from transformers import AutoTokenizer import vllm # v0.9.2 print(f"version: {vllm.__version__}") from vllm import LLM, SamplingParams model_id = "Qwen/Qwen2.5-14B-Instruct" tokenizer = AutoTokenizer.from_pretrained(model_id) llm = LLM(model=model_id) sampling_params = SamplingParams( n=8, temperature=0.7, top_p=0.8, top_k=20, repetition_penalty=1.05, max_tokens=800, seed=42, ) # part content of ccdv/arxiv-summarization test [0] text = """for about 20 years the problem of properties of short - term changes of s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: issues/15730 Although both issues have been closed, one of the comments links to this PR: https://github.com/vllm-project/vllm/pull/15492. However, it seems the issue still persists. The reason I don’t think this is an...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: em of aliases in the power spectrum analysis is presented . in section 4 numerical results of the new method of the diagnosis of an echo - effect for sunspot area data are discussed . in section 5 the problem of the exi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: a memory related issue — the results are correct when n or batch_size is smaller or prompt is shorter, or enable_prefix_caching=False. ### Your current environment ### 🐛 Describe the bug Bad result when rollout.n is big...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nt(f"version: {vllm.__version__}") from vllm import LLM, SamplingParams model_id = "Qwen/Qwen2.5-14B-Instruct" tokenizer = AutoTokenizer.from_pretrained(model_id) llm = LLM(model=model_id) sampling_params = SamplingPara...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: max_tokens=800, seed=42, ) # part content of ccdv/arxiv-summarization test [0] text = """for about 20 years the problem of properties of short - term changes of solar activity has been considered extensively . many inve...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
