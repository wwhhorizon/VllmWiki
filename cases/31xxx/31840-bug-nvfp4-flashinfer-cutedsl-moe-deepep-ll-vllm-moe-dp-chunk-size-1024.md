# vllm-project/vllm#31840: [Bug]: NVFP4 Flashinfer CuteDSL MoE + DeepEP ll + VLLM_MOE_DP_CHUNK_SIZE=1024 + cudagraph numerical accuracy issue on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#31840](https://github.com/vllm-project/vllm/issues/31840) |
| 状态 | open |
| 标签 | bug;unstale;nvidia |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;moe |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NVFP4 Flashinfer CuteDSL MoE + DeepEP ll + VLLM_MOE_DP_CHUNK_SIZE=1024 + cudagraph numerical accuracy issue on B200

### Issue 正文摘录

### Your current environment There seems to be a numerical accuracy issue with nvfp4 flashinfer cutedsl moe + deepep low latency with certain DP CHUNK sizes. ### 🐛 Describe the bug ``` VLLM_MOE_DP_CHUNK_SIZE=1024 NVSHMEM_IB_ENABLE_IBGDA=1 VLLM_DEEPEP_BUFFER_SIZE_MB=0 VLLM_DEEPEP_LOW_LATENCY_USE_MNNVL=1 VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_FLASHINFER_MOE_BACKEND="masked_gemm" VLLM_WORKER_MULTIPROC_METHOD=spawn VLLM_ATTENTION_BACKEND=FLASHINFER_MLA lm_eval --model vllm --model_args pretrained=/data/local/models/DeepSeek-R1-FP4/,data_parallel_size=8,enable_expert_parallel=True,tensor_parallel_size=1,max_model_len=16384,all2all_backend=deepep_low_latency,max_cudagraph_capture_size=8 --trust_remote_code --tasks gsm8k --num_fewshot 5 --batch_size 1024 |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.7627|± |0.0117| | | |strict-match | 5|exact_match|↑ |0.7582|± |0.0118| ``` However, there is no accuracy issue with VLLM_MOE_DP_CHUNK_SIZE=256, which is the default when VLLM_MOE_DP_CHUNK_SIZE is not set: ``` VLLM_MOE_DP_CHUNK_SIZE=256 NVSHMEM_IB_ENABLE_IBGDA=1 VLL...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: NVFP4 Flashinfer CuteDSL MoE + DeepEP ll + VLLM_MOE_DP_CHUNK_SIZE=1024 + cudagraph numerical accuracy issue on B200 bug;unstale;nvidia ### Your current environment There seems to be a numerical accuracy issue with nvfp4...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: eDSL MoE + DeepEP ll + VLLM_MOE_DP_CHUNK_SIZE=1024 + cudagraph numerical accuracy issue on B200 bug;unstale;nvidia ### Your current environment There seems to be a numerical accuracy issue with nvfp4 flashinfer cutedsl...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: hinfer CuteDSL MoE + DeepEP ll + VLLM_MOE_DP_CHUNK_SIZE=1024 + cudagraph numerical accuracy issue on B200 bug;unstale;nvidia ### Your current environment There seems to be a numerical accuracy issue with nvfp4 flashinfe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: NVFP4 Flashinfer CuteDSL MoE + DeepEP ll + VLLM_MOE_DP_CHUNK_SIZE=1024 + cudagraph numerical accuracy issue on B200 bug;unstale;nvidia ### Your current environment There seems to be a numerical accuracy issue wit...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: NVFP4 Flashinfer CuteDSL MoE + DeepEP ll + VLLM_MOE_DP_CHUNK_SIZE=1024 + cudagraph numerical accuracy issue on B200 bug;unstale;nvidia ### Your current environment There seems to be a numerical accuracy issue wit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
