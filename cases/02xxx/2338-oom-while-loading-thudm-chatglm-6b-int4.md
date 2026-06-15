# vllm-project/vllm#2338: OOM while loading THUDM/chatglm-6b-int4

| 字段 | 值 |
| --- | --- |
| Issue | [#2338](https://github.com/vllm-project/vllm/issues/2338) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;gemm_linear;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> OOM while loading THUDM/chatglm-6b-int4

### Issue 正文摘录

I am trying this code to load THUDM/chatglm-6b-int4 on a single GPU: `llm = LLM(model=model_path, trust_remote_code=True)` However it raises an OOM exception: > Traceback (most recent call last): File "demo_vllm.py", line 15, in llm = LLM(model="chatglm-6b-int4", File "miniconda3/envs/vllm/lib/python3.9/site-packages/vllm/entrypoints/llm.py", line 105, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "miniconda3/envs/vllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 250, in from_engine_args engine = cls(*engine_configs, File "miniconda3/envs/vllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 110, in __init__ self._init_workers(distributed_init_method) File "miniconda3/envs/vllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 146, in _init_workers self._run_workers( File "miniconda3/envs/vllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 755, in _run_workers self._run_workers_in_batch(workers, method, *args, **kwargs)) File "miniconda3/envs/vllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 729, in _run_workers_in_batch output = executor(*args, **kwargs) File "miniconda3/envs/vllm/li...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: OOM while loading THUDM/chatglm-6b-int4 I am trying this code to load THUDM/chatglm-6b-int4 on a single GPU: `llm = LLM(model=model_path, trust_remote_code=True)` However it raises an OOM exception: > Traceback (most re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ying this code to load THUDM/chatglm-6b-int4 on a single GPU: `llm = LLM(model=model_path, trust_remote_code=True)` However it raises an OOM exception: > Traceback (most recent call last): File "demo_vllm.py", line 15,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: port;quantization;scheduler_memory cuda;quantization crash;oom dtype;env_dependency I am trying this code to load THUDM/chatglm-6b-int4 on a single GPU:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: line 77, in __torch_function__ return func(*args, **kwargs) > torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 214.00 MiB. GPU 0 has a total capacty of 10.75 GiB of which 134.50 MiB is free. Including...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: OOM while loading THUDM/chatglm-6b-int4 I am trying this code to load THUDM/chatglm-6b-int4 on a single GPU: `llm = LLM(model=model_path, trust_remote_code=True)` However it raises an OOM exception: > Traceback (most r

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
