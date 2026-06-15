# vllm-project/vllm#9122: [Bug] BlockSpaceManagerV1.get_common_computed_block_ids returns empty string, causing msgspec decode failure

| 字段 | 值 |
| --- | --- |
| Issue | [#9122](https://github.com/vllm-project/vllm/issues/9122) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] BlockSpaceManagerV1.get_common_computed_block_ids returns empty string, causing msgspec decode failure

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When testing vllm, `BlockSpaceManagerV1.get_common_computed_block_ids` does not properly handle empty lists before calling `commonprefix(ids_list)`. https://github.com/vllm-project/vllm/blob/f19da64871065510691cd4fcaa5f4096b661dcec/vllm/core/block_manager_v1.py#L730 As a result, when `ids_list` is empty, `commonprefix` returns an empty string `""` instead of an expected list. This causes `msgspec` serialization to fail with the following error: ``` ERROR 10-07 18:45:55 async_llm_engine.py:61] msgspec.ValidationError: Expected array | null, got str - at $[0][0][9] ``` This issue occurs because the function does not check for empty `ids_list` before calling `commonprefix`, leading to an invalid output type. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ManagerV1.get_common_computed_block_ids returns empty string, causing msgspec decode failure bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When testing vllm, `BlockSpa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pe. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug] BlockSpaceManagerV1.get_common_computed_block_ids returns empty string, causing msgspec decode failure bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When testing

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
