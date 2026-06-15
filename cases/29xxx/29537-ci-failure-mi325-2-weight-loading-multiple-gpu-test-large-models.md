# vllm-project/vllm#29537: [CI Failure]: mi325_2: Weight Loading Multiple GPU Test - Large Models

| 字段 | 值 |
| --- | --- |
| Issue | [#29537](https://github.com/vllm-project/vllm/issues/29537) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;quantization |
| 症状 | build_error |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_2: Weight Loading Multiple GPU Test - Large Models

### Issue 正文摘录

### Name of failing test `bash weight_loading/run_model_weight_loading_test.sh -c weight_loading/models-large-amd.txt` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Test Summary:** **test_weight_loading in test_weight_loading.py** - Tests: Weight loading with tensor_parallel_size=2 - Failure: OSError (403 Client Error) during model configuration loading - Configuration: model=amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV, quantization=fp8, revision=main - Error location: `/usr/local/lib/python3.12/dist-packages/transformers/utils/hub.py:543` - Likely cause: The CI environment lacks authentication/authorization to access the gated HuggingFace repository `amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV`. This is an access control issue rather than a code or numerical failure - the test cannot proceed because it cannot download the model files from the restricted repository. ### 📝 History of failing test AMD-CI build Buildkite references: - 1041 - 1077 - 1088 - 1109 - 1111 ### CC List. _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI Failure]: mi325_2: Weight Loading Multiple GPU Test - Large Models ci-failure ### Name of failing test `bash weight_loading/run_model_weight_loading_test.sh -c weight_loading/models-large-amd.txt` ### Basic informat...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: models-large-amd.txt` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Test Summary:** **test_w...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: iguration loading - Configuration: model=amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV, quantization=fp8, revision=main - Error location: `/usr/local/lib/python3.12/dist-packages/transformers/utils/hub.py:543` - Likely cause:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_2: Weight Loading Multiple GPU Test - Large Models ci-failure ### Name of failing test `bash weight_loading/run_model_weight_loading_test.sh -c weight_loading/models-large-amd.txt` ### Basic informat
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_2: Weight Loading Multiple GPU Test - Large Models ci-failure ### Name of failing test `bash weight_loading/run_model_weight_loading_test.sh -c weight_loading/models-large-amd.txt` ### Basic informat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
