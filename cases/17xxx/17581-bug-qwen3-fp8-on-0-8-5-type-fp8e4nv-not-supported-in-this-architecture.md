# vllm-project/vllm#17581: [Bug]: Qwen3 FP8 on 0.8.5: type fp8e4nv not supported in this architecture.

| 字段 | 值 |
| --- | --- |
| Issue | [#17581](https://github.com/vllm-project/vllm/issues/17581) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 FP8 on 0.8.5: type fp8e4nv not supported in this architecture.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I use FP8 quant of Qwen 3 30BA3 on 0.8.5 via: ```bash CUDA_VISIBLE_DEVICES=0,1 CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_LAUNCH_BLOCKING=1 vllm serve Qwen_Qwen3-30B-A3B-FP8/ --dtype auto --api-key token-abc123 --host 0.0.0.0 --port 8000 --tensor-parallel-size 2 --gpu-memory-utilization 0.95 --max-model-len 30000 --cpu-offload-gb 0 --device cuda --disable-custom-all-reduce --enable-reasoning --reasoning-parser deepseek_r1 --served-model-name AlexBefest/Qwen_QwQ-32B-AWQ --block-size 32 --max-seq-len-to-capture 30000 ``` I am facing the following problem: ```bash (base) root@306ae3f19619:/workdir# CUDA_VISIBLE_DEVICES=0,1 CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_LAUNCH_BLOCKING=1 vllm serve Qwen_Qwen3-30B-A3B-FP8/ --dtype auto --api-key token-abc123 --host 0.0.0.0 --port 8000 --tensor-parallel-size 2 --gpu-memory-utilization 0.95 --max-model-len 30000 --cpu-offload-gb 0 --device cuda --disable-custom-all-reduce --enable-reasoning --reasoning-parser deepseek_r1 --served-model-name AlexBefest/Qwen_QwQ-32B-AWQ --block-size 32 --max-seq-len-to-capture 30000 INFO 05-02 10:21:12 [__init__.py:239] Automatically detected platform cuda. INFO 05-02 10:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: 30BA3 on 0.8.5 via: ```bash CUDA_VISIBLE_DEVICES=0,1 CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_LAUNCH_BLOCKING=1 vllm serve Qwen_Qwen3-30B-A3B-FP8/ --dtype auto --api-key token-abc123 --host 0.0.0.0 --port 8000 --tensor-paralle...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Qwen3 FP8 on 0.8.5: type fp8e4nv not supported in this architecture. bug;stale ### Your current environment ### 🐛 Describe the bug When I use FP8 quant of Qwen 3 30BA3 on 0.8.5 via: ```bash CUDA_VISIBLE_DEVICES=0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: Qwen3 FP8 on 0.8.5: type fp8e4nv not supported in this architecture. bug;stale ### Your current environment ### 🐛 Describe the bug When I use FP8 quant of Qwen 3 30BA3 on 0.8.5 via: ```bash CUDA_VISIBLE_DEVICES=0,1 CUDA...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: rue, config_format= , dtype='auto', max_model_len=30000, guided_decoding_backend='auto', reasoning_parser='deepseek_r1', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_para...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: ``bash CUDA_VISIBLE_DEVICES=0,1 CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_LAUNCH_BLOCKING=1 vllm serve Qwen_Qwen3-30B-A3B-FP8/ --dtype auto --api-key token-abc123 --host 0.0.0.0 --port 8000 --tensor-parallel-size 2 --gpu-memory...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
