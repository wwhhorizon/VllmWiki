# vllm-project/vllm#37856: [Bug]: Shared Expert output is incorrect under Sequence Parallel MoE (EP + TP > 1 + DP > 1) for Qwen3.5 MoE models

| 字段 | 值 |
| --- | --- |
| Issue | [#37856](https://github.com/vllm-project/vllm/issues/37856) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Shared Expert output is incorrect under Sequence Parallel MoE (EP + TP > 1 + DP > 1) for Qwen3.5 MoE models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running Qwen3.5 MoE models (e.g., `Qwen/Qwen3.5-397B-A17B`) with Expert Parallelism enabled and `TP > 1` and `DP > 1`, the model produces completely garbled output. The root cause is that the Shared Expert computation is incorrect under the `use_sequence_parallel_moe` code path. **Model**: `Qwen/Qwen3.5-397B-A17B` (512 routed experts, 1 shared expert) **Configuration**: 8 nodes × 8 GPUs, TP=8, DP=8 (EP=64) ```python from vllm import LLM, SamplingParams llm = LLM( model="Qwen/Qwen3.5-397B-A17B", tensor_parallel_size=8, data_parallel_size=8, enable_expert_parallel=True, ) output = llm.generate( ["What is 2+3?"], SamplingParams(max_tokens=128, temperature=0.0), ) print(output[0].outputs[0].text) ``` ### Analysis When `use_sequence_parallel_moe` is `True` (triggered by EP enabled + TP > 1 + DP > 1), `Qwen3NextSparseMoeBlock.forward()` chunks the input via `sequence_parallel_chunk`, so each TP rank processes only N/TP **different** tokens. This is correct for **routed experts** — the EP all-to-all mechanism handles chunked tokens properly. But it breaks the **shared expert**. The shared expert MLP uses TP-sharded weights (`Column...

## 现有链接修复摘要

#41763 Fix EP precision for Qwen3 MoE shared expert under sequence-parallel MoE

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nfiguration**: 8 nodes × 8 GPUs, TP=8, DP=8 (EP=64) ```python from vllm import LLM, SamplingParams llm = LLM( model="Qwen/Qwen3.5-397B-A17B", tensor_parallel_size=8, data_parallel_size=8, enable_expert_parallel=True, )...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Qwen3.5 MoE models (e.g., `Qwen/Qwen3.5-397B-A17B`) with Expert Parallelism enabled and `TP > 1` and `DP > 1`, the model produces completely garbled output. The root cause is that the Shared Expert computation is incorr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tput is incorrect under Sequence Parallel MoE (EP + TP > 1 + DP > 1) for Qwen3.5 MoE models bug ### Your current environment ### 🐛 Describe the bug When running Qwen3.5 MoE models (e.g., `Qwen/Qwen3.5-397B-A17B`) with E...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Shared Expert output is incorrect under Sequence Parallel MoE (EP + TP > 1 + DP > 1) for Qwen3.5 MoE models bug ### Your current environment ### 🐛 Describe the bug When running Qwen3.5 MoE models (e.g., `Qwen/Qwe...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ogits;speculative_decoding cuda;moe;operator;sampling;triton build_error;mismatch;nan_inf env_dependency #41763 Fix EP precision for Qwen3 MoE shared expert under sequence-parallel MoE Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41763](https://github.com/vllm-project/vllm/pull/41763) | closes_keyword | 0.95 | Fix EP precision for Qwen3 MoE shared expert under sequence-parallel MoE | Closes #37856. ## Purpose https://github.com/vllm-project/vllm/pull/39181 fixed Qwen3-Next and Qwen2MoeMLP. This PR extends the same `is_sequence_parallel` → `disable_tp` wir |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
