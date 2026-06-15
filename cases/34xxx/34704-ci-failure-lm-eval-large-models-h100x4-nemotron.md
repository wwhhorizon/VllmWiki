# vllm-project/vllm#34704: [CI Failure]: LM Eval Large Models (H100x4) - Nemotron

| 字段 | 值 |
| --- | --- |
| Issue | [#34704](https://github.com/vllm-project/vllm/issues/34704) |
| 状态 | open |
| 标签 | stale;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;quantization |
| 子分类 |  |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: LM Eval Large Models (H100x4) - Nemotron

### Issue 正文摘录

### Name of failing test `config_filename = PosixPath('/vllm-workspace/.buildkite/lm-eval-harness/configs/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8.yaml'), tp_size = '4'` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` gsm8k \| exact_match,strict-match: ground_truth=0.714 \| measured=0.660 \| rtol=0.08 -- gsm8k \| exact_match,flexible-extract: ground_truth=0.458 \| measured=0.419 \| rtol=0.08 ``` ### 📝 History of failing test unclear, some issues with buildkite runners in the past ### CC List. _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: kspace/.buildkite/lm-eval-harness/configs/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8.yaml'), tp_size = '4'` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `tra...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: LM Eval Large Models (H100x4) - Nemotron stale;ci-failure ### Name of failing test `config_filename = PosixPath('/vllm-workspace/.buildkite/lm-eval-harness/configs/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8.yaml')...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: LM Eval Large Models (H100x4) - Nemotron stale;ci-failure ### Name of failing test `config_filename = PosixPath('/vllm-workspace/.buildkite/lm-eval-harness/configs/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8.yaml'),
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: LM Eval Large Models (H100x4) - Nemotron stale;ci-failure ### Name of failing test `config_filename = PosixPath('/vllm-workspace/.buildkite/lm-eval-harness/configs/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8.yaml')...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: LM Eval Large Models (H100x4) - Nemotron stale;ci-failure ### Name of failing test `config_filename = PosixPath('/vllm-workspace/.buildkite/lm-eval-harness/configs/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8.yaml')...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
