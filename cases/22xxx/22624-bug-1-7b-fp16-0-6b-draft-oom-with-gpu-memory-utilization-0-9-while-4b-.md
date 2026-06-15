# vllm-project/vllm#22624: [Bug]: 1.7B fp16 + 0.6B draft OOM with gpu_memory_utilization=0.9, while 4B int8 + 0.6B works fine on A800 80 GB

| 字段 | 值 |
| --- | --- |
| Issue | [#22624](https://github.com/vllm-project/vllm/issues/22624) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 1.7B fp16 + 0.6B draft OOM with gpu_memory_utilization=0.9, while 4B int8 + 0.6B works fine on A800 80 GB

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **1.7B fp16 + 0.6B draft OOM with gpu_memory_utilization=0.9, while 4B int8 + 0.6B works fine on A800 80 GB** **Observed behavior** When util=0.9, vLLM crashes during CUDA-graph capture: RuntimeError: CUDA error: out of memory ... torch/cuda/graphs.py:84 With util=0.8 or switching the target to 4B-int8, vLLM starts normally. **Expected behavior** On an 80 GB A800, 1.7B-fp16 + 0.6B-fp16 should be able to use util=0.9 without OOM, or at least behave not worse than the larger 4B-int8 + 0.6B combination. **Notes** Issue appears to be CUDA-graph memory fragmentation rather than absolute memory size. 4B-int8 model + 0.6B draft uses ~5 GB more parameters+activations, yet succeeds at util=0.9. 1.7B-fp16 model alone uses less memory, but combined with draft it requires lowering util to 0.8. **Request** Investigate why the smaller 1.7B-fp16 combination is more sensitive to gpu_memory_utilization than the larger 4B-int8 combination during speculative decoding CUDA-graph initialization. ``` CUDA_VISIBLE_DEVICES=0 vllm serve before_qwen_full_sam_1b7_250807_deploy \ --max-model-len 4096 \ --served-model-name qwen3 \ --host 0.0.0.0 \ --port 898...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: 1.7B fp16 + 0.6B draft OOM with gpu_memory_utilization=0.9, while 4B int8 + 0.6B works fine on A800 80 GB bug;stale ### Your current environment ### 🐛 Describe the bug **1.7B fp16 + 0.6B draft OOM with gpu_memory...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform cuda. INFO 08-11 15:37:37 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 08-11 15:37:37 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/root/paddlejob/workspace/env_run/xavier...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e, model_loader_extra_config={}, use_tqdm_on_load=True, config_format= , dtype='auto', max_model_len=4096, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distrib...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: UDA-graph memory fragmentation rather than absolute memory size. 4B-int8 model + 0.6B draft uses ~5 GB more parameters+activations, yet succeeds at util=0.9. 1.7B-fp16 model alone uses less memory, but combined with dra...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: True, config_format= , dtype='auto', max_model_len=4096, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
