# vllm-project/vllm#38892: [Bug]: matmul_batch_invariant does not handle all torch.matmul dimension combinations (4D x 3D for gemma4-E2B)

| 字段 | 值 |
| --- | --- |
| Issue | [#38892](https://github.com/vllm-project/vllm/issues/38892) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: matmul_batch_invariant does not handle all torch.matmul dimension combinations (4D x 3D for gemma4-E2B)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug matmul_batch_invariant() function does not support all the dimension combination that torch.matmul supports. When testing gemma4-E2B on the batch invariant unit tests (https://github.com/vllm-project/vllm/tree/main/tests/v1/determinism) I faced the following error: ```Python (EngineCore pid=68032) ValueError: matmul_batch_invariant currently only supports 2D x 2D, 3D x 3D, 3D x 2D, 2D x 3D, and 4D x 4D, got shapes torch.Size([1, 2, 630, 10240]) and torch.Size([2, 10240, 768]) ``` The 4D x 3D matmul is not supported by matmul_batch_invariant() and it comes from: ```Python (EngineCore pid=68032) File "/home/yusuf/PycharmProjects/ym_vllm/vllm/.venv/lib/python3.12/site-packages/transformers/models/gemma4/modeling_gemma4.py", line 569, in forward (EngineCore pid=68032) position_embeddings = self._position_embeddings(pixel_position_ids, padding_positions) (EngineCore pid=68032) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=68032) File "/home/yusuf/PycharmProjects/ym_vllm/vllm/.venv/lib/python3.12/site-packages/transformers/models/gemma4/modeling_gemma4.py", line 557, in _position_embeddings (EngineCor...

## 现有链接修复摘要

#39909 Added general ND x ND matmul and unit test for it

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;gemm;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tests (https://github.com/vllm-project/vllm/tree/main/tests/v1/determinism) I faced the following error: ```Python (EngineCore pid=68032) ValueError: matmul_batch_invariant currently only supports 2D x 2D, 3D x 3D, 3D x...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ding cuda;gemm;operator;quantization;sampling;triton build_error;nan_inf;nondeterministic env_dependency;shape #39909 Added general ND x ND matmul and unit test for it Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ant does not handle all torch.matmul dimension combinations (4D x 3D for gemma4-E2B) bug ### Your current environment ### 🐛 Describe the bug matmul_batch_invariant() function does not support all the dimension combinati...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: t support all the dimension combination that torch.matmul supports. When testing gemma4-E2B on the batch invariant unit tests (https://github.com/vllm-project/vllm/tree/main/tests/v1/determinism) I faced the following e...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39909](https://github.com/vllm-project/vllm/pull/39909) | closes_keyword | 0.95 | Added general ND x ND matmul and unit test for it | fixes: #38892 and the general implementation ensures all shapes supported by torch.matmul are now supported by batch invariant matmul too. ## Test Plan Created a new test fil |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
