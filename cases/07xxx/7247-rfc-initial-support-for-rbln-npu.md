# vllm-project/vllm#7247: [RFC]: Initial support for RBLN NPU

| 字段 | 值 |
| --- | --- |
| Issue | [#7247](https://github.com/vllm-project/vllm/issues/7247) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Initial support for RBLN NPU

### Issue 正文摘录

### Motivation. The [RBLN SDK](https://rebellions.ai/wp-content/uploads/2024/08/WhitePaper_Issue2_ATOM_SoftwareStack.pdf) provides a solution for innovative deep learning inference on Rebellion's NPUs, such as [ATOM](https://rebellions.ai/wp-content/uploads/2024/07/ATOMgenAI_white-paper.pdf) and REBEL, including support for large language models (LLMs). This project aims to develop the RBLN backend for vLLM, initially prioritizing the ATOM device, with future plans to enable REBEL support. In alignment with Rebellion's Optimum Huggingface extension [documentation](https://docs.rbln.ai/software/optimum/optimum_rbln.html), RBLN backend will support a wide range of models available in the [Rebellion's Model Zoo](https://rebellions.ai/developers/model-zoo/). The project currently incorporates continuous batching feature and will soon integrate additional techniques, such as PagedAttention, to enhance performance further. ### Proposed Change. Introduce the RBLN vLLM backend, which will: - Load models via the optimum-rbln extension for Hugging Face ([documentation](https://docs.rbln.ai/software/optimum/optimum_rbln.html)) - Implement custom RBLN model loader, model runner, model executo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: OMgenAI_white-paper.pdf) and REBEL, including support for large language models (LLMs). This project aims to develop the RBLN backend for vLLM, initially prioritizing the ATOM device, with future plans to enable REBEL s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Initial support for RBLN NPU RFC;stale ### Motivation. The [RBLN SDK](https://rebellions.ai/wp-content/uploads/2024/08/WhitePaper_Issue2_ATOM_SoftwareStack.pdf) provides a solution for innovative deep learning in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: m.rbln, model_cls_name) assert model_cls is not None # load RBLN compiler binary model model = model_cls.from_pretrained(model_name_or_path, export=False) self.model = model ``` ##### Model-specific (e.g. llama specific...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: model model = model_cls.from_pretrained(model_name_or_path, export=False) self.model = model ``` ##### Model-specific (e.g. llama specific) forward functions ```python class RBLNOptimumRBLNLlamaForCausalLM(RBLNBaseLlama...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: for large language models (LLMs). This project aims to develop the RBLN backend for vLLM, initially prioritizing the ATOM device, with future plans to enable REBEL support. In alignment with Rebellion's Optimum Huggingf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
