# vllm-project/vllm#14888: [Usage]: ModuleNotFoundError: No module named 'triton'

| 字段 | 值 |
| --- | --- |
| Issue | [#14888](https://github.com/vllm-project/vllm/issues/14888) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support |
| 子分类 | install |
| Operator 关键词 | triton |
| 症状 | import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: ModuleNotFoundError: No module named 'triton'

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi there! When I try to run the model with vLLM, I get this error: `ModuleNotFoundError: No module named ‘triton’. ` My local environment is macOS and I have successfully installed vLLM. `(base) ➜ ~ vLLM -v INFO 03-16 22:15:08 [__init__.py:256] Automatically detected platform cpu. 0.7.4.dev483+gd1ad2a57` I don't think I need to rely on nvidia to run the model through the cpu, and the documentation on cpu booting doesn't mention any dependencies on NVIDIA. So do I have to install the triton module? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: named ‘triton’. ` My local environment is macOS and I have successfully installed vLLM. `(base) ➜ ~ vLLM -v INFO 03-16 22:15:08 [__init__.py:256] Automatically detected platform cpu. 0.7.4.dev483+gd1ad2a57` I don't thin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Usage]: ModuleNotFoundError: No module named 'triton' usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi there! When I try to run the model with v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: le? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: `` ### How would you like to use vllm Hi there! When I try to run the model with vLLM, I get this error: `ModuleNotFoundError: No module named ‘triton’. ` My local environment is macOS and I have successfully installed...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development model_support triton import_error env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
