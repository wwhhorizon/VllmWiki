# vllm-project/vllm#10015: [Bug]: [Bug]: vllm 启动，openai的swarm 函数调用不正常 

| 字段 | 值 |
| --- | --- |
| Issue | [#10015](https://github.com/vllm-project/vllm/issues/10015) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Bug]: vllm 启动，openai的swarm 函数调用不正常 

### Issue 正文摘录

### Your current environment Model Series Qwen2.5 What are the models used? Qwen2.5-72B-Instruct-AWQ What is the scenario where the problem happened? vllm启动 Is this a known issue? I have followed [the GitHub README](https://github.com/QwenLM/Qwen2.5). I have checked [the Qwen documentation](https://qwen.readthedocs.io/) and cannot find an answer there. I have checked the documentation of the related framework and cannot find useful information. I have searched [the issues](https://github.com/QwenLM/Qwen2.5/issues?q=is%3Aissue) and there is not a similar one. Information about environment OS: Ubuntu 22.04 Python: Python 3.11 GPUs: 4 x NVIDIA A20 NVIDIA driver: 535 (from nvidia-smi) CUDA compiler: 12.1 (from nvcc -V) PyTorch: 2.4.1+cu121 (from python -c "import troch; print(torch.version)") Log output 错误信息如下： openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': '[{\'type\': \'string_type\', \'loc\': (\'body\', \'messages\', 2, \'typed-dict\', \'content\', \'str\'), \'msg\': \'Input should be a valid string\', \'input\': None}, {\'type\': \'iterable_type\', \'loc\': (\'body\', \'messages\', 2, \'typed-dict\', \'content\', \'generator[typed-dict]\'), \'msg\': \'Inp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: thon 3.11 GPUs: 4 x NVIDIA A20 NVIDIA driver: 535 (from nvidia-smi) CUDA compiler: 12.1 (from nvcc -V) PyTorch: 2.4.1+cu121 (from python -c "import troch; print(torch.version)") Log output 错误信息如下： openai.BadRequestError...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: n of the related framework and cannot find useful information. I have searched [the issues](https://github.com/QwenLM/Qwen2.5/issues?q=is%3Aissue) and there is not a similar one. Information about environment OS: Ubuntu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ]: vllm 启动，openai的swarm 函数调用不正常 bug;stale ### Your current environment Model Series Qwen2.5 What are the models used? Qwen2.5-72B-Instruct-AWQ What is the scenario where the problem happened? vllm启动 Is this a known issu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: [Bug]: vllm 启动，openai的swarm 函数调用不正常 bug;stale ### Your current environment Model Series Qwen2.5 What are the models used? Qwen2.5-72B-Instruct-AWQ What is the scenario where the problem happened? vllm启动 Is this a...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: pe': 'BadRequestError', 'param': None, 'code': 400} Description Steps to reproduce Qwen2.5-72B-Instruct-AWQ 部署验证openai的swarm 地址https://github.com/openai/swarm swarm/examples/basic 1、vim function_calling.py =============...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
