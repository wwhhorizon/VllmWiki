# vllm-project/vllm#42183: [CI Failure]:  mi300_4: Distributed Torchrun + Examples (4 GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#42183](https://github.com/vllm-project/vllm/issues/42183) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi300_4: Distributed Torchrun + Examples (4 GPUs)

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_4-distributed-torchrun---examples-4-gpus && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && torchrun --nproc-per-node=4 distributed/test_torchrun_example.py && PP_SIZE=2 torchrun --nproc-per-node=4 distributed/test_torchrun_example.py && TP_SIZE=4 torchrun --nproc-per-node=4 distributed/test_torchrun_example_moe.py && PP_SIZE=2 TP_SIZE=2 torchrun --nproc-per-node=4 distributed/test_torchrun_example_moe.py && DP_SIZE=4 ENABLE_EP=1 torchrun --nproc-per-node=4 distributed/test_torchrun_example_moe.py && TP_SIZE=2 DP_SIZE=2 ENABLE_EP=1 torchrun --nproc-per-node=4 distributed/test_torchrun_example_moe.py && python3 ../examples/features/data_parallel/data_parallel_offline.py --enforce-eager && VLLM_ALLOW_INSECURE_SERIALIZATION=1 python3 ../examples/rl/rlhf_nccl.py && VLLM_ALLOW_INSECURE_SERIALIZATION=1 python3 ../examples/rl/rlhf_ipc.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` RuntimeError: NCCL error: unhandled cuda error (run with NCCL_DEBUG=INFO...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [CI Failure]: mi300_4: Distributed Torchrun + Examples (4 GPUs) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_4-distributed-torchrun---examples-4-gpus && export VLL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi300_4: Distributed Torchrun + Examples (4 GPUs) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_4-distributed-torchrun---examples-4-gpus && export VLL
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ce-eager && VLLM_ALLOW_INSECURE_SERIALIZATION=1 python3 ../examples/rl/rlhf_nccl.py && VLLM_ALLOW_INSECURE_SERIALIZATION=1 python3 ../examples/rl/rlhf_ipc.py` ### Basic information - [ ] Flaky test - [x] Can reproduce l...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: mples/rl/rlhf_ipc.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` RuntimeError: NCCL error: unha...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: TP_SIZE=4 torchrun --nproc-per-node=4 distributed/test_torchrun_example_moe.py && PP_SIZE=2 TP_SIZE=2 torchrun --nproc-per-node=4 distributed/test_torchrun_example_moe.py && DP_SIZE=4 ENABLE_EP=1 torchrun --nproc-per-no...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
