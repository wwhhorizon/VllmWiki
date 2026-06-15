# vllm-project/vllm#40320: [CI Failure]: tests/kernels/moe/test_moe_layer.py

| 字段 | 值 |
| --- | --- |
| Issue | [#40320](https://github.com/vllm-project/vllm/issues/40320) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: tests/kernels/moe/test_moe_layer.py

### Issue 正文摘录

### Name of failing test tests/kernels/moe/test_moe_layer.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Running `tests/kernels/moe/test_moe_layer.py` got: ``` tests/kernels/moe/test_moe_layer.py::test_moe_layer[False-deepep_low_latency-2-1-True] INFO 04-19 20:55:09 [kernel.py:199] Final IR op priority after setting platform defaults: IrOpPriorityConfig(rms_norm=['native']) NCCL version 2.28.9+cuda13.0 Assertion failed: /root/vllm/tools/ep_kernels/ep_kernels_workspace/DeepEP/csrc/kernels/internode_ll.cu:285, condition: ibgda_get_state()->num_rc_per_pe >= num_local_experts Assertion failed: /root/vllm/tools/ep_kernels/ep_kernels_workspace/DeepEP/csrc/kernels/internode_ll.cu:285, condition: ibgda_get_state()->num_rc_per_pe >= num_local_experts Assertion failed: /root/vllm/tools/ep_kernels/ep_kernels_workspace/DeepEP/csrc/kernels/internode_ll.cu:285, condition: ibgda_get_state()->num_rc_per_pe >= num_local_experts Assertion failed: /root/vllm/tools/ep_kernels/ep_kernels_workspace/DeepEP/csrc/kernels/internode_ll.cu:285, condition: ibgda_get_state()->num_rc_per_pe >=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: tests/kernels/moe/test_moe_layer.py ci-failure ### Name of failing test tests/kernels/moe/test_moe_layer.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libr
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ayer[False-deepep_low_latency-2-1-True]" --subtests="[222-2048-2048-64-2-bfloat16-None-False-False-False-False-False-deepep_low_latency-2-2-1],[222-2048-2048-8-2-bfloat16-None-False-Fal se-False-False-False-deepep_low_l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: # Name of failing test tests/kernels/moe/test_moe_layer.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [CI Failure]: tests/kernels/moe/test_moe_layer.py ci-failure ### Name of failing test tests/kernels/moe/test_moe_layer.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libra...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: tests/kernels/moe/test_moe_layer.py ci-failure ### Name of failing test tests/kernels/moe/test_moe_layer.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libra...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
