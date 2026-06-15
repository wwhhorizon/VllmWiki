# vllm-project/vllm#16655: [Usage]: RuntimeError: ('Worker failed with error %s, please check the stack trace above for the root cause'

| 字段 | 值 |
| --- | --- |
| Issue | [#16655](https://github.com/vllm-project/vllm/issues/16655) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;gemm_linear;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: RuntimeError: ('Worker failed with error %s, please check the stack trace above for the root cause'

### Issue 正文摘录

### Your current environment ``` ERROR 04-15 17:47:45 [core.py:387] EngineCore hit an exception: Traceback (most recent call last): ERROR 04-15 17:47:45 [core.py:387] File "/opt/miniconda3/envs/vLLM-3.12/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 378, in run_engine_core ERROR 04-15 17:47:45 [core.py:387] engine_core = EngineCoreProc(*args, **kwargs) ERROR 04-15 17:47:45 [core.py:387] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-15 17:47:45 [core.py:387] File "/opt/miniconda3/envs/vLLM-3.12/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 320, in __init__ ERROR 04-15 17:47:45 [core.py:387] super().__init__(vllm_config, executor_class, log_stats) ERROR 04-15 17:47:45 [core.py:387] File "/opt/miniconda3/envs/vLLM-3.12/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 71, in __init__ ERROR 04-15 17:47:45 [core.py:387] self._initialize_kv_caches(vllm_config) ERROR 04-15 17:47:45 [core.py:387] File "/opt/miniconda3/envs/vLLM-3.12/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 133, in _initialize_kv_caches ERROR 04-15 17:47:45 [core.py:387] available_gpu_memory = self.model_executor.determine_available_memory() ERROR 04-15 17:47:45 [core.py:387]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nYou can suppress this exception and fall back to eager by setting:\n import torch._dynamo\n torch._dynamo.config.suppress_errors = True\n') ERROR 04-15 17:47:45 [core.py:387] CRITICAL 04-15 17:47:45 [core_client.py:359...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: in __init__ ERROR 04-15 17:47:45 [core.py:387] super().__init__(vllm_config, executor_class, log_stats) ERROR 04-15 17:47:45 [core.py:387] File "/opt/miniconda3/envs/vLLM-3.12/lib/python3.12/site-packages/vllm/v1/engine...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ing down. See stack trace above for root cause issue. ``` Python 3.12 + CUDA 12.6 + 560.35.05 ``` (vLLM-3.12) root@vllm-h3c-ubuntu:/data# pip show flashinfer-python Name: flashinfer-python Version: 0.2.5 ``` ``` (vLLM-3...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: A 12.6 + 560.35.05 ``` (vLLM-3.12) root@vllm-h3c-ubuntu:/data# pip show flashinfer-python Name: flashinfer-python Version: 0.2.5 ``` ``` (vLLM-3.12) root@vllm-h3c-ubuntu:/data# pip show vllm Name: vllm Version: 0.8.4 ``...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: utor/layers/linear.py", line 474, in forward\n output_parallel = self.quant_method.apply(self, input_, bias)\n File "/opt/miniconda3/envs/vLLM-3.12/lib/python3.12/site-packages/vllm/model_executor/layers/linear.py", lin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
