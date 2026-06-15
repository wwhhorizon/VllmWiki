# vllm-project/vllm#13143: [Usage]: Qwen2-VL keyword argument `max_pixels` is not a valid argument for this processor and will be ignored.

| 字段 | 值 |
| --- | --- |
| Issue | [#13143](https://github.com/vllm-project/vllm/issues/13143) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;gemm;operator |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Qwen2-VL keyword argument `max_pixels` is not a valid argument for this processor and will be ignored.

### Issue 正文摘录

### Your current environment `branch:qwen25vl` ### How would you like to use vllm ``` VLLM_ARGS="--limit-mm-per-prompt image=2 \ --tensor-parallel-size 1 \ --max-model-len 16384 --served-model-name Qwen2.5-VL-7B-Instruct/ \ --mm_processor_kwargs {\"max_pixels\":1000000} \ --gpu_memory_utilization 0.9 \ --model Qwen/Qwen2.5-VL-7B-Instruct/" CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.openai.api_server ${VLLM_ARGS} --port 8000 ``` ### bash run in the preceding way, the configured max_pixels is invalid in the following log ``` INFO 02-12 03:01:35 cuda.py:230] Using Flash Attention backend. [W212 03:01:36.265895118 CUDAAllocatorConfig.h:28] Warning: expandable_segments not supported on this platform (function operator()) INFO 02-12 03:01:36 model_runner.py:1110] Starting to load model Qwen/Qwen2.5-VL-7B-autoglm-android-wechat-test-250211/... INFO 02-12 03:01:36 config.py:2930] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 1...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Qwen2-VL keyword argument `max_pixels` is not a valid argument for this processor and will be ignored. usage ### Your current environment `branch:qwen25vl` ### How would you like to use vllm ``` VLLM_ARGS="--li...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: y:1110] Starting to load model Qwen/Qwen2.5-VL-7B-autoglm-android-wechat-test-250211/... INFO 02-12 03:01:36 config.py:2930] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: nvalid in the following log ``` INFO 02-12 03:01:35 cuda.py:230] Using Flash Attention backend. [W212 03:01:36.265895118 CUDAAllocatorConfig.h:28] Warning: expandable_segments not supported on this platform (function op...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t-test-250211/... INFO 02-12 03:01:36 config.py:2930] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: } \ --gpu_memory_utilization 0.9 \ --model Qwen/Qwen2.5-VL-7B-Instruct/" CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.openai.api_server ${VLLM_ARGS} --port 8000 ``` ### bash run in the preceding way, the configure...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
