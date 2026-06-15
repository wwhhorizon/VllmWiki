# vllm-project/vllm#3844: [Installation]: missing dependencies in neuron requirements

| 字段 | 值 |
| --- | --- |
| Issue | [#3844](https://github.com/vllm-project/vllm/issues/3844) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: missing dependencies in neuron requirements

### Issue 正文摘录

The following packages are missing from the neuron requirements: `ray` `outlines`. After installing with the following commands: ```sh pip install -U -r requirements-neuron.txt pip install . ``` I get the following error when launching the server (here omitting parameters for simplicity as the error is identical): ``` $ python -m vllm.entrypoints.openai.api_server WARNING 04-04 08:51:34 ray_utils.py:70] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For distributed inference, please install Ray with `pip install ray`. Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/home/ubuntu/dev/vllm/vllm/entrypoints/openai/api_server.py", line 22, in from vllm.entrypoints.openai.serving_chat import OpenAIServingChat File "/home/ubuntu/dev/vllm/vllm/entrypoints/openai/serving_chat.py", line 15, in from vllm.model_executor.guided_decoding import ( File "/home/ubuntu/dev/vllm/vllm/model_executor/guided_decoding.py", line 15, in from vllm.model_executor.guided_logits_processors import (C...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: missing dependencies in neuron requirements installation;stale The following packages are missing from the neuron requirements: `ray` `outlines`. After installing with the following commands: ```sh pip i
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: _executor/guided_logits_processors.py", line 22, in from outlines.fsm.fsm import CFGFSM, RegexFSM ModuleNotFoundError: No module named 'outlines' ``` ### Your current environment ```text PyTorch version: 2.1.2+cu121 Is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: lm/vllm/entrypoints/openai/serving_chat.py", line 15, in from vllm.model_executor.guided_decoding import ( File "/home/ubuntu/dev/vllm/vllm/model_executor/guided_decoding.py", line 15, in from vllm.model_executor.guided...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Installation]: missing dependencies in neuron requirements installation;stale The following packages are missing from the neuron requirements: `ray` `outlines`. After installing with the following commands: ```sh pip i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: x==2.1.2.2.1.0 [pip3] torch-xla==2.1.2 [pip3] torchvision==0.16.2 [pip3] triton==2.1.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: (0, 'instance-type: inf2.48xlarge instance-id: i-0c551a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
