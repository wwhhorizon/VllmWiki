# vllm-project/vllm#6241: [Performance]: empirical measurement of object serialization for input/output of worker

| 字段 | 值 |
| --- | --- |
| Issue | [#6241](https://github.com/vllm-project/vllm/issues/6241) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: empirical measurement of object serialization for input/output of worker

### Issue 正文摘录

### Proposal to improve performance currently, `LLMEngine` (driver) lives in the same process as tensor parallel rank 0 process, which caused a lot trouble for us, e.g. we cannot easily create two instances of vLLM with different GPUs. Spec decode hacks this a lot. basically, the function we care about is `LLMEngine.step`, and the core line of code is: ```python output = self.model_executor.execute_model( execute_model_req=execute_model_req) ``` when we use tensor parallel of size N, this line will: 1. process `execute_model_req` into tensors, broadcast tensors to the rest N - 1 workers 2. the worker process, together with the rest N - 1 workers, execute the model, and gather the output in the worker process if we want to separate the tp rank 0 process and the engine process, such as https://github.com/vllm-project/vllm/pull/6032 ,there will be two serialization: 1. `execute_model_req` will be serialized and sent to tp processes, even with advanced techniques, we can send once, and all processes can receive it, we still need to serialize it. 2. `output` will live in the tp rank 0 process at first, and then passed to the engine process Therefore, we need to measure how large are th...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: asurement of object serialization for input/output of worker performance;stale ### Proposal to improve performance currently, `LLMEngine` (driver) lives in the same process as tensor parallel rank 0 process, which cause...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: cost of serializing them. Here is a simple script: ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: (difference, or distance between consecutive messages) is actually quite small, in several dozens of bytes. however, the serialized data are 10x~100x larger. Why? for the output, this is because we have a very bad seria...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `LLMEngine.step`, and the core line of code is: ```python output = self.model_executor.execute_model( execute_model_req=execute_model_req) ``` when we use tensor parallel of size N, this line will: 1. process `execute_m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: niac @cadedaniel @stephanie-wang @ruisearch42 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
