# vllm-project/vllm#13150: [Bug]: vllm serve: error: the following arguments are required: model_tag

| 字段 | 值 |
| --- | --- |
| Issue | [#13150](https://github.com/vllm-project/vllm/issues/13150) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve: error: the following arguments are required: model_tag

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve --model /home/models/PointerHQ/Qwen2.5-VL-72B-Instruct-Pointer-AWQ --quantization awq --tensor-parallel-size 8 --gpu-memory-utilization 0.99 --max-model-len 32768 --max-num-batched-tokens 32768 --max-num-seqs 20 --swap-space 8 --num-scheduler-steps 6 ` [BUG] `/home/anaconda3/envs/xinference/lib/python3.11/site-packages/transformers/utils/hub.py:128: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and will be removed in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( INFO 02-12 18:34:14 __init__.py:190] Automatically detected platform cuda. usage: vllm serve [options] vllm serve: error: the following arguments are required: model_tag` `CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve unsloth/Qwen2.5-VL-72B-Instruct-unsloth-bnb-4bit --served-model-name Qwen2.5-VL-72B-Instruct-unsloth-bnb-4bit --quantization bitsandbytes --tensor-parallel-size 8 --gpu-memory-utilization 0.99 --max-model-len 32768 --max-num-batched-tokens 32768 --max-num-seqs 20 --swap-space 8 --num-scheduler-steps 6 ` [BUG] `/home/anaconda3/envs/xinference/lib/python3.11/site-packages/transformers/uti...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: : vllm serve: error: the following arguments are required: model_tag bug;stale ### Your current environment ### 🐛 Describe the bug `CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve --model /home/models/PointerHQ/Qwen2.5-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vllm serve: error: the following arguments are required: model_tag bug;stale ### Your current environment ### 🐛 Describe the bug `CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve --model /home/models/PointerHQ/Qwe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ed platform cuda. INFO 02-12 18:37:29 api_server.py:840] vLLM API server version 0.7.2 INFO 02-12 18:37:29 api_server.py:841] args: Namespace(subparser='serve', model_tag='unsloth/Qwen2.5-VL-72B-Instruct-unsloth-bnb-4bi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: type='auto', kv_cache_dtype='auto', max_model_len=32768, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rve --model /home/models/PointerHQ/Qwen2.5-VL-72B-Instruct-Pointer-AWQ --quantization awq --tensor-parallel-size 8 --gpu-memory-utilization 0.99 --max-model-len 32768 --max-num-batched-tokens 32768 --max-num-seqs 20 --s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
