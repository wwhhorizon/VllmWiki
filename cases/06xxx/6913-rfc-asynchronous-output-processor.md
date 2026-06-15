# vllm-project/vllm#6913: [RFC]: Asynchronous Output Processor

| 字段 | 值 |
| --- | --- |
| Issue | [#6913](https://github.com/vllm-project/vllm/issues/6913) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Asynchronous Output Processor

### Issue 正文摘录

### Motivation. Each decoding step inside LLMEngine does the following: schedules the sequences to be executed in the next iteration, executes the model and process model outputs. GPU remains largely blocked while executing `_process_model_outputs()` in `LLMEngine`. We ran detailed profiling with LLaMa3-70B-instruct on 4xH100 (FP8 scales) and measured time taken by this function inside `LLMEngine`. Case study: Model: Llama3-70B Hardware: 4xH100 Dtype: FP8 dynamic scaling 128 input tokens, varying batch sizes | Batch size | TPOT (ms) | Time taken by `_process_model_outputs` (ms) | Expected reduction in TPOT (ms) | | --- | --- | --- | --- | | 1 | 19 | 0.2 | 0.6% | | 32 | 25 | 3.4 | 2.1% | | 1024 | 19 | 0.2 | 20% | [Note: I'm generating new numbers using latest `main` branch. Will update soon.] Above numbers are conservative estimates for performance improvement. ### Proposed Change. Currently, sampler is just waiting for CPU-GPU synchronization. This solution takes advantage of this idle time and proposes to asynchronously process output while forward pass is being executed on GPU. **High-level changes** Introducing a new RPC server+client inside AsnycLLMEngine to run model output p...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [RFC]: Asynchronous Output Processor RFC;stale ### Motivation. Each decoding step inside LLMEngine does the following: schedules the sequences to be executed in the next iteration, executes the model and process model o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Engine`. We ran detailed profiling with LLaMa3-70B-instruct on 4xH100 (FP8 scales) and measured time taken by this function inside `LLMEngine`. Case study: Model: Llama3-70B Hardware: 4xH100 Dtype: FP8 dynamic scaling 1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: e executing `_process_model_outputs()` in `LLMEngine`. We ran detailed profiling with LLaMa3-70B-instruct on 4xH100 (FP8 scales) and measured time taken by this function inside `LLMEngine`. Case study: Model: Llama3-70B...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: hedules the sequences to be executed in the next iteration, executes the model and process model outputs. GPU remains largely blocked while executing `_process_model_outputs()` in `LLMEngine`. We ran detailed profiling...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: le forward pass is being executed on GPU. **High-level changes** Introducing a new RPC server+client inside AsnycLLMEngine to run model output processing in a separate process. This server will exclusively do all ops in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
