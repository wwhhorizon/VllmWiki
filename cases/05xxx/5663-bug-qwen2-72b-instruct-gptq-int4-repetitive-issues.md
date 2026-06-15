# vllm-project/vllm#5663: [Bug]: Qwen2-72B-Instruct-gptq-int4 Repetitive issues

| 字段 | 值 |
| --- | --- |
| Issue | [#5663](https://github.com/vllm-project/vllm/issues/5663) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen2-72B-Instruct-gptq-int4 Repetitive issues

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Machine A800, VLLM 0.5.0, PROMPT=开始, output max tokens = 2048, Temperature sets 0.7 VLLM loads Qwen2-72b-InStruct-GPTQ-IT4, and uses the Benchmark script of VLLM to do concurrent testing. Whether it is a concurrent limit or 10 concurrency restrictions, the output will be repeated. https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_serving.py ![image](https://github.com/vllm-project/vllm/assets/57557769/f3440a14-71a1-4b8c-b3e4-6a66aaba4aa8)

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: mperature sets 0.7 VLLM loads Qwen2-72b-InStruct-GPTQ-IT4, and uses the Benchmark script of VLLM to do concurrent testing. Whether it is a concurrent limit or 10 concurrency restrictions, the output will be repeated. ht...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Qwen2-72B-Instruct-gptq-int4 Repetitive issues bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Machine A800, VLLM 0.5.0, PROMPT=开始, output max token...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Qwen2-72B-Instruct-gptq-int4 Repetitive issues bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Machine A800, VLLM 0.5.0, PROMPT=开始, output max token...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Qwen2-72B-Instruct-gptq-int4 Repetitive issues bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Machine A800, VLLM 0.5.0, PROMPT=开始, output max token...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
