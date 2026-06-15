# vllm-project/vllm#24376: [Bug]: `tests/compile` failures

| 字段 | 值 |
| --- | --- |
| Issue | [#24376](https://github.com/vllm-project/vllm/issues/24376) |
| 状态 | closed |
| 标签 | bug;good first issue;torch.compile |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: `tests/compile` failures

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Currently, running `pytest tests/compile` fails for 2 reasons: 1. There are repeated registrations of silly attention ops, so importing multiple tests into the same process fails 2. There are a bunch of tests not currently in CI, all failing. Fixing this would be helpful so that we can just run all of the tests in CI, as well as locally during development to make sure nothing compilation-related broke. Tracking solutions: 1. I started working on this in #23257 but gave up due to the many failures. It should still be a good starting point. Done by @ZJY0516 in #24502. 2. The tests currently failing individually 2.a) `test_functionalization.py`: Done in #23953 by @angelayi 2.b) `tests/compile/test_sequence_parallelism.py`: fixed in #24542 2.c) `tests/compile/test_config.py`: Fixed in #22682 by @zou3519, waiting to be merged 2.d) `tests/compile/test_async_tp.py`: Done in #26038 by @jasonlizhengjian The failure in 2.d (full trace below): ``` torch._dynamo.exc.BackendCompilerFailed: backend=' ' raised: RuntimeError: symm_mem::fused_scaled_matmul_reduce_scatter() is missing value for argument 'orig_scatter_dim'. Declaration: symm_mem::f...

## 现有链接修复摘要

#23257 [torch.compile] Refactor duplicate torch op registrations | #24188 [torch.compile] Custom op matching | #24542 [torch.compile] Cleanup compilation tests and custom passes, add debug utils, fix DCE bug (#23091), fix test (#24376), and prep for…

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: `tests/compile` failures bug;good first issue;torch.compile ### Your current environment ### 🐛 Describe the bug Currently, running `pytest tests/compile` fails for 2 reasons: 1. There are repeated registrations o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: hengjian The failure in 2.d (full trace below): ``` torch._dynamo.exc.BackendCompilerFailed: backend=' ' raised: RuntimeError: symm_mem::fused_scaled_matmul_reduce_scatter() is missing value for argument 'orig_scatter_d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: : Done in #23953 by @angelayi 2.b) `tests/compile/test_sequence_parallelism.py`: fixed in #24542 2.c) `tests/compile/test_config.py`: Fixed in #22682 by @zou3519, waiting to be merged 2.d) `tests/compile/test_async_tp.p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: BackendCompilerFailed: backend=' ' raised: RuntimeError: symm_mem::fused_scaled_matmul_reduce_scatter() is missing value for argument 'orig_scatter_dim'. Declaration: symm_mem::fused_scaled_matmul_reduce_scatter(Tensor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: /test_sequence_parallelism.py`: fixed in #24542 2.c) `tests/compile/test_config.py`: Fixed in #22682 by @zou3519, waiting to be merged 2.d) `tests/compile/test_async_tp.py`: Done in #26038 by @jasonlizhengjian The failu...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23257](https://github.com/vllm-project/vllm/pull/23257) | mentioned | 0.45 | [torch.compile] Refactor duplicate torch op registrations | n-related broke. tracking solutions: 1. i started working on this in #23257 but gave up due to the many failures. it should still be a good starting point. done by @zjy0516 in #24… |
| [#24188](https://github.com/vllm-project/vllm/pull/24188) | closes_keyword | 0.95 | [torch.compile] Custom op matching | Fixes #23091. <!-- markdownlint-disable --> ## Purpose Cleanup compilation tests and custom passes and address #23091 and part of #24376. This PR is a prerequisite for matching to |
| [#24542](https://github.com/vllm-project/vllm/pull/24542) | closes_keyword | 0.95 | [torch.compile] Cleanup compilation tests and custom passes, add debug utils, fix DCE bug (#23091), fix test (#24376), and prep for custom op matching (#24604) | Fixes #23091. ## Purpose Cleanup compilation tests and custom passes and address #23091 and part of #24376. This PR is a prerequisite for matching torch implementations of custom |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
