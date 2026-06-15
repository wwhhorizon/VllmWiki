# vllm-project/vllm#20723: [CI Failure]: LoRA TP Test (Distributed) - lora/test_llama_tp.py::test_tp2_serialize_and_deserialize_lora

| 字段 | 值 |
| --- | --- |
| Issue | [#20723](https://github.com/vllm-project/vllm/issues/20723) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: LoRA TP Test (Distributed) - lora/test_llama_tp.py::test_tp2_serialize_and_deserialize_lora

### Issue 正文摘录

### Name of failing test `lora/test_llama_tp.py::test_tp2_serialize_and_deserialize_lora` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/builds/23536/steps/canvas?sid=0197f0f3-a191-49c0-aef5-89d61c597808 ``` [2025-07-09T23:17:11Z] (VllmWorker rank=0 pid=11292) WARNING 07-09 16:17:11 [tensorizer.py:226] Provided both tensorizer_dir and tensorizer_uri. Inferring tensorizer_dir from tensorizer_uri as the latter takes precedence. [2025-07-09T23:17:11Z] (VllmWorker rank=0 pid=11292) ERROR 07-09 16:17:11 [multiproc_executor.py:487] Traceback (most recent call last): [2025-07-09T23:17:11Z] (VllmWorker rank=0 pid=11292) ERROR 07-09 16:17:11 [multiproc_executor.py:487] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 461, in worker_main [2025-07-09T23:17:11Z] (VllmWorker rank=0 pid=11292) ERROR 07-09 16:17:11 [multiproc_executor.py:487] worker = WorkerProc(*args, **kwargs) [2025-07-09T23:17:11Z] (VllmWorker rank=0 pid=11292) ERROR 07-09 16:17:11 [multiproc_executor.py:487] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ [20...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI Failure]: LoRA TP Test (Distributed) - lora/test_llama_tp.py::test_tp2_serialize_and_deserialize_lora ci-failure ### Name of failing test `lora/test_llama_tp.py::test_tp2_serialize_and_deserialize_lora` ### Basic in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: LoRA TP Test (Distributed) - lora/test_llama_tp.py::test_tp2_serialize_and_deserialize_lora ci-failure ### Name of failing test `lora/test_llama_tp.py::test_tp2_serialize_and_deserialize_lora` ### Basic in
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: and_deserialize_lora` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/buil...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: LoRA TP Test (Distributed) - lora/test_llama_tp.py::test_tp2_serialize_and_deserialize_lora ci-failure ### Name of failing test `lora/test_llama_tp.py::test_tp2_serialize_and_deserialize_lora` ### Basic in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
