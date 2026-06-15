# vllm-project/vllm#4100: [Bug]: --engine-use-ray is broken.

| 字段 | 值 |
| --- | --- |
| Issue | [#4100](https://github.com/vllm-project/vllm/issues/4100) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: --engine-use-ray is broken.

### Issue 正文摘录

### Your current environment N/A (happens in all env) ### 🐛 Describe the bug ``` python -m vllm.entrypoints.openai.api_server --model "facebook/opt-125m" --dtype auto --api-key token-abc123 --engine-use-ray ``` When I start an openai server with engine-use-ray, I found it crashes with the following error ``` Traceback (most recent call last): File "/home/ray/anaconda3/lib/python3.9/runpy.py", line 197, in _run_module_as_main return _run_code(code, main_globals, None, File "/home/ray/anaconda3/lib/python3.9/runpy.py", line 87, in _run_code exec(code, run_globals) File "/home/ray/default/vllm/vllm/entrypoints/openai/api_server.py", line 157, in engine = AsyncLLMEngine.from_engine_args( File "/home/ray/default/vllm/vllm/engine/async_llm_engine.py", line 347, in from_engine_args engine = cls( File "/home/ray/default/vllm/vllm/engine/async_llm_engine.py", line 311, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/home/ray/default/vllm/vllm/engine/async_llm_engine.py", line 413, in _init_engine cache_config = args[1] IndexError: tuple index out of range ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: # 🐛 Describe the bug ``` python -m vllm.entrypoints.openai.api_server --model "facebook/opt-125m" --dtype auto --api-key token-abc123 --engine-use-ray ``` When I start an openai server with engine-use-ray, I found it cr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: thon -m vllm.entrypoints.openai.api_server --model "facebook/opt-125m" --dtype auto --api-key token-abc123 --engine-use-ray ``` When I start an openai server with engine-use-ray, I found it crashes with the following er...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
