# vllm-project/vllm#25194: [Bug]: vLLM produces non-deterministic output due to Triton autotuner

| 字段 | 值 |
| --- | --- |
| Issue | [#25194](https://github.com/vllm-project/vllm/issues/25194) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic;slowdown |
| 根因提示 | env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM produces non-deterministic output due to Triton autotuner

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **TLDR: Triton auto-tuning can cause vLLM to have non-deterministic output** While debugging prefix caching for mamba, we encountered a test-case that produces non-deterministic behaviour on `main`. Running the script below multiple times (on an H100) produces non-deterministic output, even though there is (a) no batching (b) no prefix caching (c) no chunked prefill and (d) temperature is zero. Please excuse the bizarre prompt... ```python from vllm import LLM, SamplingParams prompt = """vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs. vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs. vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs. vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs. vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs. vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs. vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs. vLLM is a high-throughput and memory-efficient infer...

## 现有链接修复摘要

#25197 [Kernel] [Mamba] Remove BLOCK_H=1 from list of tuneable configurations for `_chunk_cumsum_fwd_kernel` | #34648 [Feature] Add VLLM_TRITON_AUTOTUNE with functional autotune control

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 6: [Bug]: vLLM produces non-deterministic output due to Triton autotuner bug ### Your current environment ### 🐛 Describe the bug **TLDR: Triton auto-tuning can cause vLLM to have non-deterministic output** While debugging...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rature is zero. Please excuse the bizarre prompt... ```python from vllm import LLM, SamplingParams prompt = """vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs. vLLM is a high-through...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ic behaviour on `main`. Running the script below multiple times (on an H100) produces non-deterministic output, even though there is (a) no batching (b) no prefix caching (c) no chunked prefill and (d) temperature is ze...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ven though there is (a) no batching (b) no prefix caching (c) no chunked prefill and (d) temperature is zero. Please excuse the bizarre prompt... ```python from vllm import LLM, SamplingParams prompt = """vLLM is a high...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s(temperature=0.0, max_tokens=3, logprobs=1) # Create an LLM. llm = LLM(model="ibm-granite/granite-4.0-tiny-preview", enforce_eager=True, max_num_seqs=1, gpu_memory_utilization=0.4) # Generate texts from the prompts. #...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25197](https://github.com/vllm-project/vllm/pull/25197) | closes_keyword | 0.95 | [Kernel] [Mamba] Remove BLOCK_H=1 from list of tuneable configurations for `_chunk_cumsum_fwd_kernel` | Resolves #25194 The call to `tl.cumsum` in `_chunk_cumsum_fwd_kernel` produces numerically different output depending on whether `BLOCK_H=1` vs. `BLOCK_H>1`. We suspect it is usin |
| [#34648](https://github.com/vllm-project/vllm/pull/34648) | mentioned | 0.6 | [Feature] Add VLLM_TRITON_AUTOTUNE with functional autotune control | `VLLM_BATCH_INVARIANT=1` for kernels still using `@triton.autotune` (#25194) 2. **Slow startup** — autotuning adds seconds to minutes depending on kernel count and shape variety (… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
