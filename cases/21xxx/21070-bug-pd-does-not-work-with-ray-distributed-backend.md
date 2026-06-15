# vllm-project/vllm#21070: [Bug]: PD does not work with ray distributed backend

| 字段 | 值 |
| --- | --- |
| Issue | [#21070](https://github.com/vllm-project/vllm/issues/21070) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: PD does not work with ray distributed backend

### Issue 正文摘录

### Your current environment It turns out after https://github.com/vllm-project/vllm/pull/19555, choosing ray distributed executor backend along with nixl_connector is broken. The reason is that the changes to multiProcExecutor are not replicated for ray executor, so the ray executor will hang making D wait indefinitely for P (since finished_recving and finished_sending are not properly filled out) ### 🐛 Describe the bug N/A ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization quantization build_error env_dependency Your current enviro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: PD does not work with ray distributed backend bug;ray ### Your current environment It turns out after https://github.com/vllm-project/vllm/pull/19555, choosing ray distributed executor backend along with nixl_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization quantization build_error env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: N/A ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization quantization build_error env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
