# vllm-project/vllm#35048: [Bug]: perf degradation between vllm 0.14.0 to 0.15.1

| 字段 | 值 |
| --- | --- |
| Issue | [#35048](https://github.com/vllm-project/vllm/issues/35048) |
| 状态 | open |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | moe |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: perf degradation between vllm 0.14.0 to 0.15.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, I love the model! For both (minimax m2.1 and m2.5), there is a performance (throughput) degradation between vllm 0.14.0 and newer versions, which is visible under high load with large requests. Is that something that you are aware of? I see this on 4H100 and 8H100 I load the model like this (I got the best performance like this): ``` docker run -d --gpus all -p 0.0.0.0:8000:8000 -v ~/.cache/huggingface:/root/.cache/huggingface -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 -e VLLM_ATTENTION_BACKEND=FLASHINFER -e VLLM_FLASHINFER_MOE_BACKEND=throughput -e VLLM_USE_FLASHINFER_MOE_FP16=1 -e VLLM_USE_FLASHINFER_MOE_FP8=1 -e VLLM_USE_FLASHINFER_MOE_FP4=1 -e VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 -e SAFETENSORS_FAST_GPU=1 -e VLLM_SERVER_DEV_MODE=1 -e TORCH_ALLOW_TF32_CUBLAS_OVERRIDE=1 vllm/vllm-openai:v0.15.1 --model MiniMaxAI/MiniMax-M2.5 --port 8000 --max-model-len 128000 --max-num-seqs 64 --tool-call-parser minimax_m2 --reasoning-parser minimax_m2_append_think --enable-auto-tool-choice --tensor-parallel-size 4 --gpu-memory-utilization 0.9 --swap-space 16 --enable-expert-parallel --trust_remote_code ``` ___________________________________...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: is a performance (throughput) degradation between vllm 0.14.0 and newer versions, which is visible under high load with large requests. Is that something that you are aware of? I see this on 4H100 and 8H100 I load the m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ove the model! For both (minimax m2.1 and m2.5), there is a performance (throughput) degradation between vllm 0.14.0 and newer versions, which is visible under high load with large requests. Is that something that you a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: =throughput -e VLLM_USE_FLASHINFER_MOE_FP16=1 -e VLLM_USE_FLASHINFER_MOE_FP8=1 -e VLLM_USE_FLASHINFER_MOE_FP4=1 -e VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 -e SAFETENSORS_FAST_GPU=1 -e VLLM_SERVER_DEV_MODE=1 -e TORCH_ALLOW...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: large requests. Is that something that you are aware of? I see this on 4H100 and 8H100 I load the model like this (I got the best performance like this): ``` docker run -d --gpus all -p 0.0.0.0:8000:8000 -v ~/.cache/hug...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: he/huggingface -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 -e VLLM_ATTENTION_BACKEND=FLASHINFER -e VLLM_FLASHINFER_MOE_BACKEND=throughput -e VLLM_USE_FLASHINFER_MOE_FP16=1 -e VLLM_USE_FLASHINFER_MOE_FP8=1 -e VLLM_USE_FLASHI...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
