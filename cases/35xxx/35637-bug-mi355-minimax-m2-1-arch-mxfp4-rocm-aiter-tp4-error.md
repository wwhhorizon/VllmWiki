# vllm-project/vllm#35637: [Bug]: mi355 minimax m2.1 arch mxfp4 rocm AITER TP4 error

| 字段 | 值 |
| --- | --- |
| Issue | [#35637](https://github.com/vllm-project/vllm/issues/35637) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;gemm;operator |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: mi355 minimax m2.1 arch mxfp4 rocm AITER TP4 error

### Issue 正文摘录

### Your current environment `vllm/vllm-openai-rocm:v0.16.0` ### 🐛 Describe the bug hi @powderluv @chunfangamd @andyluo7 One of the main value add of AMD's latest flagship MI355X GPU is MXFP4, the ability to have better perf at similar accuracy. While waiting for AMD to release the mxfp4 ckpt of MiniMax M2.5, i was trying to test out amd's mxfp4 checkpoint `amd/MiniMax-M2.1-MXFP4` using amd's vllm/vllm-openai-rocm:v0.16.0 since it has same arch as m2.5 but unfortunately i ran into this error. can u take a look? `amd/MiniMax-M2.1-MXFP4` tp=4 Interestingly MiniMax M2.5 TP4 on FP8 works but MiniMax M2.5 TP4 on FP4 doesnt also note this is performed with `export VLLM_ROCM_USE_AITER=1` and that TP2 AITER MXFP4 works but TP4 does not ``` vllm serve $MODEL --port $PORT \ --tensor-parallel-size=4 \ --gpu-memory-utilization 0.95 \ --max-model-len $MAX_MODEL_LEN \ --block-size=32 \ --disable-log-requests \ --trust-remote-code > $SERVER_LOG 2>&1 & ``` https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22535712810/job/65282641447?pr=827 ``` (Worker_TP0 pid=2914528) ERROR 03-01 04:24:25 [multiproc_executor.py:863] out = rocm_aiter_fused_experts( (Worker_TP0 pid=2914528) ERROR 03-01 04:2...

## 现有链接修复摘要

#35893 [ROCm][Bugfix] Fall back from CK MXFP4 MoE when GEMM dimensions are unsupported

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: mi355 minimax m2.1 arch mxfp4 rocm AITER TP4 error bug;rocm ### Your current environment `vllm/vllm-openai-rocm:v0.16.0` ### 🐛 Describe the bug hi @powderluv @chunfangamd @andyluo7 One of the main value add of AM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [multiproc_executor.py:863] RuntimeError: wrong! device_gemm with the specified compilation parameters does not support this GEMM problem (Worker_TP0 pid=2914528) ERROR 03-01 04:24:25 [multiproc_executor.py:863] (Engine...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: mi355 minimax m2.1 arch mxfp4 rocm AITER TP4 error bug;rocm ### Your current environment `vllm/vllm-openai-rocm:v0.16.0` ### 🐛 Describe the bug hi @powderluv @chunfangamd @andyluo7 One of the main value add of AM...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: e=4 \ --gpu-memory-utilization 0.95 \ --max-model-len $MAX_MODEL_LEN \ --block-size=32 \ --disable-log-requests \ --trust-remote-code > $SERVER_LOG 2>&1 & ``` https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: OR 03-01 04:24:25 [multiproc_executor.py:863] out = rocm_aiter_fused_experts( (Worker_TP0 pid=2914528) ERROR 03-01 04:24:25 [multiproc_executor.py:863] ^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=2914528) ERROR 03-01 04:2...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35893](https://github.com/vllm-project/vllm/pull/35893) | closes_keyword | 0.95 | [ROCm][Bugfix] Fall back from CK MXFP4 MoE when GEMM dimensions are unsupported | Fixes #35637 ## Test plan - With MiniMax-M2.1 MXFP4 on TP=4 (the failing config from the issue): model should load and serve without crash, using the emulation/triton fallback - |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
