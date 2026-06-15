# vllm-project/vllm#10294: [Feature]: Quark quantization format  upstream to VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#10294](https://github.com/vllm-project/vllm/issues/10294) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cache;fp8;moe;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Quark quantization format  upstream to VLLM

### Issue 正文摘录

Quark is a comprehensive cross-platform toolkit designed to simplify and enhance the quantization of deep learning models. Supporting both PyTorch and ONNX models, Quark empowers developers to optimize their models for deployment on a wide range of hardware backends, achieving significant performance gains without compromising accuracy. Here is the introduction to [Quark.](https://quark.docs.amd.com) Currently, the format of the quantized model exported by Quark is different from the formats supported by VLLM, so we need to contribute codes to VLLM to add support for the Quark format. ### Quark Format 1) [configuration file config.json of Quark format](https://huggingface.co/amd/Meta-Llama-2-7B-chat-hf-awq-uint4-asym-g128-bf16/blob/main/config.json) 2) key names and data types of Quark safetensors ``` model.layers.1.self_attn.k_proj.input_scale, torch.float16 model.layers.1.self_attn.k_proj.weight, torch.float8_e4m3fn model.layers.1.self_attn.k_proj.weight_scale, torch.float16 model.layers.1.self_attn.o_proj.input_scale, torch.float16 model.layers.1.self_attn.o_proj.weight, torch.float8_e4m3fn model.layers.1.self_attn.o_proj.weight_scale, torch.float16 model.layers.1.self_attn.q_p...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Feature]: Quark quantization format upstream to VLLM feature request;stale Quark is a comprehensive cross-platform toolkit designed to simplify and enhance the quantization of deep learning models. Supporting both PyTo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Feature]: Quark quantization format upstream to VLLM feature request;stale Quark is a comprehensive cross-platform toolkit designed to simplify and enhance the quantization of deep learning models. Supporting both PyTo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Quark quantization format upstream to VLLM feature request;stale Quark is a comprehensive cross-platform toolkit designed to simplify and enhance the quantization of deep learning models. Supporting both PyTo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pers to optimize their models for deployment on a wide range of hardware backends, achieving significant performance gains without compromising accuracy. Here is the introduction to [Quark.](https://quark.docs.amd.com)...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: e backends, achieving significant performance gains without compromising accuracy. Here is the introduction to [Quark.](https://quark.docs.amd.com) Currently, the format of the quantized model exported by Quark is diffe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
