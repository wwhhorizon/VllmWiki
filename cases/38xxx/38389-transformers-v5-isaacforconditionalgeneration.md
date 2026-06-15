# vllm-project/vllm#38389: [Transformers v5] IsaacForConditionalGeneration

| 字段 | 值 |
| --- | --- |
| Issue | [#38389](https://github.com/vllm-project/vllm/issues/38389) |
| 状态 | open |
| 标签 | help wanted;good first issue |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Transformers v5] IsaacForConditionalGeneration

### Issue 正文摘录

This is a sub-issue forming part of the work in https://github.com/vllm-project/vllm/issues/38379, please read the description of this issue before beginning to work on this one. ## Which test is failing? This one has lots of issues beyond this test, it should be upstreamed so that the code is correct and stays maintained ```console $ pytest tests/models/test_initialization.py::test_can_initialize_large_subset[IsaacForConditionalGeneration] ... AttributeError: 'str' object has no attribute '__args__' ``` Related tests: ``` [2026-03-27T01:46:05Z] FAILED models/multimodal/generation/test_common.py::test_single_image_models[isaac-test_case35] - ImportError: cannot import name 'SlidingWindowCache' from 'transformers.cache_utils' (/usr/local/lib/python3.12/dist-packages/transformers/cache_utils.py) [2026-03-27T01:46:05Z] FAILED models/multimodal/generation/test_common.py::test_single_image_models[isaac-test_case36] - ImportError: cannot import name 'SlidingWindowCache' from 'transformers.cache_utils' (/usr/local/lib/python3.12/dist-packages/transformers/cache_utils.py) [2026-03-27T01:46:05Z] FAILED models/multimodal/generation/test_common.py::test_single_image_models[isaac-test_case37]...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: that the code is correct and stays maintained ```console $ pytest tests/models/test_initialization.py::test_can_initialize_large_subset[IsaacForConditionalGeneration] ... AttributeError: 'str' object has no attribute '_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: generation/test_common.py::test_single_image_models[isaac-test_case35] - ImportError: cannot import name 'SlidingWindowCache' from 'transformers.cache_utils' (/usr/local/lib/python3.12/dist-packages/transformers/cache_u...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: escription of this issue before beginning to work on this one. ## Which test is failing? This one has lots of issues beyond this test, it should be upstreamed so that the code is correct and stays maintained ```console...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
