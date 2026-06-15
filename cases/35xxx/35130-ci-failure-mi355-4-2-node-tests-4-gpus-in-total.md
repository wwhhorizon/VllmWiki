# vllm-project/vllm#35130: [CI Failure]:  mi355_4: 2 Node Tests (4 GPUs in total)

| 字段 | 值 |
| --- | --- |
| Issue | [#35130](https://github.com/vllm-project/vllm/issues/35130) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_4: 2 Node Tests (4 GPUs in total)

### Issue 正文摘录

### Name of failing test `pytest -v -s -x lora/test_chatglm3_tp.py && pytest -v -s -x lora/test_llama_tp.py && pytest -v -s -x lora/test_llm_with_multi_loras.py && pytest -v -s -x lora/test_olmoe_tp.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There is a failing test in this TG specific to MI355: ```log FAILED lora/test_olmoe_tp.py::test_olmoe_lora_mixed ``` ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/5234/steps/canvas?sid=019c894c-5e4d-41a0-9f59-b5785b8ccbd1&tab=output

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_4: 2 Node Tests (4 GPUs in total) rocm;ci-failure ### Name of failing test `pytest -v -s -x lora/test_chatglm3_tp.py && pytest -v -s -x lora/test_llama_tp.py && pytest -v -s -x lora/test_llm_with_mul
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `pytest -v -s -x lora/test_chatglm3_tp.py && pytest -v -s -x lora/test_llama_tp.py && pytest -v -s -x lora/test_llm_with_multi_loras.py && pytest -v -s -x lora/test_olmoe_tp.py` ### Basic information - [ ] Flaky test -...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ora/test_olmoe_tp.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There is a failing test in this TG...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: mi355_4: 2 Node Tests (4 GPUs in total) rocm;ci-failure ### Name of failing test `pytest -v -s -x lora/test_chatglm3_tp.py && pytest -v -s -x lora/test_llama_tp.py && pytest -v -s -x lora/test_llm_with_mul...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: v -s -x lora/test_llm_with_multi_loras.py && pytest -v -s -x lora/test_olmoe_tp.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
