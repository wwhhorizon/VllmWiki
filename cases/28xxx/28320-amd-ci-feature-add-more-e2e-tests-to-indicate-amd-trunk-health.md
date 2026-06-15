# vllm-project/vllm#28320: [AMD CI][Feature]: Add more E2E tests to indicate AMD trunk health

| 字段 | 值 |
| --- | --- |
| Issue | [#28320](https://github.com/vllm-project/vllm/issues/28320) |
| 状态 | closed |
| 标签 | feature request;rocm;ci/build;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8 |
| 症状 | build_error |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [AMD CI][Feature]: Add more E2E tests to indicate AMD trunk health

### Issue 正文摘录

AMD CI doesn't not have a very good coverage on E2E evals compared to Nvidia. At the current moment, only [Multi-Modal Accuracy Eval (Small Models)](https://github.com/vllm-project/vllm/blob/main/.buildkite/test-amd.yaml#L863) and [LM Eval Small Models](https://github.com/vllm-project/vllm/blob/main/.buildkite/test-amd.yaml#L621) are added to the current CI. As captured in [this doc](https://docs.google.com/document/d/1rBtSQ7bbrzFbSX3IjULmqZtYVxpVgqEo_A9W0PytxiM/edit?tab=t.0#heading=h.bqg584n9zp0v), we can add these models to start: - [ ] Deepseek R1: TP8, EP + MMLU-Pro - [x] GPT-OSS-120B: TP2, AIME - [x] Llama4-Maverick-FP8: TP8, MMLU-Pro

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: : TP8, EP + MMLU-Pro - [x] GPT-OSS-120B: TP2, AIME - [x] Llama4-Maverick-FP8: TP8, MMLU-Pro correctness ci_build;frontend_api;hardware_porting;moe;quantization fp8 build_error dtype AMD CI doesn't not have a very good c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: to Nvidia. At the current moment, only [Multi-Modal Accuracy Eval (Small Models)](https://github.com/vllm-project/vllm/blob/main/.buildkite/test-amd.yaml#L863) and [LM Eval Small Models](https://github.com/vllm-project/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [AMD CI][Feature]: Add more E2E tests to indicate AMD trunk health feature request;rocm;ci/build;stale AMD CI doesn't not have a very good coverage on E2E evals compared to Nvidia. At the current moment, only [Multi-Mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [AMD CI][Feature]: Add more E2E tests to indicate AMD trunk health feature request;rocm;ci/build;stale AMD CI doesn't not have a very good coverage on E2E evals compared to Nvidia. At the current moment, only [Multi-Mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: eature]: Add more E2E tests to indicate AMD trunk health feature request;rocm;ci/build;stale AMD CI doesn't not have a very good coverage on E2E evals compared to Nvidia. At the current moment, only [Multi-Modal Accurac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
