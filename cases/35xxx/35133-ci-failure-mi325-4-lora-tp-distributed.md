# vllm-project/vllm#35133: [CI Failure]:  mi325_4: LoRA TP (Distributed)

| 字段 | 值 |
| --- | --- |
| Issue | [#35133](https://github.com/vllm-project/vllm/issues/35133) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_4: LoRA TP (Distributed)

### Issue 正文摘录

### Name of failing test `pytest -v -s -x lora/test_chatglm3_tp.py && pytest -v -s -x lora/test_llama_tp.py && pytest -v -s -x lora/test_llm_with_multi_loras.py && pytest -v -s -x lora/test_olmoe_tp.py && pytest -v -s -x lora/test_gptoss_tp.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test has a failure here: ```log FAILED lora/test_olmoe_tp.py::test_olmoe_lora_mixed ``` This is an accuracy bug. **However**, in this TG, we would like to enable another test: ```bash pytest -v -s -x lora/test_gptoss_tp.py ``` Currently this test is not in `test-amd.yaml` file. However, in our effort to achieve parity with upstream signal, we need to enable this test. ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/5234/steps/canvas?sid=019c894c-5e4d-41a0-9f59-b5785b8ccbd1&tab=output

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ra/test_gptoss_tp.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test has a failure here: ```l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_4: LoRA TP (Distributed) ci-failure ### Name of failing test `pytest -v -s -x lora/test_chatglm3_tp.py && pytest -v -s -x lora/test_llama_tp.py && pytest -v -s -x lora/test_llm_with_multi_loras.py &&
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `pytest -v -s -x lora/test_chatglm3_tp.py && pytest -v -s -x lora/test_llama_tp.py && pytest -v -s -x lora/test_llm_with_multi_loras.py && pytest -v -s -x lora/test_olmoe_tp.py && pytest -v -s -x lora/test_gptoss_tp.py`...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Failure]: mi325_4: LoRA TP (Distributed) ci-failure ### Name of failing test `pytest -v -s -x lora/test_chatglm3_tp.py && pytest -v -s -x lora/test_llama_tp.py && pytest -v -s -x lora/test_llm_with_multi_loras.py && pyt...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: v -s -x lora/test_llm_with_multi_loras.py && pytest -v -s -x lora/test_olmoe_tp.py && pytest -v -s -x lora/test_gptoss_tp.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
