# vllm-project/vllm#31559: [CI Failure]: Failed to upload and process pipeline: Pipeline upload rejected

| 字段 | 值 |
| --- | --- |
| Issue | [#31559](https://github.com/vllm-project/vllm/issues/31559) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Failed to upload and process pipeline: Pipeline upload rejected

### Issue 正文摘录

### Name of failing test pipeline was not uploaded due to duplicated keys ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test fatal: Failed to upload and process pipeline: Pipeline upload rejected: The key "block-nixlconnector-pd-accuracy-tests-distributed" has already been used by another step in this build key appeared twice in the YAML: https://buildkite.com/vllm/ci/builds/45222/steps/canvas?sid=019b7299-7b54-40ca-b446-b38c378c9050#019b7299-7b71-470b-bc99-00af63b981ce/L2854 ``` [2025-12-31T04:11:20Z] - block: "Run NixlConnector PD accuracy tests (Distributed)" [2025-12-31T04:11:20Z] depends_on: image-build [2025-12-31T04:11:20Z] key: block-nixlconnector-pd-accuracy-tests-distributed ``` https://buildkite.com/vllm/ci/builds/45222/steps/canvas?sid=019b7299-7b54-40ca-b446-b38c378c9050#019b7299-7b71-470b-bc99-00af63b981ce/L2887 ``` [2025-12-31T04:11:20Z] - block: "Run NixlConnector PD accuracy tests (Distributed)" [2025-12-31T04:11:20Z] depends_on: image-build [2025-12-31T04:11:20Z] key: block-nixlconnector-pd-accuracy-tests-distributed ```

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ue to duplicated keys ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test fatal: Failed to upload and proces...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Failed to upload and process pipeline: Pipeline upload rejected ci-failure ### Name of failing test pipeline was not uploaded due to duplicated keys ### Basic information - [ ] Flaky test - [ ] Can reprod
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: rocess pipeline: Pipeline upload rejected ci-failure ### Name of failing test pipeline was not uploaded due to duplicated keys ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ailed to upload and process pipeline: Pipeline upload rejected: The key "block-nixlconnector-pd-accuracy-tests-distributed" has already been used by another step in this build key appeared twice in the YAML: https://bui...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ling test pipeline was not uploaded due to duplicated keys ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
