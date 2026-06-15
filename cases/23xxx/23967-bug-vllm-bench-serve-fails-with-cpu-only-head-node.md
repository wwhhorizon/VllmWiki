# vllm-project/vllm#23967: [Bug]: vllm bench serve fails with CPU-only head node

| 字段 | 值 |
| --- | --- |
| Issue | [#23967](https://github.com/vllm-project/vllm/issues/23967) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm bench serve fails with CPU-only head node

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running `vllm bench serve` will fail with a CPU-only head node. On the contrary, running the benchmarking script `python benchmarking_serve.py` will succeed on that same node. My ray cluster is just a CPU head node and a GPU worker node that serves my LLM Error log with `VLLM_LOGGING_LEVEL=DEBUG` : ```log (base) ray@ip-10-0-3-237:~/default/benchmark_serve$ ./minimal_error.sh DEBUG 08-29 14:35:22 [__init__.py:30] No plugins for group vllm.platform_plugins found. DEBUG 08-29 14:35:22 [__init__.py:35] Checking if TPU platform is available. DEBUG 08-29 14:35:22 [__init__.py:45] TPU platform is not available because: No module named 'libtpu' DEBUG 08-29 14:35:22 [__init__.py:52] Checking if CUDA platform is available. DEBUG 08-29 14:35:22 [__init__.py:76] Exception happens when checking CUDA platform: NVML Shared Library Not Found DEBUG 08-29 14:35:22 [__init__.py:93] CUDA platform is not available because: NVML Shared Library Not Found DEBUG 08-29 14:35:22 [__init__.py:100] Checking if ROCm platform is available. DEBUG 08-29 14:35:22 [__init__.py:114] ROCm platform is not available because: No module named 'amdsmi' DEBUG 08-29 14:35:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 14:35:22 [__init__.py:239] No platform detected, vLLM is running on UnspecifiedPlatform WARNING 08-29 14:35:24 [_custom_ops.py:20] Failed to import from vllm._C with ImportError('libcuda.so.1: cannot open shared object...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: module named 'libtpu' DEBUG 08-29 14:35:22 [__init__.py:52] Checking if CUDA platform is available. DEBUG 08-29 14:35:22 [__init__.py:76] Exception happens when checking CUDA platform: NVML Shared Library Not Found DEBU...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: t `VLLM_PLUGINS` to control which plugins to load. DEBUG 08-29 14:35:26 [config.py:2212] Disabled the custom all-reduce kernel because it is not supported on current platform. Traceback (most recent call last): File "/h...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: M_LOGGING_LEVEL=DEBUG vllm bench serve \ --model Qwen/Qwen2.5-7B \ --backend openai-chat \ --base-url "$BASE_URL" \ --endpoint /v1/chat/completions \ --dataset-name random ``` If you git clone vllm then replace the comm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: serve` will fail with a CPU-only head node. On the contrary, running the benchmarking script `python benchmarking_serve.py` will succeed on that same node. My ray cluster is just a CPU head node and a GPU worker node th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
