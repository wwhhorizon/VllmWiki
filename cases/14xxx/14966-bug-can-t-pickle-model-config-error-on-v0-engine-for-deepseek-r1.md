# vllm-project/vllm#14966: [Bug]: can't pickle model config error on V0 engine for deepseek-r1

| 字段 | 值 |
| --- | --- |
| Issue | [#14966](https://github.com/vllm-project/vllm/issues/14966) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cache;cuda;quantization;triton |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: can't pickle model config error on V0 engine for deepseek-r1

### Issue 正文摘录

### Your current environment AFAICT it happens regardless of the GPU arch the particular version that I have tested is: vLLM API server version 0.8.0rc2.dev9+g6eaf1e5c (for cuda) ### 🐛 Describe the bug When `VLLM_USE_V1=0`, launching vLLM server with `--trust-remote-code` fails with the following error - `Can't pickle : it's not the same object as transformers_modules.configuration_deepseek.DeepseekV3Config` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nvironment AFAICT it happens regardless of the GPU arch the particular version that I have tested is: vLLM API server version 0.8.0rc2.dev9+g6eaf1e5c (for cuda) ### 🐛 Describe the bug When `VLLM_USE_V1=0`, launching vLL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: mance attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory cache;cuda;quantization;triton crash;slowdown dtype;env_dependency;memory_layout Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ug ### Your current environment AFAICT it happens regardless of the GPU arch the particular version that I have tested is: vLLM API server version 0.8.0rc2.dev9+g6eaf1e5c (for cuda) ### 🐛 Describe the bug When `VLLM_USE...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: can't pickle model config error on V0 engine for deepseek-r1 bug ### Your current environment AFAICT it happens regardless of the GPU arch the particular version that I have tested is: vLLM API server version 0.8...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _api;model_support;quantization;scheduler_memory cache;cuda;quantization;triton crash;slowdown dtype;env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
