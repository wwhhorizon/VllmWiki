# vllm-project/vllm#29514: [CI Failure]: mi325_4: EPLB Execution Test

| 字段 | 值 |
| --- | --- |
| Issue | [#29514](https://github.com/vllm-project/vllm/issues/29514) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;model_support;moe;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | moe |
| 症状 | build_error;mismatch |
| 根因提示 | race_condition |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_4: EPLB Execution Test

### Issue 正文摘录

### Name of failing test `pytest -v -s distributed/test_eplb_execute.py && pytest -v -s distributed/test_eplb_spec_decode.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ## Failing Tests Summary **Failing Test 1:** `test_eplb_spec_decode[qwen3_next_mtp]` in `test_eplb_spec_decode.py` Tests EPLB correctness with MTP speculative decoding on Qwen3-Next-80B model using GSM8K dataset. **Failure:** Assertion error (likely accuracy mismatch) **Configuration:** model=Qwen3-Next-80B-A3B, tp_size=4, spec_method=mtp, expected_gsm8k=0.86±0.03 **Likely cause:** Measured GSM8K accuracy fell outside expected range (0.83-0.89), possibly due to numerical instability in distributed expert parallel load balancing or GPU memory pressure indicated by leaked shared_memory objects. --- **Failing Test 2:** `test_eplb_spec_decode_qwen3_next_mtp_async` in `test_eplb_spec_decode.py` Tests async EPLB implementation with MTP speculative decoding for same model. **Failure:** Assertion error (likely accuracy mismatch) **Configuration:** Same as above but with `use_async=True` in eplb_config **L...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: _eplb_spec_decode.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ## Failing Tests Summary **Failing...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: te.py && pytest -v -s distributed/test_eplb_spec_decode.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure]: mi325_4: EPLB Execution Test ci-failure ### Name of failing test `pytest -v -s distributed/test_eplb_execute.py && pytest -v -s distributed/test_eplb_spec_decode.py` ### Basic information - [ ] Flaky test...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_4: EPLB Execution Test ci-failure ### Name of failing test `pytest -v -s distributed/test_eplb_execute.py && pytest -v -s distributed/test_eplb_spec_decode.py` ### Basic information - [ ] Flaky test
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: range (0.83-0.89), possibly due to numerical instability in distributed expert parallel load balancing or GPU memory pressure indicated by leaked shared_memory objects. --- **Failing Test 2:** `test_eplb_spec_decode_qwe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
