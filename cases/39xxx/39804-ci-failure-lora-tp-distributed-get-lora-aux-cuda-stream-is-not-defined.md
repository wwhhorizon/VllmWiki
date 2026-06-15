# vllm-project/vllm#39804: [CI Failure]: LoRA TP (Distributed) _get_lora_aux_cuda_stream is not defined

| 字段 | 值 |
| --- | --- |
| Issue | [#39804](https://github.com/vllm-project/vllm/issues/39804) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: LoRA TP (Distributed) _get_lora_aux_cuda_stream is not defined

### Issue 正文摘录

### Name of failing test `lora/test_olmoe_tp.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test LoRA TP (Distributed) [test](https://buildkite.com/vllm/ci/builds/61159#019d8a94-c00f-42b4-8b68-9a650f217336) failure ``` pytest -v -s -x lora/test_olmoe_tp.py ``` due to ``` Loading safetensors checkpoint shards: 100% 3/3 [00:16 ``` ### 📝 History of failing test Not failed in previous nightly. ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: LoRA TP (Distributed) _get_lora_aux_cuda_stream is not defined ci-failure ### Name of failing test `lora/test_olmoe_tp.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused b
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ora/test_olmoe_tp.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test LoRA TP (Distributed) [test](https...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: LoRA TP (Distributed) _get_lora_aux_cuda_stream is not defined ci-failure ### Name of failing test `lora/test_olmoe_tp.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: i-failure ### Name of failing test `lora/test_olmoe_tp.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: _stream is not defined ci-failure ### Name of failing test `lora/test_olmoe_tp.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
