# vllm-project/vllm#42093: [CI Failure]: GPQA Eval (GPT-OSS) (B200) - gpt-oss-20b-flashinfer-mxfp4-mxfp8-cutlass

| 字段 | 值 |
| --- | --- |
| Issue | [#42093](https://github.com/vllm-project/vllm/issues/42093) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: GPQA Eval (GPT-OSS) (B200) - gpt-oss-20b-flashinfer-mxfp4-mxfp8-cutlass

### Issue 正文摘录

### Name of failing test `evals/gpt_oss/test_gpqa_correctness.py::test_gpqa_correctness[gpt-oss-20b-flashinfer-mxfp4-mxfp8-cutlass]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Currently the test just "hangs" forever due to the model producing gibberish until it times out ### 📝 History of failing test I believe it is because due to https://github.com/vllm-project/vllm/pull/40960 hardcoding is_sf_swizzled_layout=False in the mxfp8 branch of moe_kernel_quantize_input ### CC List. _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [CI Failure]: GPQA Eval (GPT-OSS) (B200) - gpt-oss-20b-flashinfer-mxfp4-mxfp8-cutlass ci-failure ### Name of failing test `evals/gpt_oss/test_gpqa_correctness.py::test_gpqa_correctness[gpt-oss-20b-flashinfer-mxfp4-mxfp8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: GPQA Eval (GPT-OSS) (B200) - gpt-oss-20b-flashinfer-mxfp4-mxfp8-cutlass ci-failure ### Name of failing test `evals/gpt_oss/test_gpqa_correctness.py::test_gpqa_correctness[gpt-oss-20b-flashinfer-mxfp4-mxfp8...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [CI Failure]: GPQA Eval (GPT-OSS) (B200) - gpt-oss-20b-flashinfer-mxfp4-mxfp8-cutlass ci-failure ### Name of failing test `evals/gpt_oss/test_gpqa_correctness.py::test_gpqa_correctness[gpt-oss-20b-flashinfer-mxfp4-mxfp8...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ttps://github.com/vllm-project/vllm/pull/40960 hardcoding is_sf_swizzled_layout=False in the mxfp8 branch of moe_kernel_quantize_input ### CC List. _No response_
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: GPQA Eval (GPT-OSS) (B200) - gpt-oss-20b-flashinfer-mxfp4-mxfp8-cutlass ci-failure ### Name of failing test `evals/gpt_oss/test_gpqa_correctness.py::test_gpqa_correctness[gpt-oss-20b-flashinfer-mxfp4-mxfp8...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
