# vllm-project/vllm#12247: [Usage]: Does vLLM support running the DeepSeek-V3 model with CUDA 11.8?

| 字段 | 值 |
| --- | --- |
| Issue | [#12247](https://github.com/vllm-project/vllm/issues/12247) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does vLLM support running the DeepSeek-V3 model with CUDA 11.8?

### Issue 正文摘录

I'm trying to use the DeepSeek-V3 model with vLLM, but I'm currently using CUDA 11.8. The latest vLLM documentation and releases seem to focus on newer CUDA versions. Is there compatibility or a specific version of vLLM that supports DeepSeek-V3 inference with CUDA 11.8? If not, what's the minimum CUDA version required for running DeepSeek-V3 with vLLM?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: . The latest vLLM documentation and releases seem to focus on newer CUDA versions. Is there compatibility or a specific version of vLLM that supports DeepSeek-V3 inference with CUDA 11.8? If not, what's the minimum CUDA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage]: Does vLLM support running the DeepSeek-V3 model with CUDA 11.8? usage;stale I'm trying to use the DeepSeek-V3 model with vLLM, but I'm currently using CUDA 11.8. The latest vLLM documentation and releases seem...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Does vLLM support running the DeepSeek-V3 model with CUDA 11.8? usage;stale I'm trying to use the DeepSeek-V3 model with vLLM, but I'm currently using CUDA 11.8. The latest vLLM documentation and releases seem...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: Does vLLM support running the DeepSeek-V3 model with CUDA 11.8? usage;stale I'm trying to use the DeepSeek-V3 model with vLLM, but I'm currently using CUDA 11.8. The latest vLLM documentation and releases seem to foc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: he DeepSeek-V3 model with vLLM, but I'm currently using CUDA 11.8. The latest vLLM documentation and releases seem to focus on newer CUDA versions. Is there compatibility or a specific version of vLLM that supports Deep...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
