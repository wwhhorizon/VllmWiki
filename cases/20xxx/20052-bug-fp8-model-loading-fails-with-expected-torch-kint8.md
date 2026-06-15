# vllm-project/vllm#20052: [Bug] FP8 Model Loading Fails with "Expected torch::kInt8"

| 字段 | 值 |
| --- | --- |
| Issue | [#20052](https://github.com/vllm-project/vllm/issues/20052) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] FP8 Model Loading Fails with "Expected torch::kInt8"

### Issue 正文摘录

### Your current environment RTX 5090 vLLM API server version 0.9.2.dev209+g2dd24ebe1 ### 🐛 Describe the bug ``` docker run --gpus all --rm -it -p 8000:8000 \ -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ vllm:openai \ --model RedHatAI/Mistral-Nemo-Instruct-2407-FP8 \ --max-model-len 60000 \ --gpu-memory-utilization 0.85 INFO 06-24 20:25:11 [__init__.py:244] Automatically detected platform cuda. INFO 06-24 20:25:15 [api_server.py:1287] vLLM API server version 0.9.2.dev209+g2dd24ebe1 INFO 06-24 20:25:15 [cli_args.py:309] non-default args: {'model': 'RedHatAI/Mistral-Nemo-Instruct-2407-FP8', 'max_model_len': 60000, 'gpu_memory_utilization': 0.85} config.json: 100%|█████████████████████████████████████████████████████████████████████| 822/822 [00:00 INFO 06-24 20:25:38 [parallel_state.py:1072] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0 INFO 06-24 20:25:38 [topk_topp_sampler.py:49] Using FlashInfer for top-p & top-k sampling. INFO 06-24 20:25:38 [gpu_model_runner.py:1696] Starting to load model RedHatAI/Mistral-Nemo-Instruct-2407-FP8... INFO 06-24 20:25:38 [gpu_model_runner.py:1701] Loading model from scratch... INFO 06-24 20:25:39 [cuda.p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: :kInt8" bug;stale ### Your current environment RTX 5090 vLLM API server version 0.9.2.dev209+g2dd24ebe1 ### 🐛 Describe the bug ``` docker run --gpus all --rm -it -p 8000:8000 \ -e PYTORCH_CUDA_ALLOC_CONF=expandable_segm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: TP rank 0, EP rank 0 INFO 06-24 20:25:38 [topk_topp_sampler.py:49] Using FlashInfer for top-p & top-k sampling. INFO 06-24 20:25:38 [gpu_model_runner.py:1696] Starting to load model RedHatAI/Mistral-Nemo-Instruct-2407-F...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug] FP8 Model Loading Fails with "Expected torch::kInt8" bug;stale ### Your current environment RTX 5090 vLLM API server version 0.9.2.dev209+g2dd24ebe1 ### 🐛 Describe the bug ``` docker run --gpus all --rm -it -p 800...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug] FP8 Model Loading Fails with "Expected torch::kInt8" bug;stale ### Your current environment RTX 5090 vLLM API server version 0.9.2.dev209+g2dd24ebe1 ### 🐛 Describe the bug ``` docker run --gpus all --rm -it -p 800...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ils with "Expected torch::kInt8" bug;stale ### Your current environment RTX 5090 vLLM API server version 0.9.2.dev209+g2dd24ebe1 ### 🐛 Describe the bug ``` docker run --gpus all --rm -it -p 8000:8000 \ -e PYTORCH_CUDA_A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
