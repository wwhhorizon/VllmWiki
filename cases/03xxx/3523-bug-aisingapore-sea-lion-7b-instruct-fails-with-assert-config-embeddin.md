# vllm-project/vllm#3523: [Bug]: aisingapore/sea-lion-7b-instruct fails with assert config.embedding_fraction == 1.0

| 字段 | 值 |
| --- | --- |
| Issue | [#3523](https://github.com/vllm-project/vllm/issues/3523) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: aisingapore/sea-lion-7b-instruct fails with assert config.embedding_fraction == 1.0

### Issue 正文摘录

### Your current environment python 3.10 vllm 0.3.3 ### 🐛 Describe the bug https://huggingface.co/aisingapore/sea-lion-7b-instruct/blob/main/config.json ``` WARNING 03-20 04:11:30 tokenizer.py:64] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. Traceback (most recent call last): File "/h2ogpt_conda/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/h2ogpt_conda/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/h2ogpt_conda/vllm_env/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 237, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/h2ogpt_conda/vllm_env/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 625, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/h2ogpt_conda/vllm_env/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 321, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/h2ogpt_conda/vllm_env/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 366, in _init_engine return engine_class(*args, **kwarg...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: aisingapore/sea-lion-7b-instruct fails with assert config.embedding_fraction == 1.0 bug ### Your current environment python 3.10 vllm 0.3.3 ### 🐛 Describe the bug https://huggingface.co/aisingapore/sea-lion-7b-in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
