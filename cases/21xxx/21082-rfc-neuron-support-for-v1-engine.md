# vllm-project/vllm#21082: [RFC]: Neuron Support for V1 Engine

| 字段 | 值 |
| --- | --- |
| Issue | [#21082](https://github.com/vllm-project/vllm/issues/21082) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Neuron Support for V1 Engine

### Issue 正文摘录

### Motivation. This RFC discusses AWS Neuron’s plan to integrate [NeuronX Distributed (NxD) Inference](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/libraries/nxd-inference/index.html) with V1 architecture on vLLM. with: @elaineyz @mrinalks @rgrandhiamzn ### Proposed Changes. #### Change 1: Chunked prefill support — the default mechanism in V1. We have upgraded core Neuron interfaces to comply with V1 Engine and enable Chunked Prefill. No modifications to vLLM core interfaces were needed. This change offers a native implementation of Chunked Prefill — a required feature on V1. * Neuron Worker compliant with V1 Model Loader, and Model Runner. * Chunked Prefill Worker that enables chunked prefill on NxD Inference. * No modifications to vLLM Core Interfaces. #### Change 2: Optionally disable Chunked Prefill — for higher performance on Neuron. For customers who see a higher performance on Neuron without Chunked Prefill, we offer an option to disable Chunked Prefill. Option 1: New scheduler mode in V1 that disables chunked prefill (RECOMMENDED) * While we understand that chunked prefill is a defining characteristic of the V1 architecture, we believe that allowing the flexibi...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: z @mrinalks @rgrandhiamzn ### Proposed Changes. #### Change 1: Chunked prefill support — the default mechanism in V1. We have upgraded core Neuron interfaces to comply with V1 Engine and enable Chunked Prefill. No modif...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: thedocs-hosted.com/en/latest/libraries/nxd-inference/index.html) with V1 architecture on vLLM. with: @elaineyz @mrinalks @rgrandhiamzn ### Proposed Changes. #### Change 1: Chunked prefill support — the default mechanism...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: his behavior. * To opt-in to this implementation, users only need to pip install this repository in addition to vllm, and may continue to invoke vLLM exactly the same as they normally would (e.g. python -m vllm.entrypoi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: d Prefill — a required feature on V1. * Neuron Worker compliant with V1 Model Loader, and Model Runner. * Chunked Prefill Worker that enables chunked prefill on NxD Inference. * No modifications to vLLM Core Interfaces....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: uted (NxD) Inference](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/libraries/nxd-inference/index.html) with V1 architecture on vLLM. with: @elaineyz @mrinalks @rgrandhiamzn ### Proposed Changes. #### Change 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
