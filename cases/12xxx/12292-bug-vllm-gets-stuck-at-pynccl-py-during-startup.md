# vllm-project/vllm#12292: [Bug]:  vLLM gets stuck at pynccl.py during startup

| 字段 | 值 |
| --- | --- |
| Issue | [#12292](https://github.com/vllm-project/vllm/issues/12292) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;quantization;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  vLLM gets stuck at pynccl.py during startup

### Issue 正文摘录

### Your current environment When I start vLLM, it gets stuck at a step in pynccl.py and cannot proceed to model loading. At this point, I have to enable the export NCCL_P2P_DISABLE=1 parameter to load the model, but this significantly reduces inference speed. After rebooting the server, vLLM can start normally again. I am unsure of the reason for this issue and how to resolve it. Here is the version information of my server, NVIDIA driver, NCCL, and PyTorch, along with specific log details: ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I start vLLM, it gets stuck at a step in pynccl.py and cannot proceed to model loading. At this point, I have to enable the export NCCL_P2P_DISABLE=1 parameter to load the model, but this significantly reduces inference speed. After rebooting the server, vLLM can start normally again. I am unsure of the reason for this issue and how to resolve it. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: m unsure of the reason for this issue and how to resolve it. Here is the version information of my server, NVIDIA driver, NCCL, and PyTorch, along with specific log details: ### Model Input Dumps _No response_ ### 🐛 Des...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: d questions. performance distributed_parallel;frontend_api;model_support;quantization cuda;quantization;triton dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: I start vLLM, it gets stuck at a step in pynccl.py and cannot proceed to model loading. At this point, I have to enable the export NCCL_P2P_DISABLE=1 parameter to load the model, but this significantly reduces inference...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;model_support;quantization cuda;quantization;triton dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
