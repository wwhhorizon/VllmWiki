# vllm-project/vllm#24156: [Bug]: Crash when running embedding model on CPU (kv_cache_spec_values empty)

| 字段 | 值 |
| --- | --- |
| Issue | [#24156](https://github.com/vllm-project/vllm/issues/24156) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash when running embedding model on CPU (kv_cache_spec_values empty)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running an embedding (pooling) model with CPU backend (V1 only), vLLM crashes with an IndexError inside is_kv_cache_type_uniform. It seems that in embedding mode, kv_cache_spec_values is empty, but the function still tries to access [0]. Since embedding/pooling tasks do not require KV cache, this check should be skipped. ### Error Log ``` (EngineCore_0 pid=24341) File ".../vllm/v1/core/kv_cache_utils.py", line 753, in is_kv_cache_type_uniform (EngineCore_0 pid=24341) _ = kv_cache_spec_values[0].merge(kv_cache_spec_values) (EngineCore_0 pid=24341) IndexError: list index out of range ``` ### Steps to Reproduce 1. Environment variables: ``` export VLLM_USE_V1=1 export VLLM_TARGET_DEVICE=cpu export VLLM_USE_CUDA=0 export PYTHONUNBUFFERED=1 ``` 2. Start API server: ``` python -m vllm.entrypoints.api_server \ --model intfloat/multilingual-e5-small \ --dtype float32 \ --tensor-parallel-size 1 \ --enforce-eager ``` 3. Or run embedding call: ``` from vllm import LLM def main(): model_name = "intfloat/multilingual-e5-small" llm = LLM( model=model_name, runner="pooling", # embedding runner enforce_eager=True, # required on CPU dtype="f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: size 1 \ --enforce-eager ``` 3. Or run embedding call: ``` from vllm import LLM def main(): model_name = "intfloat/multilingual-e5-small" llm = LLM( model=model_name, runner="pooling", # embedding runner enforce_eager=T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: : ``` export VLLM_USE_V1=1 export VLLM_TARGET_DEVICE=cpu export VLLM_USE_CUDA=0 export PYTHONUNBUFFERED=1 ``` 2. Start API server: ``` python -m vllm.entrypoints.api_server \ --model intfloat/multilingual-e5-small \ --d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: rypoints.api_server \ --model intfloat/multilingual-e5-small \ --dtype float32 \ --tensor-parallel-size 1 \ --enforce-eager ``` 3. Or run embedding call: ``` from vllm import LLM def main(): model_name = "intfloat/multi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: # 🐛 Describe the bug When running an embedding (pooling) model with CPU backend (V1 only), vLLM crashes with an IndexError inside is_kv_cache_type_uniform. It seems that in embedding mode, kv_cache_spec_values is empty,...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: neCore_0 pid=24341) IndexError: list index out of range ``` ### Steps to Reproduce 1. Environment variables: ``` export VLLM_USE_V1=1 export VLLM_TARGET_DEVICE=cpu export VLLM_USE_CUDA=0 export PYTHONUNBUFFERED=1 ``` 2....

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
