# vllm-project/vllm#29516: [CI Failure]: mi325_4: Distributed Tests (A100)

| 字段 | 值 |
| --- | --- |
| Issue | [#29516](https://github.com/vllm-project/vllm/issues/29516) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_4: Distributed Tests (A100)

### Issue 正文摘录

### Name of failing test `pytest -v -s distributed/test_custom_all_reduce.py && torchrun --nproc_per_node=2 distributed/test_ca_buffer_sharing.py && TARGET_TEST_SUITE=A100 pytest basic_correctness/ -v -s -m 'distributed(num_gpus=2)' && pytest -v -s -x lora/test_mixtral.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests in distributed/test_custom_all_reduce.py** **test_custom_allreduce[test_target1-1-2]** - Tests graph-captured custom all_reduce with tensor parallelism - Configuration: test_target=graph_allreduce, pipeline_parallel_size=1, tp_size=2 - Tests: CUDA graph capture of tensor_model_parallel_all_reduce operations with multiple communication rounds - Likely cause: The test captures all_reduce operations in a CUDA graph and replays them. It verifies outputs match between custom all_reduce and NCCL. The graph_allreduce function successfully registers cuda graph addresses but appears to fail during graph replay or verification. This suggests potential issues with CUDA graph compatibility on ROCm or synchronization problems during graph capture/re...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [CI Failure]: mi325_4: Distributed Tests (A100) ci-failure ### Name of failing test `pytest -v -s distributed/test_custom_all_reduce.py && torchrun --nproc_per_node=2 distributed/test_ca_buffer_sharing.py && TARGET_TEST...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: buted(num_gpus=2)' && pytest -v -s -x lora/test_mixtral.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_4: Distributed Tests (A100) ci-failure ### Name of failing test `pytest -v -s distributed/test_custom_all_reduce.py && torchrun --nproc_per_node=2 distributed/test_ca_buffer_sharing.py && TARGET_TEST_
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: lora/test_mixtral.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests in distributed/tes...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_4: Distributed Tests (A100) ci-failure ### Name of failing test `pytest -v -s distributed/test_custom_all_reduce.py && torchrun --nproc_per_node=2 distributed/test_ca_buffer_sharing.py && TARGET_TEST...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
