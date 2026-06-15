# vllm-project/vllm#12778: [Bug]: CPU build crashes with float16 or float32, only bfloat16 works, which leads to very poor performance. This is due to intel_extension_for_pytorch. How to build vllm without it?

| 字段 | 值 |
| --- | --- |
| Issue | [#12778](https://github.com/vllm-project/vllm/issues/12778) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPU build crashes with float16 or float32, only bfloat16 works, which leads to very poor performance. This is due to intel_extension_for_pytorch. How to build vllm without it?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The current build vllm==0.7.2.dev36+g18016a5e.cpu crashes float16 because of intel_extension_for_pytorch. Please provide a way to a way to build the vllm CPU without IPEX. When you start ```vllm serve ~/projects/webui/text-generation-webui/models/gpqt/``` your application will crash. I tracked it down to ipex. How do I build vllm with intel_extension_for_pytorch (ipex)? ``` ERROR 02-05 14:12:03 engine.py:389] ImportError: Please install intel_extension_for_pytorch>=2.5.0 via `pip install intel_extension_for_pytorch>=2.5.0` to use IPEX-AWQ linear method. Process SpawnProcess-1: Traceback (most recent call last): File "/home/rohezal/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm-0.7.2.dev36+g18016a5e.cpu-py3.12-linux-x86_64.egg/vllm/model_executor/layers/quantization/ipex_quant.py", line 134, in process_weights_after_loading import intel_extension_for_pytorch as ipex ModuleNotFoundError: No module named 'intel_extension_for_pytorch' ``` When installing IPEX, I get the following problems: ``` vllm serve ~/projects/webui/text-generation-webui/models/gpqt/ No ROCm runtime is found, using ROCM_HOME='/opt/rocm' INFO 02-05 14:15:3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: CPU build crashes with float16 or float32, only bfloat16 works, which leads to very poor performance. This is due to intel_extension_for_pytorch. How to build vllm without it? bug;stale ### Your current environme...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: CPU build crashes with float16 or float32, only bfloat16 works, which leads to very poor performance. This is due to intel_extension_for_pytorch. How to build vllm without it? bug;stale ### Your current environme...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: is due to intel_extension_for_pytorch. How to build vllm without it? bug;stale ### Your current environment ### 🐛 Describe the bug The current build vllm==0.7.2.dev36+g18016a5e.cpu crashes float16 because of intel_exten...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: X. When you start ```vllm serve ~/projects/webui/text-generation-webui/models/gpqt/``` your application will crash. I tracked it down to ipex. How do I build vllm with intel_extension_for_pytorch (ipex)? ``` ERROR 02-05...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
