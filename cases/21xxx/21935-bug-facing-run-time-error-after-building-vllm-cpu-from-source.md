# vllm-project/vllm#21935: [Bug]: Facing run time error after building vllm cpu from source

| 字段 | 值 |
| --- | --- |
| Issue | [#21935](https://github.com/vllm-project/vllm/issues/21935) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Facing run time error after building vllm cpu from source

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Unable to build cpu wheels on cpu without using gpu. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Facing run time error after building vllm cpu from source bug ### Your current environment ### 🐛 Describe the bug Unable to build cpu wheels on cpu without using gpu. ### Before submitting a new issue... - [x] M
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: activation_norm;ci_build;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding activation;cuda;operator;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your cur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: u. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: n;sampling_logits;speculative_decoding activation;cuda;operator;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ions. correctness activation_norm;ci_build;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding activation;cuda;operator;sampling;triton build_error;crash;nan_inf dtype;env_d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
