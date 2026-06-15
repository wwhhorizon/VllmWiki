# vllm-project/vllm#30206: [Bug]: DeepSeek-V3.2 DeepGEMM RuntimeError

| 字段 | 值 |
| --- | --- |
| Issue | [#30206](https://github.com/vllm-project/vllm/issues/30206) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;model_support;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;fp8;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V3.2 DeepGEMM RuntimeError

### Issue 正文摘录

### Your current environment - vLLM nightly (`879ddb09c3b7b5a21f75e46ded148ce70f1c486e`) - DeepGEMM (`v2.1.1.post3`) - CUDA (`12.9`) ### 🐛 Describe the bug EngineArgs (`vllm serve`): - tensor_parallel_size=8 - tool_call_parser=deepseek_v32 - enable_auto_tool_choice=True - tokenizer_mode=deepseek_v32 - reasoning_parser=deepseek_v3 - max_model_len=32768 logs: ``` [default_loader.py:308] Loading weights took 53.99 seconds [multiproc_executor.py:750] WorkerProc failed to start. [multiproc_executor.py:750] Traceback (most recent call last): [multiproc_executor.py:750] File "/.venv/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 722, in worker_main [multiproc_executor.py:750] worker = WorkerProc(*args, **kwargs) [multiproc_executor.py:750] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ [multiproc_executor.py:750] File "/.venv/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 562, in __init__ [multiproc_executor.py:750] self.worker.load_model() [multiproc_executor.py:750] File "/.venv/lib/python3.12/site-packages/vllm/v1/worker/gpu_worker.py", line 273, in load_model [multiproc_executor.py:750] self.model_runner.load_model(eep_scale_up=eep_scale_up) [mult...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: d_model [multiproc_executor.py:750] self.model_runner.load_model(eep_scale_up=eep_scale_up) [multiproc_executor.py:750] File "/.venv/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", line 3540, in load_m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 879ddb09c3b7b5a21f75e46ded148ce70f1c486e`) - DeepGEMM (`v2.1.1.post3`) - CUDA (`12.9`) ### 🐛 Describe the bug EngineArgs (`vllm serve`): - tensor_parallel_size=8 - tool_call_parser=deepseek_v32 - enable_auto_tool_choice...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: =True - tokenizer_mode=deepseek_v32 - reasoning_parser=deepseek_v3 - max_model_len=32768 logs: ``` [default_loader.py:308] Loading weights took 53.99 seconds [multiproc_executor.py:750] WorkerProc failed to start. [mult...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: or.py:750] File "/.venv/lib/python3.12/site-packages/vllm/v1/attention/backends/mla/common.py", line 1170, in process_weights_after_loading [multiproc_executor.py:750] kv_b_proj_weight = get_and_maybe_dequant_weights(se...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rt;quantization attention;cuda;fp8;operator;quantization crash dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
