# vllm-project/vllm#36091: [RFC]: Add InstantTensor Support in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#36091](https://github.com/vllm-project/vllm/issues/36091) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | throughput |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Add InstantTensor Support in vLLM

### Issue 正文摘录

### Motivation. In LLM serving, model weight loading is often the dominant component of “time-to-ready”, especially for large models where hundreds of gigabytes of weights must be read and materialized into GPU memory. At the same time, modern storage and networking have advanced significantly: it is increasingly common to deploy models on servers with high-performance networked storage, where the available storage bandwidth can be very high (e.g., 400 Gbps). However, in practice the existing baselines typically fall into two categories: either extremely slow (the standard safetensors loading path), or faster but still unable to fully utilize the bandwidth of modern high-throughput network storage (e.g., fastsafetensors and runai_model_streamer). ### Proposed Change. We propose adding InstantTensor as a new weight-loading backend in vLLM (--load-format instanttensor). InstantTensor is a high-performance distributed model loader purpose-built for fast .safetensors ingestion, while still offering a user-friendly API similar to safetensors.safe_open (drop-in style usage, multi-file support, and optional torch.distributed process groups). We have already integrated InstantTensor into...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: l weight loading is often the dominant component of “time-to-ready”, especially for large models where hundreds of gigabytes of weights must be read and materialized into GPU memory. At the same time, modern storage and...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: : Add InstantTensor Support in vLLM RFC ### Motivation. In LLM serving, model weight loading is often the dominant component of “time-to-ready”, especially for large models where hundreds of gigabytes of weights must be...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ensors"] tensors = {} with safe_open(files, framework="pt", device=torch.cuda.current_device(), process_group=process_group) as f: for name, tensor in f.tensors(): tensors[name] = tensor.clone() ``` For more technical d...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: or faster but still unable to fully utilize the bandwidth of modern high-throughput network storage (e.g., fastsafetensors and runai_model_streamer). ### Proposed Change. We propose adding InstantTensor as a new weight-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: roposed Change. We propose adding InstantTensor as a new weight-loading backend in vLLM (--load-format instanttensor). InstantTensor is a high-performance distributed model loader purpose-built for fast .safetensors ing...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
