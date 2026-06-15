# vllm-project/vllm#2676: Add support for long-context beacon models: KeyError: 'model.beacon_embed_tokens.weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#2676](https://github.com/vllm-project/vllm/issues/2676) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add support for long-context beacon models: KeyError: 'model.beacon_embed_tokens.weight'

### Issue 正文摘录

https://github.com/FlagOpen/FlagEmbedding/tree/master/Long_LLM/activation_beacon https://huggingface.co/namespace-Pt/activation-beacon-llama2-7b-chat/tree/main https://arxiv.org/abs/2401.03462 Currently fails with: ``` Traceback (most recent call last): 71%|??????? | 3.53G/4.97G [00:37 engine = AsyncLLMEngine.from_engine_args(engine_args) File "/h2ogpt_conda/vllm_env/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 500, in from_engine_args engine = cls(parallel_config.worker_use_ray, File "/h2ogpt_conda/vllm_env/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 273, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/h2ogpt_conda/vllm_env/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 318, in _init_engine return engine_class(*args, **kwargs) File "/h2ogpt_conda/vllm_env/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 111, in __init__ self._init_workers() File "/h2ogpt_conda/vllm_env/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 146, in _init_workers self._run_workers("load_model") File "/h2ogpt_conda/vllm_env/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 795, in...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Add support for long-context beacon models: KeyError: 'model.beacon_embed_tokens.weight' new-model;stale https://github.com/FlagOpen/FlagEmbedding/tree/master/Long_LLM/activation_beacon https://huggingface.co/namespace-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: xt beacon models: KeyError: 'model.beacon_embed_tokens.weight' new-model;stale https://github.com/FlagOpen/FlagEmbedding/tree/master/Long_LLM/activation_beacon https://huggingface.co/namespace-Pt/activation-beacon-llama...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
