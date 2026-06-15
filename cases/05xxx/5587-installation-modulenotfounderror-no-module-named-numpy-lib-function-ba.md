# vllm-project/vllm#5587: [Installation]: `ModuleNotFoundError: No module named 'numpy.lib.function_base'` due to NumPy 2.0 release

| 字段 | 值 |
| --- | --- |
| Issue | [#5587](https://github.com/vllm-project/vllm/issues/5587) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: `ModuleNotFoundError: No module named 'numpy.lib.function_base'` due to NumPy 2.0 release

### Issue 正文摘录

### Anything you want to discuss about vllm. Users may see the following error when trying to run vllm: ``` Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/home/waldo/venv/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 26, in from vllm.entrypoints.openai.serving_chat import OpenAIServingChat File "/home/waldo/venv/lib/python3.11/site-packages/vllm/entrypoints/openai/serving_chat.py", line 27, in from vllm.model_executor.guided_decoding import ( File "/home/waldo/venv/lib/python3.11/site-packages/vllm/model_executor/guided_decoding/__init__.py", line 6, in from vllm.model_executor.guided_decoding.lm_format_enforcer_decoding import ( File "/home/waldo/venv/lib/python3.11/site-packages/vllm/model_executor/guided_decoding/lm_format_enforcer_decoding.py", line 15, in from vllm.model_executor.guided_decoding.outlines_decoding import ( File "/home/waldo/venv/lib/python3.11/site-packages/vllm/model_executor/guided_decoding/outlines_decoding.py", line 13, in from vllm.model_executor.guided_decoding.outlines_logits_processors import ( File "/home/waldo/venv/lib/python3.11/site-packages/vllm/model...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: `ModuleNotFoundError: No module named 'numpy.lib.function_base'` due to NumPy 2.0 release installation;stale ### Anything you want to discuss about vllm. Users may see the following error when trying to r
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ecoding/outlines_logits_processors.py", line 24, in from outlines.fsm.guide import CFGGuide, Generate, Guide, RegexGuide, Write File "/home/waldo/venv/lib/python3.11/site-packages/outlines/__init__.py", line 2, in impor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: es/vllm/entrypoints/openai/serving_chat.py", line 27, in from vllm.model_executor.guided_decoding import ( File "/home/waldo/venv/lib/python3.11/site-packages/vllm/model_executor/guided_decoding/__init__.py", line 6, in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e named 'numpy.lib.function_base'` due to NumPy 2.0 release installation;stale ### Anything you want to discuss about vllm. Users may see the following error when trying to run vllm: ``` Traceback (most recent call last...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
