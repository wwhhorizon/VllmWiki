# vllm-project/vllm#6736: [Bug]: TypeError: snapshot_download() got an unexpected keyword argument 'ignore_patterns' when set VLLM_USE_MODELSCOPE=True

| 字段 | 值 |
| --- | --- |
| Issue | [#6736](https://github.com/vllm-project/vllm/issues/6736) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TypeError: snapshot_download() got an unexpected keyword argument 'ignore_patterns' when set VLLM_USE_MODELSCOPE=True

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug start vllm with env `export VLLM_USE_MODELSCOPE=True`, got errors: ```python INFO 07-24 08:44:25 model_runner.py:680] Starting to load model LLM-Research/Meta-Llama-3.1-8B-Instruct... [rank0]: Traceback (most recent call last): [rank0]: File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main [rank0]: return _run_code(code, main_globals, None, [rank0]: File "/usr/lib/python3.10/runpy.py", line 86, in _run_code [rank0]: exec(code, run_globals) [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 317, in [rank0]: run_server(args) [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 231, in run_server [rank0]: if llm_engine is not None else AsyncLLMEngine.from_engine_args( [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 466, in from_engine_args [rank0]: engine = cls( [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 380, in __init__ [rank0]: self.engine = self._init_engine(*args, **kwargs)...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ) got an unexpected keyword argument 'ignore_patterns' when set VLLM_USE_MODELSCOPE=True bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug start vllm with env `exp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: INFO 07-24 08:44:25 model_runner.py:680] Starting to load model LLM-Research/Meta-Llama-3.1-8B-Instruct... [rank0]: Traceback (most recent call last): [rank0]: File "/usr/lib/python3.10/runpy.py", line 196, in _run_modu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ver.py", line 231, in run_server [rank0]: if llm_engine is not None else AsyncLLMEngine.from_engine_args( [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 466, in from_engine...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
