# vllm-project/vllm#3028: `--kv-cache-dtype fp8_e5m2` requires official docker image to have `nvcc`

| 字段 | 值 |
| --- | --- |
| Issue | [#3028](https://github.com/vllm-project/vllm/issues/3028) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> `--kv-cache-dtype fp8_e5m2` requires official docker image to have `nvcc`

### Issue 正文摘录

```bash CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.api_server \ --model=my_model --tensor-parallel-size 1 \ --dtype float16 \ --kv-cache-dtype fp8_e5m2 \ --swap-space 32 \ --gpu-memory-utilization 0.95 ``` yields ``` INFO 02-25 05:44:42 utils.py:188] CUDA_HOME is not found in the environment. Using /usr/local/cuda as CUDA_HOME. Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/api_server.py", line 90, in engine = AsyncLLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 617, in from_engine_args engine_configs = engine_args.create_engine_configs() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/arg_utils.py", line 279, in create_engine_configs cache_config = CacheConfig(self.block_size, File "/usr/local/lib/python3.10/dist-packages/vllm/config.py", line 296, in __init__ self._verify_cache_dtype() File "/usr/local/lib/python3.10/dist-packages/vllm/config....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: `--kv-cache-dtype fp8_e5m2` requires official docker image to have `nvcc` ```bash CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.api_server \ --model=my_model --tensor-parallel-size 1 \
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: `--kv-cache-dtype fp8_e5m2` requires official docker image to have `nvcc` ```bash CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.api_server \ --model=my_model --tenso
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ython3 -m vllm.entrypoints.api_server \ --model=my_model --tensor-parallel-size 1 \ --dtype float16 \ --kv-cache-dtype fp8_e5m2 \ --swap-s
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: he-dtype fp8_e5m2` requires official docker image to have `nvcc` ```bash CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.api_server \ --model=my_model --tensor-parallel-size 1 \ --dtype float16 \
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: `--kv-cache-dtype fp8_e5m2` requires official docker image to have `nvcc` ```bash CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.api_server \ --model=my_model

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
