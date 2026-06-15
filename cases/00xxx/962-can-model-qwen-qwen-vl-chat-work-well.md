# vllm-project/vllm#962: can model  Qwen/Qwen-VL-Chat work well?

| 字段 | 值 |
| --- | --- |
| Issue | [#962](https://github.com/vllm-project/vllm/issues/962) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> can model  Qwen/Qwen-VL-Chat work well?

### Issue 正文摘录

when i use Qwen/Qwen-VL-Chat I do not know why! throw a error `Traceback (most recent call last): File "test.py", line 20, in model = LLM(model=model_path, tokenizer=model_path,tokenizer_mode='slow',tensor_parallel_size=1,trust_remote_code=True) File "/usr/local/miniconda3/lib/python3.8/site-packages/vllm/entrypoints/llm.py", line 66, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/usr/local/miniconda3/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 220, in from_engine_args engine = cls(*engine_configs, File "/usr/local/miniconda3/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 101, in __init__ self._init_workers(distributed_init_method) File "/usr/local/miniconda3/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 133, in _init_workers self._run_workers( File "/usr/local/miniconda3/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 470, in _run_workers output = executor(*args, **kwargs) File "/usr/local/miniconda3/lib/python3.8/site-packages/vllm/worker/worker.py", line 67, in init_model self.model = get_model(self.model_config) File "/usr/local/miniconda3/lib/python3.8/site-packages/vllm/model_executor/mo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: can model Qwen/Qwen-VL-Chat work well? new-model when i use Qwen/Qwen-VL-Chat I do not know why! throw a error `Traceback (most recent call last): File "test.py", line 20, in model = LLM(model=model_path, tokeni
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: or: 'transformer.visual.positional_embedding'` the code is `from vllm import LLM, SamplingParams from transformers import AutoModelForCausalLM, AutoTokenizer,AutoConfig import time model_path="Qwen/Qwen-VL-Chat" model =...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: t know why! throw a error `Traceback (most recent call last): File "test.py", line 20, in model = LLM(model=model_path, tokenizer=model_path,tokenizer_mode='slow',tensor_parallel_size=1,trust_remote_code=True) File "/us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
