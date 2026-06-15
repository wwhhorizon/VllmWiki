# vllm-project/vllm#4666: [Feature]: Support kv-cache-dtype fp8 without nvcc

| 字段 | 值 |
| --- | --- |
| Issue | [#4666](https://github.com/vllm-project/vllm/issues/4666) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;fp8 |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support kv-cache-dtype fp8 without nvcc

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently the following error is thrown if nvcc is not installed: ``` WARNING 05-08 01:34:59 utils.py:313] Not found nvcc in /usr/local/cuda. Skip cuda version check! Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 159, in engine = AsyncLLMEngine.from_engine_args( File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 341, in from_engine_args engine_config = engine_args.create_engine_config() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/arg_utils.py", line 471, in create_engine_config cache_config = CacheConfig(self.block_size, File "/usr/local/lib/python3.10/dist-packages/vllm/config.py", line 310, in __init__ self._verify_cache_dtype() File "/usr/local/lib/python3.10/dist-packages/vllm/config.py", line 333, in _verify_cache_dtype if nvcc_cuda_version < Version("11.8"): TypeError: '<' not supported between instances of 'NoneType'...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: vation and pitch Currently the following error is thrown if nvcc is not installed: ``` WARNING 05-08 01:34:59 utils.py:313] Not found nvcc in /usr/local/cuda. Skip cuda version check! Traceback (most recent call last):
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Support kv-cache-dtype fp8 without nvcc feature request;stale ### 🚀 The feature, motivation and pitch Currently the following error is thrown if nvcc is not installed: ``` WARNING 05-08 01:34:59 utils.py:313]...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support kv-cache-dtype fp8 without nvcc feature request;stale ### 🚀 The feature, motivation and pitch Currently the following error is thrown if nvcc is not installed: ``` WARNING 05-08 01:34:59 utils.py:313]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d: ``` WARNING 05-08 01:34:59 utils.py:313] Not found nvcc in /usr/local/cuda. Skip cuda version check! Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: Support kv-cache-dtype fp8 without nvcc feature request;stale ### 🚀 The feature, motivation and pitch Currently the following error is thrown if nvcc is not installed: ``` WARNING 05-08 01:34:59 utils.py:313]...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
