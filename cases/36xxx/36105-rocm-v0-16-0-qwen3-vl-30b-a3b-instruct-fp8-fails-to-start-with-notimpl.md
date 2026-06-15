# vllm-project/vllm#36105: [ROCm][v0.16.0] Qwen3-VL-30B-A3B-Instruct-FP8 fails to start with NotImplementedError: No FP8 MoE backend supports the deployment configuration

| 字段 | 值 |
| --- | --- |
| Issue | [#36105](https://github.com/vllm-project/vllm/issues/36105) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;fp8;gemm;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [ROCm][v0.16.0] Qwen3-VL-30B-A3B-Instruct-FP8 fails to start with NotImplementedError: No FP8 MoE backend supports the deployment configuration

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Minimal reproducible example ```bash docker run -it --rm \ --network=host \ --group-add=video \ --ipc=host \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --device /dev/kfd \ --device /dev/dri \ -v /root/data/models/Qwen3-VL-30B-A3B-Instruct-FP8:/models/Qwen3-VL-30B-A3B-Instruct-FP8 \ docker.1ms.run/vllm/vllm-openai-rocm:latest \ /models/Qwen3-VL-30B-A3B-Instruct-FP8 \ --served-model-name Qwen3-VL-30B-A3B-Instruct-FP8 \ --port 9100 \ --gpu-memory-utilization 0.75 \ --tensor-parallel-size 1 \ --limit-mm-per-prompt.video 0 \ --async-scheduling ``` ## Observed result Server exits with engine-core init failure. ```text (EngineCore_DP0 pid=132) INFO 03-05 06:17:00 [parallel_state.py:1234] world_size=1 rank=0 local_rank=0 distributed_init_method=tcp://10.0.11.212:35189 backend=nccl [W305 06:17:10.319947724 socket.cpp:209] [c10d] The hostname of the client socket cannot be retrieved. err=-3 (EngineCore_DP0 pid=132) INFO 03-05 06:17:10 [parallel_state.py:1445] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 0, EP rank 0 (EngineCore_DP0 pid=132) INFO 03-05 06:17:13 [gpu_model_runner.py:4124]...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [ROCm][v0.16.0] Qwen3-VL-30B-A3B-Instruct-FP8 fails to start with NotImplementedError: No FP8 MoE backend supports the deployment configuration bug;rocm ### Your current environment ### 🐛 Describe the bug ## Minimal rep...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: # Your current environment ### 🐛 Describe the bug ## Minimal reproducible example ```bash docker run -it --rm \ --network=host \ --group-add=video \ --ipc=host \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [ROCm][v0.16.0] Qwen3-VL-30B-A3B-Instruct-FP8 fails to start with NotImplementedError: No FP8 MoE backend supports the deployment configuration bug;rocm ### Your current environment ### 🐛 Describe the bug ## Minimal rep...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 30B-A3B-Instruct-FP8 fails to start with NotImplementedError: No FP8 MoE backend supports the deployment configuration bug;rocm ### Your current environment ### 🐛 Describe the bug ## Minimal reproducible example ```bash...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [ROCm][v0.16.0] Qwen3-VL-30B-A3B-Instruct-FP8 fails to start with NotImplementedError: No FP8 MoE backend supports the deployment configuration bug;rocm ### Your current environment ### 🐛 Describe the bug ## Minimal

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
