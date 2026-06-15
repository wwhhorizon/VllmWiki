# vllm-project/vllm#31918: [Bug]: nvidia/DeepSeek-R1-NVFP4-v2 accuracy issue with NVFP4 dispatch (CUTEDSL MoE + DeepEP LL)

| 字段 | 值 |
| --- | --- |
| Issue | [#31918](https://github.com/vllm-project/vllm/issues/31918) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | moe |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: nvidia/DeepSeek-R1-NVFP4-v2 accuracy issue with NVFP4 dispatch (CUTEDSL MoE + DeepEP LL)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `VLLM_DEEPEPLL_NVFP4_DISPATCH=1 VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_USE_STANDALONE_COMPILE=0 VLLM_FLASHINFER_MOE_BACKEND="masked_gemm" VLLM_WORKER_MULTIPROC_METHOD=spawn VLLM_ALL2ALL_BACKEND="deepep_low_latency" lm_eval --model vllm --model_args pretrained=nvidia/DeepSeek-R1-0528-FP4-v2,data_parallel_size=4,enable_expert_parallel=True,tensor_parallel_size=1,enforce_eager=True,max_model_len=2048 --trust_remote_code --tasks gsm8k --num_fewshot 5 --batch_size auto` vllm (pretrained=nvidia/DeepSeek-R1-0528-FP4-v2,data_parallel_size=4,enable_expert_parallel=True,tensor_parallel_size=1,enforce_eager=True,max_model_len=2048,trust_remote_code=True), gen_kwargs: (None), limit: None, num_fewshot: 5, batch_size: auto |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.0402|± |0.0054| | | |strict-match | 5|exact_match|↑ |0.0235|± |0.0042| In comparison, v1 ckpt accuracy is good with fp4 dispatch: `VLLM_DEEPEPLL_NVFP4_DISPATCH=1 VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_USE_STANDALONE_COMPILE=0 VLLM_FLASHINFER_MOE_BACKEND="m...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: nvidia/DeepSeek-R1-NVFP4-v2 accuracy issue with NVFP4 dispatch (CUTEDSL MoE + DeepEP LL) bug ### Your current environment ### 🐛 Describe the bug `VLLM_DEEPEPLL_NVFP4_DISPATCH=1 VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: nvidia/DeepSeek-R1-NVFP4-v2 accuracy issue with NVFP4 dispatch (CUTEDSL MoE + DeepEP LL) bug ### Your current environment ### 🐛 Describe the bug `VLLM_DEEPEPLL_NVFP4_DISPATCH=1 VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: PEPLL_NVFP4_DISPATCH=1 VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_USE_STANDALONE_COMPILE=0 VLLM_FLASHINFER_MOE_BACKEND="masked_gemm" VLLM_WORKER_MULTIPROC_METHOD=spawn VLLM_ALL2ALL_BACKEND="deepep_low_latency" lm_eval --model v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: nvidia/DeepSeek-R1-NVFP4-v2 accuracy issue with NVFP4 dispatch (CUTEDSL MoE + DeepEP LL) bug ### Your current environment ### 🐛 Describe the bug `VLLM_DEEPEPLL_NVFP4_DISPATCH=1 VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: nvidia/DeepSeek-R1-NVFP4-v2 accuracy issue with NVFP4 dispatch (CUTEDSL MoE + DeepEP LL) bug ### Your current environment ### 🐛 Describe the bug `VLLM_DEEPEPLL_NVFP4_DISPATCH=1 VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_USE_STA...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
