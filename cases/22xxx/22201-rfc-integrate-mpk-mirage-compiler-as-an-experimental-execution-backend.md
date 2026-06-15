# vllm-project/vllm#22201: [RFC]: Integrate MPK (Mirage) compiler as an experimental execution backend to vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#22201](https://github.com/vllm-project/vllm/issues/22201) |
| 状态 | open |
| 标签 | RFC;torch.compile |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;kernel;operator;quantization |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Integrate MPK (Mirage) compiler as an experimental execution backend to vLLM

### Issue 正文摘录

### Motivation. LLM inference, especially for smaller and middle-size models, still fails to attain the theoretical maximums in TFLOPs and memory bandwidth. There are many reasons for this, from CPU overheads and kernel launch overheads to other pipeline bubbles like tail latencies in GPU kernel execution. While CUDA Graphs help to some extent, one promising approach is compiling megakernels that use precision scheduling. A megakernel is a single GPU kernel where SMs read and execute “tasks” corresponding to different compute or memory operations. This can eliminate a lot of the aforementioned latencies due to better overlapping of operations, reduced memory load, and higher hardware utilization. MPK/Mirage is a megakernel compiler that takes in model definitions in its custom DSL and produces a single megakernel for the full model forward pass. This RFC proposes adding Mirage as an experimental torch.compile-based backend to vLLM. According to [the Mirage blog post](https://zhihaojia.medium.com/compiling-llms-into-a-megakernel-a-path-to-low-latency-inference-cf7840913c17), Mirage demonstrates a 20-25% improvement in forward pass latency over vLLM. I would kindly like to ask the M...

## 现有链接修复摘要

#20059 [Core] Allow full cudagraph with separate attention routines and orthogonal to compilation, add support for FA2 and FlashInfer

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [RFC]: Integrate MPK (Mirage) compiler as an experimental execution backend to vLLM RFC;torch.compile ### Motivation. LLM inference, especially for smaller and middle-size models, still fails to attain the theoretical m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: to vLLM RFC;torch.compile ### Motivation. LLM inference, especially for smaller and middle-size models, still fails to attain the theoretical maximums in TFLOPs and memory bandwidth. There are many reasons for this, fro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e ### Motivation. LLM inference, especially for smaller and middle-size models, still fails to attain the theoretical maximums in TFLOPs and memory bandwidth. There are many reasons for this, from CPU overheads and kern...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ps://zhihaojia.medium.com/compiling-llms-into-a-megakernel-a-path-to-low-latency-inference-cf7840913c17), Mirage demonstrates a 20-25% improvement in forward pass latency over vLLM. I would kindly like to ask the Mirage...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [RFC]: Integrate MPK (Mirage) compiler as an experimental execution backend to vLLM RFC;torch.compile ### Motivation. LLM inference, especially for smaller and middle-size models, still fails to attain the theoretical m...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20059](https://github.com/vllm-project/vllm/pull/20059) | mentioned | 0.45 | [Core] Allow full cudagraph with separate attention routines and orthogonal to compilation, add support for FA2 and FlashInfer | not necessary as we’re only launching a single kernel. however, with #20059, we should be able to use full cudagraphs anyway, which might be helpful if we have to split the graph… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
