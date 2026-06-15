# vllm-project/vllm#21272: [Feature]: support for NVIDIA RTX 5070Ti graphics card and Windows 11 system

| 字段 | 值 |
| --- | --- |
| Issue | [#21272](https://github.com/vllm-project/vllm/issues/21272) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | install |
| Operator 关键词 | attention;cuda;kernel |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: support for NVIDIA RTX 5070Ti graphics card and Windows 11 system

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I want to install vllm in a Docker environment and load the Qwen2.5 model. My graphics card is RTX 5070Ti, and the CUDA version is 12.8. When installing the model, it shows that the CUDA kernel is incompatible. Please provide guidance and feature additions for installing this graphics card either through Docker or directly in the Windows 11 environment. Thank you! error code:CUDA error (/__w/xformers/xformers/third_party/flash-attention/hopper/flash_fwd_launch_template.h:175): no kernel image is available for execution on the device ### Alternatives / ### Additional context / ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: feature request;stale ### 🚀 The feature, motivation and pitch I want to install vllm in a Docker environment and load the Qwen2.5 model. My graphics card is RTX 5070Ti, and the CUDA version is 12.8. When installing the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Feature]: support for NVIDIA RTX 5070Ti graphics card and Windows 11 system feature request;stale ### 🚀 The feature, motivation and pitch I want to install vllm in a Docker environment and load the Qwen2.5 model. My gr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n and pitch I want to install vllm in a Docker environment and load the Qwen2.5 model. My graphics card is RTX 5070Ti, and the CUDA version is 12.8. When installing the model, it shows that the CUDA kernel is incompatib...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: upport for NVIDIA RTX 5070Ti graphics card and Windows 11 system feature request;stale ### 🚀 The feature, motivation and pitch I want to install vllm in a Docker environment and load the Qwen2.5 model. My graphics card...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
