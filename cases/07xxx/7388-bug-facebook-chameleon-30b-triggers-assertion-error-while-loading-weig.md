# vllm-project/vllm#7388: [Bug]: `facebook/chameleon-30b` triggers assertion error while loading weights

| 字段 | 值 |
| --- | --- |
| Issue | [#7388](https://github.com/vllm-project/vllm/issues/7388) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `facebook/chameleon-30b` triggers assertion error while loading weights

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running vLLM v0.5.4 with tensor parallelism degree 2. `facebook/chameleon-7b` works well (this one with TP 1), but `facebook/chameleon-30b` fails to load weights while reading in the first safetensors shard. The name of the parameter that triggers the assertion is `model.layers.3.self_attn.k_norm.bias`. ```python Traceback (most recent call last): File "/usr/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/rpc/server.py", line 217, in run_rpc_server server = AsyncEngineRPCServer(async_engine_args, usage_context, port) File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/rpc/server.py", line 25, in __init__ self.engine = AsyncLLMEngine.from_engine_args(async_engine_args, File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 484, in from_engine_args engine = cls( File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 394, in __init__ self.engine...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: heckpoint shards: 0% Completed | 0/15 [00:00<?, ?it/s] ``` correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;crash;nan_inf en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ent ### 🐛 Describe the bug Running vLLM v0.5.4 with tensor parallelism degree 2. `facebook/chameleon-7b` works well (this one with TP 1), but `facebook/chameleon-30b` fails to load weights while reading in the first saf...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tensors shard. The name of the parameter that triggers the assertion is `model.layers.3.self_attn.k_norm.bias`. ```python Traceback (most recent call last): File "/usr/lib/python3.10/multip
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pi;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
