# vllm-project/vllm#4306: [New Model]: Support Phi-3

| 字段 | 值 |
| --- | --- |
| Issue | [#4306](https://github.com/vllm-project/vllm/issues/4306) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Support Phi-3

### Issue 正文摘录

### The model to consider. https://huggingface.co/microsoft/Phi-3-mini-128k-instruct https://huggingface.co/microsoft/Phi-3-mini-4k-instruct ### The closest model vllm already supports. Phi-2 (which uses the same transformers model as Phi-1) ### What's your difficulty of supporting the model you want? Support for LongRope #3575 I tried running `Phi-3-mini-128k-instruct` but got this error: ``` langbench-vllm-1 | Traceback (most recent call last): langbench-vllm-1 | File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main langbench-vllm-1 | return _run_code(code, main_globals, None, langbench-vllm-1 | File "/usr/lib/python3.10/runpy.py", line 86, in _run_code langbench-vllm-1 | exec(code, run_globals) langbench-vllm-1 | File "/workspace/vllm/entrypoints/openai/api_server.py", line 157, in langbench-vllm-1 | engine = AsyncLLMEngine.from_engine_args( langbench-vllm-1 | File "/workspace/vllm/engine/async_llm_engine.py", line 331, in from_engine_args langbench-vllm-1 | engine_config = engine_args.create_engine_config() langbench-vllm-1 | File "/workspace/vllm/engine/arg_utils.py", line 406, in create_engine_config langbench-vllm-1 | model_config = ModelConfig( langbench-vl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: Support Phi-3 new-model ### The model to consider. https://huggingface.co/microsoft/Phi-3-mini-128k-instruct https://huggingface.co/microsoft/Phi-3-mini-4k-instruct ### The closest model vllm already suppor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
