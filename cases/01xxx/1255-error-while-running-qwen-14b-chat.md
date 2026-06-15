# vllm-project/vllm#1255: Error while running Qwen-14B-chat

| 字段 | 值 |
| --- | --- |
| Issue | [#1255](https://github.com/vllm-project/vllm/issues/1255) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error while running Qwen-14B-chat

### Issue 正文摘录

Tried running Qwen-14B-chat using the following command. Using vllm 0.2.0. ``` python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen-14B-Chat-Int4 --trust-remote-code ``` and got this error ``` File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_globals, None,█████████████████████████▌ | 524M/2.04G [00:06 engine = AsyncLLMEngine.from_engine_args(engine_args) File "/home/azureuser/.local/lib/python3.8/site-packages/vllm/engine/async_llm_engine.py", line 486, in from_engine_args engine = cls(engine_args.worker_use_ray, File "/home/azureuser/.local/lib/python3.8/site-packages/vllm/engine/async_llm_engine.py", line 270, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/home/azureuser/.local/lib/python3.8/site-packages/vllm/engine/async_llm_engine.py", line 306, in _init_engine return engine_class(*args, **kwargs) File "/home/azureuser/.local/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 108, in __init__ self._init_workers(distributed_init_method) File "/home/azureuser/.local/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 140, in _init_workers self._run_workers( File "/home/azureuser/....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Error while running Qwen-14B-chat Tried running Qwen-14B-chat using the following command. Using vllm 0.2.0. ``` python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen-14B-Chat-Int4 --trust-remote-code ``` and...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: on3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen-14B-Chat-Int4 --trust-remote-code ``` and got this error ``` File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
