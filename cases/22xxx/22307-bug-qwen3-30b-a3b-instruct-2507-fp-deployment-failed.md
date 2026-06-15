# vllm-project/vllm#22307: [Bug]: Qwen3-30B-A3B-Instruct-2507-FP deployment failed

| 字段 | 值 |
| --- | --- |
| Issue | [#22307](https://github.com/vllm-project/vllm/issues/22307) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;fp8;operator |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-30B-A3B-Instruct-2507-FP deployment failed

### Issue 正文摘录

### Your current environment vllm==0.9.2 export CUDA_VISIBLE_DEVICES=1,2 vllm serve /mnt/general/models/Qwen3-30B-A3B-Instruct-2507-FP8 \ --served-model-name Qwen3-30B-A3B-Instruct-2507-FP8 \ --tensor-parallel-size 2 \ --pipeline-parallel-size 1 \ --gpu-memory-utilization 0.9 \ --port 8011 \ --trust-remote-code \ --max-model-len 64000 ### 🐛 Describe the bug (VllmWorker rank=1 pid=2061) INFO 08-06 03:26:00 [gpu_model_runner.py:1843] Starting to load model /mnt/general/models/Qwen3-30B-A3B-Instruct-2507-FP8... (VllmWorker rank=0 pid=2057) INFO 08-06 03:26:00 [gpu_model_runner.py:1843] Starting to load model /mnt/general/models/Qwen3-30B-A3B-Instruct-2507-FP8... (VllmWorker rank=1 pid=2061) INFO 08-06 03:26:00 [gpu_model_runner.py:1875] Loading model from scratch... (VllmWorker rank=1 pid=2061) INFO 08-06 03:26:00 [cuda.py:290] Using Flash Attention backend on V1 engine. (VllmWorker rank=1 pid=2061) WARNING 08-06 03:26:00 [fp8.py:535] CutlassBlockScaledGroupedGemm not supported on the current platform. (VllmWorker rank=0 pid=2057) INFO 08-06 03:26:00 [gpu_model_runner.py:1875] Loading model from scratch... (VllmWorker rank=0 pid=2057) INFO 08-06 03:26:00 [cuda.py:290] Using Flash Att...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ... (VllmWorker rank=1 pid=2061) INFO 08-06 03:26:00 [cuda.py:290] Using Flash Attention backend on V1 engine. (VllmWorker rank=1 pid=2061) WARNING 08-06 03:26:00 [fp8.py:535] CutlassBlockScaledGroupedGemm not supported...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: _DEVICES=1,2 vllm serve /mnt/general/models/Qwen3-30B-A3B-Instruct-2507-FP8 \ --served-model-name Qwen3-30B-A3B-Instruct-2507-FP8 \ --tensor-parallel-size 2 \ --pipeline-parallel-size 1 \ --gpu-memory-utilization 0.9 \...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-30B-A3B-Instruct-2507-FP deployment failed bug;stale ### Your current environment vllm==0.9.2 export CUDA_VISIBLE_DEVICES=1,2 vllm serve /mnt/general/models/Qwen3-30B-A3B-Instruct-2507-FP8 \ --served-model-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ment failed bug;stale ### Your current environment vllm==0.9.2 export CUDA_VISIBLE_DEVICES=1,2 vllm serve /mnt/general/models/Qwen3-30B-A3B-Instruct-2507-FP8 \ --served-model-name Qwen3-30B-A3B-Instruct-2507-FP8 \ --ten...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: 1 pid=2061) WARNING 08-06 03:26:00 [fp8.py:535] CutlassBlockScaledGroupedGemm not supported on the current platform. (VllmWorker rank=0 pid=2057) INFO 08-06 03:26:00 [gpu_model_runner.py:1875] Loading model from scratch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
