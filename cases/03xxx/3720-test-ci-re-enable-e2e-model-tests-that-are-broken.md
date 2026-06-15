# vllm-project/vllm#3720: [Test][CI] Re-enable e2e model tests that are broken.

| 字段 | 值 |
| --- | --- |
| Issue | [#3720](https://github.com/vllm-project/vllm/issues/3720) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Test][CI] Re-enable e2e model tests that are broken.

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug After reenabling model tests from https://github.com/vllm-project/vllm/pull/3631, I found several e2e tests are broken in the matser. for the following reasons. - allenai/OLMo-1B: TypeError: forward() got an unexpected keyword argument 'cache_position' - mistralai/Mistral-7B-v0.1: correctness issue (generate doesn't generate any token) + RuntimeError: expected scalar type - - BFloat16 but found Half (only in CI) - Deci/DeciLM-7b: correctness issue (output is different) - tiiuae/falcon-7b: correctness issue (output is different) -"Qwen/Qwen1.5-0.5B": Correctness issue - test_mistral.py They are currently skipped/commented out in the master, and we should make sure to reenable it.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ate doesn't generate any token) + RuntimeError: expected scalar type - - BFloat16 but found Half (only in CI) - Deci/DeciLM-7b: correctness issue (output is different) - tiiuae/falcon-7b: correctness issue (output is di...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Test][CI] Re-enable e2e model tests that are broken. bug;stale ### Your current environment N/A ### 🐛 Describe the bug After reenabling model tests from https://github.com/vllm-project/vllm/pull/3631, I found several e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Test][CI] Re-enable e2e model tests that are broken. bug;stale ### Your current environment N/A ### 🐛 Describe the bug After reenabling model tests from https://github.com/vllm-project/vllm/pull/3631, I found several e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Test][CI] Re-enable e2e model tests that are broken. bug;stale ### Your current environment N/A ### 🐛 Describe the bug After reenabling model tests from https://github.com/vllm-project/vllm/pull/3631, I found several e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Test][CI] Re-enable e2e model tests that are broken. bug;stale ### Your current environment N/A ### 🐛 Describe the bug After reenabling model tests from https://github.com/vllm-project/vllm/pull/3631, I found several

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
