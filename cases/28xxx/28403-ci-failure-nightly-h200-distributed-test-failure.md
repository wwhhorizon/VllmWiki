# vllm-project/vllm#28403: [CI Failure]: Nightly H200 Distributed Test Failure

| 字段 | 值 |
| --- | --- |
| Issue | [#28403](https://github.com/vllm-project/vllm/issues/28403) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 |  |
| Operator 关键词 | operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Nightly H200 Distributed Test Failure

### Issue 正文摘录

### Name of failing test `tests/compile/test_sequence_parallelism.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```bash FAILED tests/compile/test_sequence_parallelism.py::test_sequence_parallelism_pass[True-dtype0-16-16-8-TestQuantModel] - torch.multiprocessing.spawn.ProcessRaisedException: -- Process 1 terminated with the following error: Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/torch/multiprocessing/spawn.py", line 95, in _wrap fn(i, *args) File "/vllm-workspace/tests/compile/test_sequence_parallelism.py", line 330, in sequence_parallelism_pass_on_test_model backend_no_func.check_before_ops(model.ops_in_model_before()) File "/vllm-workspace/tests/compile/backend.py", line 98, in check_before_ops assert num_pre > num_post, f"All nodes remain for op {op.name()}" ^^^^^^^^^^^^^^^^^^ AssertionError: All nodes remain for op _C::fused_add_rms_norm FAILED tests/compile/test_sequence_parallelism.py::test_sequence_parallelism_pass[True-dtype1-16-16-8-TestQuantModel] - torch.multiprocessing.spawn.ProcessRaisedException: -- Process...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: Nightly H200 Distributed Test Failure ci-failure ### Name of failing test `tests/compile/test_sequence_parallelism.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by ex
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ompile/test_sequence_parallelism.py::test_sequence_parallelism_pass[True-dtype0-16-16-8-TestQuantModel] - torch.multiprocessing.spawn.ProcessRaisedException: -- Process 1 terminated with the following error: Traceback (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: failing test `tests/compile/test_sequence_parallelism.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing tes...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: arallelism.py", line 330, in sequence_parallelism_pass_on_test_model backend_no_func.check_before_ops(model.ops_in_model_before()) File "/vllm-workspace/tests/compile/backend.py", line 98, in check_before_ops assert num...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: uence_parallelism.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```bash FAILED tests/compile/test_...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
