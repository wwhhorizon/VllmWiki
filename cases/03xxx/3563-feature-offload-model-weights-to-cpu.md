# vllm-project/vllm#3563: [Feature]: Offload Model Weights to CPU 

| 字段 | 值 |
| --- | --- |
| Issue | [#3563](https://github.com/vllm-project/vllm/issues/3563) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Offload Model Weights to CPU 

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am interested in adding cpu_offload_weight capability to vLLM. Wonder whether the community would like to see it happen? The following is my design. I did some simple PoC implementation. Would love to hear feedback and suggestions before investing more time on it. ________________________________________________ **Objective** The rapid expansion of AI model sizes necessitates an increased demand for GPUs with larger memory capacities. This surge poses challenges for users without access to powerful GPU resources, hindering their ability to run vLLM on numerous models. To address these challenges, we are devloping a feature called "cpu-offload-weight" to vLLM. With cpu-offload, users can now experiment with large models even without access to high-end GPUs. This democratizes access to vLLM, empowering a broader community of learners and researchers to engage with cutting-edge AI models. **Proposed Features** Upon initial loading of the model weights, cpu-offload pins the entire weight onto the CPU. During inference computation, these weights are streamed into the GPU as required. When computing on a layer, the weights are loaded into GPU fr...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ture, motivation and pitch I am interested in adding cpu_offload_weight capability to vLLM. Wonder whether the community would like to see it happen? The following is my design. I did some simple PoC implementation. Wou...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Feature]: Offload Model Weights to CPU feature request ### 🚀 The feature, motivation and pitch I am interested in adding cpu_offload_weight capability to vLLM. Wonder whether the community would like to see it happen?...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: l sizes necessitates an increased demand for GPUs with larger memory capacities. This surge poses challenges for users without access to powerful GPU resources, hindering their ability to run vLLM on numerous models. To...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: **Proposed Future Improvement** Surely, Cpu offload will increase the latency and hurt the throughput. I am going to invest more time on the following improvements: 1. Prefetching layers' weights. Namely, loading the we...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Offload Model Weights to CPU feature request ### 🚀 The feature, motivation and pitch I am interested in adding cpu_offload_weight capability to vLLM. Wonder whether the community would like to see it happen?...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
