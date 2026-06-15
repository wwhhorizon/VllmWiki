# vllm-project/vllm#39625: MiniMaxM2 + NVFP4: shape mismatch in partial rotary embedding kernel (TP=2)

| 字段 | 值 |
| --- | --- |
| Issue | [#39625](https://github.com/vllm-project/vllm/issues/39625) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | shape_align |
| Operator 关键词 | cache;cuda;fp8;kernel;quantization |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> MiniMaxM2 + NVFP4: shape mismatch in partial rotary embedding kernel (TP=2)

### Issue 正文摘录

## Environment - vLLM: 0.19.0 - GPU: 2x NVIDIA RTX PRO 6000 Blackwell (96GB each) - Model: `lukealonso/MiniMax-M2.7-NVFP4` (ModelOpt NVFP4 quantization) - OS: Ubuntu 24.04, Linux 6.17, CUDA 13.0 - Driver: 580.126.09 ## Problem MiniMaxM2ForCausalLM with NVFP4 quantization fails during first inference with a tensor shape mismatch. Model loading succeeds (62.75 GiB in 12.7s), KV cache allocation succeeds, but the forward pass crashes. ## Error ``` RuntimeError: Worker failed with error 'Invalid shape of out: expected torch.Size([8, 24, 80]), got torch.Size([8, 24, 128])' ``` ## Analysis MiniMax-M2.7 uses partial rotary embedding: - `head_dim: 128` - `rotary_dim: 64` - `partial_rotary_factor: 0.5` The NVFP4 kernel appears to expect a shape derived from `rotary_dim` (80 = some function of 64?) but receives the full `head_dim` (128). This suggests the NVFP4 quantization path doesn't correctly account for `partial_rotary_factor` in MiniMaxM2. **Note:** FP8 quantization of the same model works correctly with TP=4 on the same hardware. ## Launch command ```bash NCCL_P2P_DISABLE=1 NCCL_CUMEM_ENABLE=0 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ CUDA_VISIBLE_DEVICES=0,1 vllm serve luke...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: MiniMaxM2 + NVFP4: shape mismatch in partial rotary embedding kernel (TP=2) ## Environment - vLLM: 0.19.0 - GPU: 2x NVIDIA RTX PRO 6000 Blackwell (96GB each) - Model: `lukealonso/MiniMax-M2.7-NVFP4` (ModelOpt NVFP4 quan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: MiniMaxM2 + NVFP4: shape mismatch in partial rotary embedding kernel (TP=2) ## Environment - vLLM: 0.19.0 - GPU: 2x NVIDIA RTX PRO 6000 Blackwell (96GB each) - Model: `lukealonso/MiniMax-M2.7-NVFP4` (ModelOpt NVFP4 quan...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ent - vLLM: 0.19.0 - GPU: 2x NVIDIA RTX PRO 6000 Blackwell (96GB each) - Model: `lukealonso/MiniMax-M2.7-NVFP4` (ModelOpt NVFP4 quantization) - OS: Ubuntu 24.04, Linux 6.17, CUDA 13.0 - Driver: 580.126.09 ## Problem Min...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: MiniMaxM2 + NVFP4: shape mismatch in partial rotary embedding kernel (TP=2) ## Environment - vLLM: 0.19.0 - GPU: 2x NVIDIA RTX PRO 6000 Blackwell (96GB each) - Model: `lukealonso/MiniMax-M2.7-NVFP4` (ModelOpt NVFP4 quan...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: st match w3_weight_scale_2. Accuracy may be affected. (Worker_TP0) Using MoEPrepareAndFinalizeNoDPEPModular (Worker_TP0) Available KV cache memory: 19.78 GiB (EngineCore) GPU KV cache size: 267,600 tokens RuntimeError:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
