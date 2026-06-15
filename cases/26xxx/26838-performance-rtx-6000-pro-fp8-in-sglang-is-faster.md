# vllm-project/vllm#26838: [Performance]: RTX 6000 PRO - FP8 in sglang is faster

| 字段 | 值 |
| --- | --- |
| Issue | [#26838](https://github.com/vllm-project/vllm/issues/26838) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;gemm_linear;model_support;multimodal_vlm;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;fp8;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: RTX 6000 PRO - FP8 in sglang is faster

### Issue 正文摘录

### Proposal to improve performance Can we have a discussion about the sglang FP8 performance vs VLLM performance - I'm able to get 133 tokens/sec with sglang GLM-4.5-Air-FP8 vs 78 tokens/sec in VLLM ```PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True USE_TRITON_W8A8_FP8_KERNEL=1 SGL_ENABLE_JIT_DEEPGEMM=0 python -m sglang.launch_server --model /mnt/GLM-4.5-FP8/ --tp 4 --host 0.0.0.0 --port 5000 --mem-fraction-static 0.93 --context-length 128000 --enable-metrics --attention-backend flashinfer --tool-call-parser glm45 --reasoning-parser glm45 --served-model-name glm-4.5-air --chunked-prefill-size 8092 --enable-mixed-chunk --cuda-graph-max-bs 32 --kv-cache-dtype fp8_e5m2``` It is using TRITON I'm not able to achieve the same speed with VLLM with any methods - neither flashinfer, nor triton etc. - the maximum is always around 78 tokens/sec 1) Any idea how to achieve the same 133tokens/sec in VLLM using triton and same configuration like in sglang? 2) is it cutlass design that it is not that fast as triton? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) _No response_ ### Bef...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ns/sec in VLLM ```PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True USE_TRITON_W8A8_FP8_KERNEL=1 SGL_ENABLE_JIT_DEEPGEMM=0 python -m sglang.launch_server --model /mnt/GLM-4.5-FP8/ --tp 4 --host 0.0.0.0 --port 5000 --mem-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _FP8_KERNEL=1 SGL_ENABLE_JIT_DEEPGEMM=0 python -m sglang.launch_server --model /mnt/GLM-4.5-FP8/ --tp 4 --host 0.0.0.0 --port 5000 --mem-fraction-static 0.93 --context-length 128000 --enable-metrics --attention-backend...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Performance]: RTX 6000 PRO - FP8 in sglang is faster performance;stale ### Proposal to improve performance Can we have a discussion about the sglang FP8 performance vs VLLM performance - I'm able to get 133 tokens/sec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Performance]: RTX 6000 PRO - FP8 in sglang is faster performance;stale ### Proposal to improve performance Can we have a discussion about the sglang FP8 performance vs VLLM performance - I'm able to get 133 tokens/sec...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: RTX 6000 PRO - FP8 in sglang is faster performance;stale ### Proposal to improve performance Can we have a discussion about the sglang FP8 performance vs VLLM performance - I'm able to get 133 tokens/sec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
