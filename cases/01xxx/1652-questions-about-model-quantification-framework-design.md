# vllm-project/vllm#1652: Questions about model quantification framework design

| 字段 | 值 |
| --- | --- |
| Issue | [#1652](https://github.com/vllm-project/vllm/issues/1652) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;gemm_linear;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | operator;quantization |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Questions about model quantification framework design

### Issue 正文摘录

In the current model quantification design part, the current vllm uses the layer of building the model, which is directly initialized according to the quantization algorithm to the layer required by the corresponding quantization algorithm. It is found that the existing design has two inconveniences, **especially when the number of supported models and the number of supported quantification algorithms increase**: **1. New model support:** When quantification supports a new model (currently only llama is supported), reconstruction is required and change the layer building part and weight loading of model model.py（ https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/llama.py#L52 ， https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/llama.py#L311） **2. New algorithm support:** It is not flexible enough to support new quantization algorithms. Currently, only two linear layers, column and row are abstracted. If new non-linear quantization operators are supported, the model.py part needs to be directly modified. If the number of supported algorithms increases in the future, it will As a result, the layer construction logic of model.py is compl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Questions about model quantification framework design In the current model quantification design part, the current vllm uses the layer of building the model, which is directly initialized according to the quantization a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ent model quantification design part, the current vllm uses the layer of building the model, which is directly initialized according to the quantization algorithm to the layer required by the corresponding quantization...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Questions about model quantification framework design In the current model quantification design part, the current vllm uses the layer of building the model, which is directly initialized according to the quantization a...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: to the model part of model.py. Can it be upgraded? development ci_build;gemm_linear;model_support;quantization operator;quantization build_error In the current model quantification design part, the current vllm uses the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
