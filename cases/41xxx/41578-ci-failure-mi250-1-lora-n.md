# vllm-project/vllm#41578: [CI Failure]:  mi250_1: LoRA %N

| 字段 | 值 |
| --- | --- |
| Issue | [#41578](https://github.com/vllm-project/vllm/issues/41578) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi250_1: LoRA %N

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi250_1-lora-n && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && pytest -v -s lora --shard-id=$BUILDKITE_PARALLEL_JOB --num-shards=$BUILDKITE_PARALLEL_JOB_COUNT --ignore=lora/test_chatglm3_tp.py --ignore=lora/test_llama_tp.py --ignore=lora/test_llm_with_multi_loras.py --ignore=lora/test_olmoe_tp.py --ignore=lora/test_deepseekv2_tp.py --ignore=lora/test_gptoss_tp.py --ignore=lora/test_qwen3moe_tp.py --ignore=lora/test_qwen35_densemodel_lora.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED lora/test_transformers_model.py::test_ilama_lora ``` ### 📝 History of failing test - Current streak start: 2026-04-16 - First failure in 60d window: 2026-04-16 - Last successful nightly: 2026-04-15 - Break frequency (60d, pass↔fail flips): 1 - Latest nightly date: 2026-05-03 - Latest build(s): [amd-ci #8177](https://buildkite.com/vllm/amd-ci/builds/8177) - Latest hardware status: `mi250_1`=fail

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _PARALLEL_JOB_COUNT --ignore=lora/test_chatglm3_tp.py --ignore=lora/test_llama_tp.py --ignore=lora/test_llm_with_multi_loras.py --ignore=lora/test_olmoe_tp.py --ignore=lora/test_deepseekv2_tp.py --ignore=lora/test_gptos...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ilure]: mi250_1: LoRA %N ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi250_1-lora-n && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && pytest...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi250_1: LoRA %N ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi250_1-lora-n && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && p
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 5_densemodel_lora.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED lora/test_transformers_...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ma_tp.py --ignore=lora/test_llm_with_multi_loras.py --ignore=lora/test_olmoe_tp.py --ignore=lora/test_deepseekv2_tp.py --ignore=lora/test_gptoss_tp.py --ignore=lora/test_qwen3moe_tp.py --ignore=lora/test_qwen35_densemod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
