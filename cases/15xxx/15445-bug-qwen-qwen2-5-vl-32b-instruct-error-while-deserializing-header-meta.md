# vllm-project/vllm#15445: [Bug]: Qwen/Qwen2.5-VL-32B-Instruct Error while deserializing header: MetadataIncompleteBuffer ProcessGroupNCCL.cpp:1496]

| 字段 | 值 |
| --- | --- |
| Issue | [#15445](https://github.com/vllm-project/vllm/issues/15445) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen/Qwen2.5-VL-32B-Instruct Error while deserializing header: MetadataIncompleteBuffer ProcessGroupNCCL.cpp:1496]

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm==0.8.1 transformers==4.50.0 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen/Qwen2.5-VL-32B-Instruct Error while deserializing header: MetadataIncompleteBuffer ProcessGroupNCCL.cpp:1496] bug ### Your current environment ### 🐛 Describe the bug vllm==0.8.1 transformers==4.50.0 ### Befo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: _kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization cuda;operator;quantization crash dtype;env_dependency;shape Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0.0 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t;multimodal_vlm;quantization cuda;operator;quantization crash dtype;env_dependency;shape Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: Qwen/Qwen2.5-VL-32B-Instruct Error while deserializing header: MetadataIncompleteBuffer ProcessGroupNCCL.cpp:1496] bug ### Your current environment ### 🐛 Describe the bug vllm==0.8.1 transformers==4.50.0 ### Befo...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
