# vllm-project/vllm#15581: [Bug]: Custom logging via VLLM_LOGGING_CONFIG_PATH causes server crash with "Cannot unpickle PostGradPassManager"

| 字段 | 值 |
| --- | --- |
| Issue | [#15581](https://github.com/vllm-project/vllm/issues/15581) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Custom logging via VLLM_LOGGING_CONFIG_PATH causes server crash with "Cannot unpickle PostGradPassManager"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Docker image `vllm/vllm-openai:v0.8.1` running on a Kubernetes cluster. I tried to create a custom logger config following [the official guide](https://docs.vllm.ai/en/latest/getting_started/examples/logging_configuration.html#logging-configuration). 1. Created a [logger-config.json](https://docs.vllm.ai/en/latest/getting_started/examples/logging_configuration.html#example-1-customize-vllm-root-logger) by copy-pasting the [example](https://docs.vllm.ai/en/latest/getting_started/examples/logging_configuration.html#example-1-customize-vllm-root-logger) and then exporting the `VLLM_LOGGING_CONFIG_PATH` pointing to the config. (On K8S platform) 1. Server started to run, and logging format was changed to json as expected but soon it crashed with an error. 1. Removed the `VLLM_LOGGING_CONFIG_PATH` environment variable and tried again. Now server was running fine without error. 1. Added `VLLM_LOGGING_CONFIG_PATH` environment again and the same crash occurred. [ecdollm-x-vllm1gpu-5ff86dfb4b-g9t5h-app.log](https://github.com/user-attachments/files/19476679/ecdollm-x-vllm1gpu-5ff86dfb4b-g9t5h-app.log) End of the error: `File \"/opt/venv/li...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: assManager" bug ### Your current environment ### 🐛 Describe the bug Docker image `vllm/vllm-openai:v0.8.1` running on a Kubernetes cluster. I tried to create a custom logger config following [the official guide](https:/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: LOGGING_CONFIG_PATH causes server crash with "Cannot unpickle PostGradPassManager" bug ### Your current environment ### 🐛 Describe the bug Docker image `vllm/vllm-openai:v0.8.1` running on a Kubernetes cluster. I tried...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Custom logging via VLLM_LOGGING_CONFIG_PATH causes server crash with "Cannot unpickle PostGradPassManager" bug ### Your current environment ### 🐛 Describe the bug Docker image `vllm/vllm-openai:v0.8.1` running on...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e ValueError(\"Cannot unpickle PostGradPassManager\")\ntorch._dynamo.exc.BackendCompilerFailed: backend=' ' raised:\nValueError: Cannot unpickle PostGradPassManager\n\nWhile executing %submod_0 : [num_users=5] = call_mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
