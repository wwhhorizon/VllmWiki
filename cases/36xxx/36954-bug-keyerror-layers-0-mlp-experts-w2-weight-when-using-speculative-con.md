# vllm-project/vllm#36954: [Bug]: KeyError 'layers.0.mlp.experts.w2_weight' when using speculative_config method='mtp' with Qwen3.5-122B-GPTQ-Int4 (moe_wna16) 

| 字段 | 值 |
| --- | --- |
| Issue | [#36954](https://github.com/vllm-project/vllm/issues/36954) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError 'layers.0.mlp.experts.w2_weight' when using speculative_config method='mtp' with Qwen3.5-122B-GPTQ-Int4 (moe_wna16) 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving Qwen/Qwen3.5-122B-A10B-GPTQ-Int4 with --quantization moe_wna16 via Docker, enabling MTP speculative decoding causes a KeyError: 'layers.0.mlp.experts.w2_weight' crash during drafter model weight loading. This occurs with both method: "mtp" and the officially recommended method: "qwen3_next_mtp". The latter is internally deprecated and aliased to "mtp" anyway (a WARNING is emitted). Without --speculative-config, the server starts and works normally. ```text docker run -d \ --gpus "device=0,1,2,3" \ --cpuset-cpus="0-17,36-53" \ --shm-size=32g \ --restart unless-stopped \ --name qwen3p5-122b-fp8-tp4-0 \ -v /u0/models/Qwen3.5-122B-A10B-GPTQ-Int4:/model \ -p 8041:8000 \ -e NCCL_P2P_DISABLE=1 \ -e NCCL_SHM_DISABLE=1 \ -e NCCL_IB_DISABLE=1 \ -e CUDA_DEVICE_ORDER=PCI_BUS_ID \ vllm/vllm-openai:cu130-nightly \ --model /model \ --disable-custom-all-reduce \ --served-model-name qwen3.5-122b-int4 \ --quantization moe_wna16 \ --tensor-parallel-size 4 \ --enable-chunked-prefill \ --max-num-seqs 16 \ --max-model-len 262144 \ --reasoning-parser qwen3 \ --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' \ --...

## 现有链接修复摘要

#36970 [Bugfix] Avoid KeyError when loading Qwen3.5 MoE expert weights | #39475 fix: exclude MTP layers from MoE quantization to fix KeyError with moe_wna16

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rving Qwen/Qwen3.5-122B-A10B-GPTQ-Int4 with --quantization moe_wna16 via Docker, enabling MTP speculative decoding causes a KeyError: 'layers.0.mlp.experts.w2_weight' crash during drafter model weight loading. This occu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: eight' when using speculative_config method='mtp' with Qwen3.5-122B-GPTQ-Int4 (moe_wna16) bug ### Your current environment ### 🐛 Describe the bug When serving Qwen/Qwen3.5-122B-A10B-GPTQ-Int4 with --quantization moe_wna...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: KeyError 'layers.0.mlp.experts.w2_weight' when using speculative_config method='mtp' with Qwen3.5-122B-GPTQ-Int4 (moe_wna16) bug ### Your current environment ### 🐛 Describe the bug When serving Qwen/Qwen3.5-122B-...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: KeyError 'layers.0.mlp.experts.w2_weight' when using speculative_config method='mtp' with Qwen3.5-122B-GPTQ-Int4 (moe_wna16) bug ### Your current environment ### 🐛 Describe the bug When serving Qwen/Qwen3.5-122B-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: KeyError 'layers.0.mlp.experts.w2_weight' when using speculative_config method='mtp' with Qwen3.5-122B-GPTQ-Int4 (moe_wna16) bug ### Your current environment ### 🐛 Describe the bug When serving Qwen/Qwen3.5-122B-...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36970](https://github.com/vllm-project/vllm/pull/36970) | closes_keyword | 0.95 | [Bugfix] Avoid KeyError when loading Qwen3.5 MoE expert weights | Fixes #36954 <!-- markdownlint-disable --> ## Purpose ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary |
| [#39475](https://github.com/vllm-project/vllm/pull/39475) | closes_keyword | 0.95 | fix: exclude MTP layers from MoE quantization to fix KeyError with moe_wna16 | Fixes #36954 KeyError: 'layers.0.mlp.experts.w2_weight' when using MTP speculative decoding with --quantization moe_wna16 (e.g., Qwen3.5-122B-A10B-GPTQ-Int4). ## Root Cause When |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
