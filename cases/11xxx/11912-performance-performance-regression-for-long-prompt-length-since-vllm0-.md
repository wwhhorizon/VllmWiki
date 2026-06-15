# vllm-project/vllm#11912: [Performance]: Performance regression for long prompt length since vLLM0.6.4.post1 

| 字段 | 值 |
| --- | --- |
| Issue | [#11912](https://github.com/vllm-project/vllm/issues/11912) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | fp8;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Performance regression for long prompt length since vLLM0.6.4.post1 

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression I tested the efficiency/speed of llama3.1-70b-instruct with some internal dataset, basically to summarize some long reports (the average prompt length is around 8000x), using benchmarking_serving.py from vllm https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_serving.py. The model I used was llama3.1-70b-instruct, quantized with fp8-dynamic. I used 8 h100, tensor parallelism=4, and two replicas. However, it seems that the mean time of output token is much larger with newer versions of vLLM (since 0.6.4.post1) For example, with QPS=0.2, it increases from 15.7 ms to 25.7. The difference is quite large, so just check whether there are some insights on this. Other details of the deployment: ``` - '--gpu-memory-utilization=0.96' - '--tensor-parallel-size=2' - '--enable-chunked-prefill' - '--max-num-batched-tokens=4096' - '--enable-auto-tool-choice' - '--tool-call-parser=llama3_json' - '--chat-template=tool_chat_template_llama3.1_json.jinja' ``` Thanks a lot! ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e _No response_ ### Report of performance regression I tested the efficiency/speed of llama3.1-70b-instruct with some internal dataset, basically to summarize some long reports (the average prompt length is around 8000x...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: hmarks/benchmark_serving.py. The model I used was llama3.1-70b-instruct, quantized with fp8-dynamic. I used 8 h100, tensor parallelism=4, and two replicas. However, it seems that the mean time of output token is much la...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: l I used was llama3.1-70b-instruct, quantized with fp8-dynamic. I used 8 h100, tensor parallelism=4, and two replicas. However, it seems that the mean time of output token is much larger with newer versions of vLLM (sin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: Performance regression for long prompt length since vLLM0.6.4.post1 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I tested the efficiency/speed o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### Report of performance regression I tested the efficiency/speed of llama3.1-70b-instruct with some internal dataset, basically to summarize some long reports (the average prompt length is around 8000x), using benchma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
