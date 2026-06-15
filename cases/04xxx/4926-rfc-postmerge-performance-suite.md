# vllm-project/vllm#4926: [RFC]: Postmerge performance suite

| 字段 | 值 |
| --- | --- |
| Issue | [#4926](https://github.com/vllm-project/vllm/issues/4926) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | fp8 |
| 症状 | build_error;slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Postmerge performance suite

### Issue 正文摘录

### Motivation. We want to start tracking performance numbers of vLLM on more realistic workloads. Thanks to our sponsors #4925 we are getting a pool of hardware resources ready to run the testing on. The goal of this test suite is to 1. Track regression 2. Track our progress in optimization ### Proposed Change. We will start with running the following benchmarks: * Llama 8B on A100, H100 * Llama 70B on 4xA100, 4xH100, 8xA100, 8xH100 * Mixtral 8x7B on 8xH100 * Mixtral 8x22B on 8xH100 We will run with the following parameters: - chunked prefill enabled - fp8 We will run with the following tests: - Benchmark latency - Benchmark throughput with 1000 prompts (ShareGPT) - Benchmark serving with 1000 prompts (ShareGPT) We will also compare with TGI and TRT-LLM. ### Feedback Period. Step 1: Ensure hardware availabilities Step 2: Setup pipeline for Llama 8B on H100 as a proof of concept Step 3: Monitor the result, build dashboard Step 4: Scale to other tests as resources come online. ### CC List. _No response_ ### Any Other Things. Suggestion welcomed.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: nsors #4925 we are getting a pool of hardware resources ready to run the testing on. The goal of this test suite is to 1. Track regression 2. Track our progress in optimization ### Proposed Change. We will start with ru...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: We will run with the following parameters: - chunked prefill enabled - fp8 We will run with the following tests: - Benchmark latency - Benchmark throughput with 1000 prompts (ShareGPT) - Benchmark serving with 1000 prom...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e for Llama 8B on H100 as a proof of concept Step 3: Monitor the result, build dashboard Step 4: Scale to other tests as resources come online. ### CC List. _No response_ ### Any Other Things. Suggestion welcomed. perfo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ge. We will start with running the following benchmarks: * Llama 8B on A100, H100 * Llama 70B on 4xA100, 4xH100, 8xA100, 8xH100 * Mixtral 8x7B on 8xH100 * Mixtral 8x22B on 8xH100 We will run with the following parameter...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Postmerge performance suite RFC;stale ### Motivation. We want to start tracking performance numbers of vLLM on more realistic workloads. Thanks to our sponsors #4925 we are getting a pool of hardware resources re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
