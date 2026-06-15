# vllm-project/vllm#31028: [RFC]: AMD-Quark Online Quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#31028](https://github.com/vllm-project/vllm/issues/31028) |
| 状态 | open |
| 标签 | rocm;RFC;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: AMD-Quark Online Quantization

### Issue 正文摘录

# Motivation. Online quantization has many advantages. For example, it simplifies the model deployment by eliminating the need to use third party quantization tools for quantization. As a major quantization backend of vLLM, Quark is planning to implement online quantization in vLLM. Users can take unquantized models or even offline quantized models as input and simply set the attribute `quantization` during LLM initialization. Then, they'll get the expected online quantized models. # Proposed Change. There's an existing pipeline of running offline quantized models. We'll reuse the existing pipeline as much as possible for online quantization. ## Run offline quantized model The current pipeline of running offline quantized model is as follows: - model init - init model layers - init `quant_method` for each layer according to `quant_config` - call `create_weights` method of `quant_method` to init weight and weight_scale as torch.nn.Parameters - attach `weight_loader` to weight and weight_scale - load weights - the weight_loader attached to weight and weight_scale will be called - process_weights_after_loading - model inference: - the method `apply_weights` of `quant_method` will be...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [RFC]: AMD-Quark Online Quantization rocm;RFC;stale # Motivation. Online quantization has many advantages. For example, it simplifies the model deployment by eliminating the need to use third party quantization tools fo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Online quantization has many advantages. For example, it simplifies the model deployment by eliminating the need to use third party quantization tools for quantization. As a major quantization backend of vLLM, Quark is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ling online quantization would be setting `quantization` attribute to specific values, for example `quark_online_fp8_ptpc`, like the pseudo code shows: ```python llm = LLM( model_name=model_name, quantization="quark_onl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: AMD-Quark Online Quantization rocm;RFC;stale # Motivation. Online quantization has many advantages. For example, it simplifies the model deployment by eliminating the need to use third party quantization tools fo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: third party quantization tools for quantization. As a major quantization backend of vLLM, Quark is planning to implement online quantization in vLLM. Users can take unquantized models or even offline quantized models as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
