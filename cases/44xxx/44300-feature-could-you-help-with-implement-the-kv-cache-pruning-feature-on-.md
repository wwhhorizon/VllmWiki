# vllm-project/vllm#44300: [Feature]: Could you help with  implement the KV cache pruning feature on vLLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#44300](https://github.com/vllm-project/vllm/issues/44300) |
| 状态 | open |
| 标签 | feature request;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel |
| 症状 | slowdown |
| 根因提示 | memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Could you help with  implement the KV cache pruning feature on vLLM?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Now , It is very necessary to introduce KV cache pruning algorithms into vLLM, as it can bring significant performance improvements. KV cache pruning algorithms can save a significant amount of GPU memory and also greatly improve inference speed. I have optimized the accuracy of pruning algorithms from several open-source papers, achieving performance that is nearly lossless compared to the unpruned baseline. I developed the code for these pruning algorithms on DCU and integrated it into vLLM version 0.18.1. The performance of this version far exceeds the published performance reported by the paper's authors. The inference results are excellent. I hope you can adapt and integrate these code or algorithm improvements into the official vLLM repository. However, I do not have pr permission to submit a pull request, so I would like to request the necessary permissions. Currently, I can only upload part of the relevant code in the attached zip package, due to the file size limitation by upload. ``` The Hugging Face dataset for RULER can be found [here](https://huggingface.co/datasets/simonjegou/ruler). schedule: pdtriton Precision: | device | sna...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: lp with implement the KV cache pruning feature on vLLM? feature request;rocm ### 🚀 The feature, motivation and pitch Now , It is very necessary to introduce KV cache pruning algorithms into vLLM, as it can bring signifi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: the code for these pruning algorithms on DCU and integrated it into vLLM version 0.18.1. The performance of this version far exceeds the published performance reported by the paper's authors. The inference results are e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: . ``` The Hugging Face dataset for RULER can be found [here](https://huggingface.co/datasets/simonjegou/ruler). schedule: pdtriton Precision: | device | snapkv | compactor | criticaladakv-snapkv | criticaladakv-compacto...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: d [here](https://huggingface.co/datasets/simonjegou/ruler). schedule: pdtriton Precision: | device | snapkv | compactor | criticaladakv-snapkv | criticaladakv-compactor | noprune | | :------: | :------: | :------: | :--...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: PU memory and also greatly improve inference speed. I have optimized the accuracy of pruning algorithms from several open-source papers, achieving performance that is nearly lossless compared to the unpruned baseline. I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
