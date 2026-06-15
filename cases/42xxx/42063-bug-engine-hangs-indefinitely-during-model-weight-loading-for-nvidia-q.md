# vllm-project/vllm#42063: [Bug]: Engine hangs indefinitely during model weight loading for nvidia/Qwen3.5-397B-A17B-NVFP4 on Blackwell GPUs (RTX PRO 6000) with TP=4

| 字段 | 值 |
| --- | --- |
| Issue | [#42063](https://github.com/vllm-project/vllm/issues/42063) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;operator;quantization;triton |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine hangs indefinitely during model weight loading for nvidia/Qwen3.5-397B-A17B-NVFP4 on Blackwell GPUs (RTX PRO 6000) with TP=4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM v0.20.1 hangs indefinitely during model weight loading when serving `nvidia/Qwen3.5-397B-A17B-NVFP4` on 4x NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs (compute capability 12.0, 95 GB each) with `--tensor-parallel-size 4`. The engine starts correctly: NCCL initializes, all 4 workers connect via P2P/CUMEM, memory is allocated (75.98 GB per GPU), and weight loading begins across 11 safetensor shards. However, the process **hangs indefinetly** after enumerating the safetensor files -- no progress, no error, no OOM. The APIServer loops forever logging `Waiting for 1 local, 0 remote core engine proc(s) to start`. The model files are fully downloaded and cached on the PVC. There is no OOM or CUDA error. ### Reproducer Launch vLLM with the following command (using Docker or Kubernetes): ```bash vllm serve nvidia/Qwen3.5-397B-A17B-NVFP4 \ --trust-remote-code \ --tensor-parallel-size 4 \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.8 \ --served-model-name Qwen/Qwen3.5-397B-A17B \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --reasoning-parser qwen3 ``` With env vars: ``` NCCL_P2P_LEVEL=PHB OMP_NUM_THREADS=1...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Engine hangs indefinitely during model weight loading for nvidia/Qwen3.5-397B-A17B-NVFP4 on Blackwell GPUs (RTX PRO 6000) with TP=4 bug ### Your current environment ### 🐛 Describe the bug vLLM v0.20.1 hangs indef...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: DA error. ### Reproducer Launch vLLM with the following command (using Docker or Kubernetes): ```bash vllm serve nvidia/Qwen3.5-397B-A17B-NVFP4 \ --trust-remote-code \ --tensor-parallel-size 4 \ --kv-cache-dtype fp8 \ -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: gs indefinitely during model weight loading for nvidia/Qwen3.5-397B-A17B-NVFP4 on Blackwell GPUs (RTX PRO 6000) with TP=4 bug ### Your current environment ### 🐛 Describe the bug vLLM v0.20.1 hangs indefinitely during mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: nitely during model weight loading for nvidia/Qwen3.5-397B-A17B-NVFP4 on Blackwell GPUs (RTX PRO 6000) with TP=4 bug ### Your current environment ### 🐛 Describe the bug vLLM v0.20.1 hangs indefinitely during model weigh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: .. (Worker_TP0 pid=46) INFO 05-08 11:11:02 [platforms/cuda.py:423] Using backend AttentionBackendEnum.FLASH_ATTN for vit attention (Worker_TP0 pid=46) INFO 05-08 11:11:02 [model_executor/.../mamba/gdn_linear_attn.py:153...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
