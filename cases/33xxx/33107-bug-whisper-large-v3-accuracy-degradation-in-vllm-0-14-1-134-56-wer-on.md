# vllm-project/vllm#33107: [Bug]: Whisper large-v3 accuracy degradation in vLLM 0.14.1 (134.56% WER) on L40S - works fine in 0.12.0

| 字段 | 值 |
| --- | --- |
| Issue | [#33107](https://github.com/vllm-project/vllm/issues/33107) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Whisper large-v3 accuracy degradation in vLLM 0.14.1 (134.56% WER) on L40S - works fine in 0.12.0

### Issue 正文摘录

### Your current environment Key details: - vLLM version: 0.14.1 - GPU: 2x NVIDIA L40S (48GB each, compute capability 8.9) - PyTorch: 2.9.0 - CUDA: 12.8.0 - OS: RHEL9 (Red Hat Enterprise Linux 9.6) - Model: openai/whisper-large-v3 - Precision: bfloat16 Describe the bug Whisper large-v3 has severe accuracy degradation in vLLM 0.14.1 compared to 0.12.0 on NVIDIA L40S GPUs. The model produces hallucinated, repetitive outputs resulting in 134% WER (Word Error Rate) What Works - vLLM 0.12.0: Achieves expected Word Error Rate: 1.8795740266661591%, accuracy=98.12042597333384% - Same hardware, same model, same dataset What seems to be broken - Model outputs repetitive hallucinated text regardless of audio input - All transcriptions are semantically unrelated to the actual audio Minimal Reproduction ``` (whisper-gpu-fresh) [root@sbhavsar-rhaiis ~] docker pull quay.io/sayali/mlperf-whisper:vllm-0.14.1 (whisper-gpu-fresh) [root@sbhavsar-rhaiis docker]# docker run -d \ --name mlperf-whisper-benchmark \ --gpus all \ --network host \ --ipc host \ --pid host \ --privileged \ --ulimit memlock=-1:-1 \ --ulimit stack=67108864:67108864 \ -e NVIDIA_VISIBLE_DEVICES=all \ -e USER=app-root \ -e LOGNAME=...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: 3. FA3 incompatible: L40S has compute capability 8.9, FA3 requires 9.0+ (H100/H200) 4. Related to #33091: FlashAtten
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: - vLLM version: 0.14.1 - GPU: 2x NVIDIA L40S (48GB each, co
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: radation in vLLM 0.14.1 (134.56% WER) on L40S - works fine in 0.12.0 bug;stale ### Your current environment Key details:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: - GPU: 2x NVIDIA L40S (48GB each, compute capability 8.9) - PyTorch: 2.9.0
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: Whisper large-v3 accuracy degradation in vLLM 0.14.1 (134.56% WER) on L40S - works fine in 0.12.0 bug;stale ### Your current environment Key details:

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
