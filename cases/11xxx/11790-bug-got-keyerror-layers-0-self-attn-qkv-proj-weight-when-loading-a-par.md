# vllm-project/vllm#11790: [Bug]: Got KeyError 'layers.0.self_attn.qkv_proj.weight'  when loading a partially quantized model.

| 字段 | 值 |
| --- | --- |
| Issue | [#11790](https://github.com/vllm-project/vllm/issues/11790) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Got KeyError 'layers.0.self_attn.qkv_proj.weight'  when loading a partially quantized model.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I used llmcompressor to create a partially quantized model, where the MLP layers are quantized but the attention layers are not. When I tried to load this model using vllm, I encountered a `KeyError: 'layers.0.self_attn.qkv_proj.weight'`, as shown below. ![image](https://github.com/user-attachments/assets/50e2db37-ace3-43e9-b3bf-af4d24c307b7) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. development attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization attention;cuda;operator;quantization;triton build_error env...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: b7) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _porting;model_support;quantization attention;cuda;operator;quantization;triton build_error env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: KeyError 'layers.0.self_attn.qkv_proj.weight' when loading a partially quantized model. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I used llmcompressor to create a partia...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 'layers.0.self_attn.qkv_proj.weight' when loading a partially quantized model. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I used llmcompressor to create a partially quant...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
