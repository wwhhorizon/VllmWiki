# vllm-project/vllm#8629: [Bug]: memory leak

| 字段 | 值 |
| --- | --- |
| Issue | [#8629](https://github.com/vllm-project/vllm/issues/8629) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: memory leak

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ![image](https://github.com/user-attachments/assets/f893f6eb-5bb5-4193-9cc7-619dcf285fd5) ```bash vllm serve /hestia/model/Qwen2.5-14B-Instruct-AWQ --max-model-len 16384 --quantization awq --port 8001 --swap-space 0 --served-model-name qwen --enable-auto-tool-choice --tool-call-parser hermes --num-gpu-blocks-override 1024 ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;frontend_api;hardware_porting;model_support;quantization;speculative_decoding cuda;kernel;operator;quantization;triton build_error env_de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: memory leak bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ![image](https://github.com/user-attachments/assets/f893f6eb-5bb5-4193-9cc7-619dcf285fd5) ```bash vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: memory leak bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ![image](https://github.com/user-attachments/assets/f893f6eb-5bb5-4193-9cc7-619dcf285fd5) ```bash vllm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;quantization;speculative_decoding cuda;kernel;operator;quantization;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
