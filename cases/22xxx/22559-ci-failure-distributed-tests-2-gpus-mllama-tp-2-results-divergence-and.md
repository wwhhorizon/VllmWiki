# vllm-project/vllm#22559: [CI Failure]: Distributed Tests (2 GPUs) - Mllama TP=2 results divergence and deadlock issue

| 字段 | 值 |
| --- | --- |
| Issue | [#22559](https://github.com/vllm-project/vllm/issues/22559) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Distributed Tests (2 GPUs) - Mllama TP=2 results divergence and deadlock issue

### Issue 正文摘录

### Name of failing test models/multimodal/generation/test_mllama.py test_models_distributed ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Mllama tp test was broken (https://buildkite.com/vllm/ci/builds/26344#01988898-4fbc-4d24-bd78-7325a1b6d9e3) with divergent results: ``` [2025-08-08T10:26:49Z] Traceback (most recent call last): -- | [2025-08-08T10:26:49Z] File "/vllm-workspace/tests/utils.py", line 742, in wrapper | [2025-08-08T10:26:49Z] f(*args, **kwargs) | [2025-08-08T10:26:49Z] File "/vllm-workspace/tests/models/multimodal/generation/test_mllama.py", line 415, in test_models_distributed | [2025-08-08T10:26:49Z] run_test( | [2025-08-08T10:26:49Z] File "/vllm-workspace/tests/models/multimodal/generation/test_mllama.py", line 174, in run_test | [2025-08-08T10:26:49Z] _run_test( | [2025-08-08T10:26:49Z] File "/vllm-workspace/tests/models/multimodal/generation/test_mllama.py", line 245, in _run_test | [2025-08-08T10:26:49Z] check_logprobs_close( | [2025-08-08T10:26:49Z] File "/vllm-workspace/tests/models/utils.py", line 228, in check_logprobs_close | [2025-08-08T1...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [CI Failure]: Distributed Tests (2 GPUs) - Mllama TP=2 results divergence and deadlock issue ci-failure ### Name of failing test models/multimodal/generation/test_mllama.py test_models_distributed ### Basic information...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [CI Failure]: Distributed Tests (2 GPUs) - Mllama TP=2 results divergence and deadlock issue ci-failure ### Name of failing test models/multimodal/generation/test_mllama.py test_models_distributed ### Basic information...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Distributed Tests (2 GPUs) - Mllama TP=2 results divergence and deadlock issue ci-failure ### Name of failing test models/multimodal/generation/test_mllama.py test_models_distributed ### Basic information
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ailure]: Distributed Tests (2 GPUs) - Mllama TP=2 results divergence and deadlock issue ci-failure ### Name of failing test models/multimodal/generation/test_mllama.py test_models_distributed ### Basic information - [ ]...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: the cherry blossoms reach their peak. The cherry blossoms are in full bloom, and the sky is a brilliant blue. The tower is a tall, slender structure that rises high above the surrounding buildings. The tower is made of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
