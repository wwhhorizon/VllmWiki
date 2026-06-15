# vllm-project/vllm#28876: [CI Failure]: should test_cumem.py use spawn or fork in cuda?

| 字段 | 值 |
| --- | --- |
| Issue | [#28876](https://github.com/vllm-project/vllm/issues/28876) |
| 状态 | closed |
| 标签 | stale;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: should test_cumem.py use spawn or fork in cuda?

### Issue 正文摘录

### Name of failing test tests/basic_correctness/test_cumem.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The test only fails locally for me when I use vllm main branch and on the CI of my PR, error is caused by cuda tests using `fork` instead of `spawn` I think, in the CI, there is a line that's trying for force spawn: https://github.com/vllm-project/vllm/blob/f2b8e1c5510cf3621dc4b910f0eba5289d9fee88/.buildkite/test-pipeline.yaml#L99-L100, but looks like it's not effective. I looked at the function that decides to use fork or spawn: https://github.com/vllm-project/vllm/blob/f8b19c0ffd65f7f6f01a0da4a39b6890f5db40cb/tests/utils.py#L1027 and I don't think it looks like the flag `VLLM_WORKER_MULTIPROC_METHOD`. Although the issue doesn't repro in the main vllm CI. Wondering how do we fix this? ``` FAILED basic_correctness/test_cumem.py::test_python_error - RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method FAILED basic_correctness/test_cumem.py::test_basic_cumem - RuntimeError: Cannot...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: should test_cumem.py use spawn or fork in cuda? stale;ci-failure ### Name of failing test tests/basic_correctness/test_cumem.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Cau
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Name of failing test tests/basic_correctness/test_cumem.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ectness/test_cumem.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The test only fails locally for me...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: should test_cumem.py use spawn or fork in cuda? stale;ci-failure ### Name of failing test tests/basic_correctness/test_cumem.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caus...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI Failure]: should test_cumem.py use spawn or fork in cuda? stale;ci-failure ### Name of failing test tests/basic_correctness/test_cumem.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caus...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
