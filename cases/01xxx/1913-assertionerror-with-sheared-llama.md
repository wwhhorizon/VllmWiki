# vllm-project/vllm#1913: AssertionError with Sheared Llama

| 字段 | 值 |
| --- | --- |
| Issue | [#1913](https://github.com/vllm-project/vllm/issues/1913) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AssertionError with Sheared Llama

### Issue 正文摘录

I run into following error while trying to run sheared llama 1.3B sharegpt `llm = LLM(model="princeton-nlp/Sheared-LLaMA-1.3B-ShareGPT", max_model_len=4096)` ``` Traceback (most recent call last): File "/home/ai/ml/llm/inference/vllm/inference.py", line 112, in llm = LLM(model="/home/ai/ml/llm/models/llama/shear-1.3B-ShareGPT/bf16", max_model_len=4096, tensor_parallel_size=1) File "/home/ai/.mconda3/envs/vllm/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 93, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/home/ai/.mconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 231, in from_engine_args engine = cls(*engine_configs, File "/home/ai/.mconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 110, in __init__ self._init_workers(distributed_init_method) File "/home/ai/.mconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 142, in _init_workers self._run_workers( File "/home/ai/.mconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 700, in _run_workers output = executor(*args, **kwargs) File "/home/ai/.mconda3/envs/vllm/lib/python3.10/site-p...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: AssertionError with Sheared Llama I run into following error while trying to run sheared llama 1.3B sharegpt `llm = LLM(model="princeton-nlp/Sheared-LLaMA-1.3B-ShareGPT", max_model_len=4096)` ``` Traceback (most recent...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: llm = LLM(model="/home/ai/ml/llm/models/llama/shear-1.3B-ShareGPT/bf16", max_model_len=4096, tensor_parallel_size=1) File "/home/ai/.mconda3/envs/vllm/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 93, in _...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e-packages/vllm/model_executor/models/llama.py", line 240, in LlamaDecoderLayer(config, linear_method) File "/home/ai/.mconda3/envs/vllm/lib/python3.10/site-packages/vllm/model_executor/models/llama.py", line 173, in __...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
