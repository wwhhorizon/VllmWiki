# vllm-project/vllm#7215: [Doc]: Bump up TensorRT-LLM version to 24.07 for comparison

| 字段 | 值 |
| --- | --- |
| Issue | [#7215](https://github.com/vllm-project/vllm/issues/7215) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Bump up TensorRT-LLM version to 24.07 for comparison

### Issue 正文摘录

### 📚 The doc issue In the current performance comparison in vLLM `README.md`, TensorRT-LLM docker container is `nvcr.io/nvidia/tritonserver:24.04-trtllm-python-py3`, and the latest version is 24.07. We should bump up trt-llm version for fair comparison. I will work on this soon. ### Suggest a potential alternative/fix _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Doc]: Bump up TensorRT-LLM version to 24.07 for comparison documentation;stale ### 📚 The doc issue In the current performance comparison in vLLM `README.md`, TensorRT-LLM docker container is `nvcr.io/nvidia/tritonserve...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: on in vLLM `README.md`, TensorRT-LLM docker container is `nvcr.io/nvidia/tritonserver:24.04-trtllm-python-py3`, and the latest version is 24.07. We should bump up trt-llm version for fair comparison. I will work on this...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Doc]: Bump up TensorRT-LLM version to 24.07 for comparison documentation;stale ### 📚 The doc issue In the current performance comparison in vLLM `README.md`, TensorRT-LLM docker container is `nvcr.io/nvidia/tritonserver...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: iner is `nvcr.io/nvidia/tritonserver:24.04-trtllm-python-py3`, and the latest version is 24.07. We should bump up trt-llm version for fair comparison. I will work on this soon. ### Suggest a potential alternative/fix _N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
