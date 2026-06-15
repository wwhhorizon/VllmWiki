# vllm-project/vllm#4953: [New Model]: Phi-3-medium-128k-instruct support

| 字段 | 值 |
| --- | --- |
| Issue | [#4953](https://github.com/vllm-project/vllm/issues/4953) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Phi-3-medium-128k-instruct support

### Issue 正文摘录

### The model to consider. https://huggingface.co/microsoft/Phi-3-medium-128k-instruct ### The closest model vllm already supports. The older phi model (including phi-3-mini) has been supported ### What's your difficulty of supporting the model you want? I run into the following error on a 4*A6000 server: ``` [rank0]: Traceback (most recent call last): [rank0]: File "/home/hu381/miniconda3/envs/py310/lib/python3.10/runpy.py", line 196, in _run_module_as_main [rank0]: return _run_code(code, main_globals, None, [rank0]: File "/home/hu381/miniconda3/envs/py310/lib/python3.10/runpy.py", line 86, in _run_code [rank0]: exec(code, run_globals) [rank0]: File "/home/hu381/miniconda3/envs/py310/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 168, in [rank0]: engine = AsyncLLMEngine.from_engine_args( [rank0]: File "/home/hu381/miniconda3/envs/py310/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 366, in from_engine_args [rank0]: engine = cls( [rank0]: File "/home/hu381/miniconda3/envs/py310/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 324, in __init__ [rank0]: self.engine = self._init_engine(*args, **kwargs) [rank0]: File "...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [New Model]: Phi-3-medium-128k-instruct support new-model ### The model to consider. https://huggingface.co/microsoft/Phi-3-medium-128k-instruct ### The closest model vllm already supports. The older phi model (includin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: .py", line 338, in __init__ [rank0]: self.model = LlamaModel(config, quant_config, lora_config=lora_config) [rank0]: File "/home/hu381/miniconda3/envs/py310/lib/python3.10/site-packages/vllm/model_executor/models/llama....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: s/vllm/model_executor/models/llama.py", line 268, in [rank0]: LlamaDecoderLayer(config, quant_config) [rank0]: File "/home/hu381/miniconda3/envs/py310/lib/python3.10/site-packages/vllm/model_executor/models/llama.py", l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
