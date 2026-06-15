# vllm-project/vllm#9413: [Performance]: inference with qwen2.5 using version vLLM 0.6.3 is felt to be slower

| 字段 | 值 |
| --- | --- |
| Issue | [#9413](https://github.com/vllm-project/vllm/issues/9413) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: inference with qwen2.5 using version vLLM 0.6.3 is felt to be slower

### Issue 正文摘录

### Your current environment Then I roughly wrote a concurrent test code ### env1: > vLLM 0.6.3 > torch 2.4.0 > transformers 4.45.2 #### test 2 times results: -- Test 100 concurrent users, round 1 -- Average response time: 20.10s Maximum response time: 35.49s Minimum response time: 2.48s Test completed, total time: 37.86s -- Test 100 concurrent users, round 1 -- Average response time: 19.19s Maximum response time: 34.13s Minimum response time: 1.02s Test completed, total time: 36.23s ### env2: > vLLM 0.5.1 > torch 2.3.0 > transformers 4.42.4 #### test 3 times results: -- Test 100 concurrent users, round 1 -- Average response time: 13.76s Maximum response time: 23.72s Minimum response time: 1.74s Test completed, total time: 25.56s -- Test 100 concurrent users, round 1 -- Average response time: 12.92s Maximum response time: 22.47s Minimum response time: 1.04s Test completed, total time: 23.36s -- Test 100 concurrent users, round 1 -- Average response time: 12.93s Maximum response time: 22.80s Minimum response time: 1.20s Test completed, total time: 23.99s Looks like it took a third more time. I found that because when I typed a single question, it didn't feel like it was taking the...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: inference with qwen2.5 using version vLLM 0.6.3 is felt to be slower performance;stale ### Your current environment Then I roughly wrote a concurrent test code ### env1: > vLLM 0.6.3 > torch 2.4.0 > trans...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Performance]: inference with qwen2.5 using version vLLM 0.6.3 is felt to be slower performance;stale ### Your current environment Then I roughly wrote a concurrent test code ### env1: > vLLM 0.6.3 > torch 2.4.0 > trans...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: *** ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e with qwen2.5 using version vLLM 0.6.3 is felt to be slower performance;stale ### Your current environment Then I roughly wrote a concurrent test code ### env1: > vLLM 0.6.3 > torch 2.4.0 > transformers 4.45.2 #### tes...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ce;stale ### Your current environment Then I roughly wrote a concurrent test code ### env1: > vLLM 0.6.3 > torch 2.4.0 > transformers 4.45.2 #### test 2 times results: -- Test 100 concurrent users, round 1 -- Average re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
