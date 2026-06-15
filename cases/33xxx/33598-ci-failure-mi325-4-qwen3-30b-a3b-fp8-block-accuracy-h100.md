# vllm-project/vllm#33598: [CI Failure]:  mi325_4: Qwen3-30B-A3B-FP8-block Accuracy (H100)

| 字段 | 值 |
| --- | --- |
| Issue | [#33598](https://github.com/vllm-project/vllm/issues/33598) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_4: Qwen3-30B-A3B-FP8-block Accuracy (H100)

### Issue 正文摘录

### Name of failing test `bash .buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep_eplb.sh 0.8 200 8020` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression in this TG: ```log ValueError: Unsupported dtype torch.float8_e4m3fnuz: should be one of int8, uint8, int32, int64, float16, float32, float64, bfloat16, float8e4m3. ``` ### 📝 History of failing test Test failed: https://buildkite.com/vllm/amd-ci/builds/3965/steps/canvas?sid=019c1800-7659-4415-ac51-725ddeeb7b45

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [CI Failure]: mi325_4: Qwen3-30B-A3B-FP8-block Accuracy (H100) ci-failure ### Name of failing test `bash .buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep_eplb.sh 0.8 200 8020` ### Basic information...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_4: Qwen3-30B-A3B-FP8-block Accuracy (H100) ci-failure ### Name of failing test `bash .buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep_eplb.sh 0.8 200 8020` ### Basic informatio
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure]: mi325_4: Qwen3-30B-A3B-FP8-block Accuracy (H100) ci-failure ### Name of failing test `bash .buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep_eplb.sh 0.8 200 8020` ### Basic information...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [CI Failure]: mi325_4: Qwen3-30B-A3B-FP8-block Accuracy (H100) ci-failure ### Name of failing test `bash .buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep_eplb.sh 0.8 200 8020` ### Basic information...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [CI Failure]: mi325_4: Qwen3-30B-A3B-FP8-block Accuracy (H100) ci-failure ### Name of failing test `bash .buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep_eplb.sh 0.8 200 8020` ### Basic information...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
