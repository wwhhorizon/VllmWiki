# vllm-project/vllm#30461: [Bug]: Lora support don't work on 0.12.0 with Qwen3-30B-A30B-Instuct-2507

| 字段 | 值 |
| --- | --- |
| Issue | [#30461](https://github.com/vllm-project/vllm/issues/30461) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Lora support don't work on 0.12.0 with Qwen3-30B-A30B-Instuct-2507

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm use vllm dynamic load lora feature with Qwen3-30B-A3B-Instruct-2507 on 4090 (48G) gpu. vllm 0.11.2 is fine; after try vllm 0.12.0, (install normal vllm, flashinfer related package, and fix DeepGEMM missed error with ```uv pip install git+https://github.com/deepseek-ai/DeepGEMM.git@v2.1.1.post3 --no-build-isolation```) it's report a assert error. start scripts ```vllm_lora.sh #!/bin/bash export MODEL=bash99/Qwen3-30B-A3B-Instruct-2507-FP8-Dynamic export MODEL_NAME=Qwen3-30B-A3B-Instruct-2507 export VLLM_ALLOW_RUNTIME_LORA_UPDATING=True VLLM_TUNED_CONFIG_FOLDER=./vllm_tuned_dir/ CUDA_VISIBLE_DEVICES=0,1 vllm serve $MODEL \ --served-model-name $MODEL_NAME default --port 17862 --trust-remote-code \ --gpu-memory-utilization 0.92 --max-model-len 32768 --max_num_seqs 96 -tp 2 \ -O3 --enable-chunked-prefill --max_num_batched_tokens 16384 --enable_prefix_caching \ --enable-lora --max_lora_rank 16 --max-loras 2 ``` Errors ``` (Worker_TP0 pid=135688) ERROR 12-11 13:08:45 [multiproc_executor.py:750] File "/data/deployer24/miniforge3/envs/vllm_0.12.x/lib/python3.12/site-packages/vllm/lora/layers/fused_moe.py", line 140, in _inject_lora_in...

## 现有链接修复摘要

#37193 [LoRA] Add LoRA support for Qwen3OmniMoeThinkerForConditionalGeneration

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: uct-2507 on 4090 (48G) gpu. vllm 0.11.2 is fine; after try vllm 0.12.0, (install normal vllm, flashinfer related package, and fix DeepGEMM missed error with ```uv pip install git+https://github.com/deepseek-ai/DeepGEMM....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: llm_lora.sh #!/bin/bash export MODEL=bash99/Qwen3-30B-A3B-Instruct-2507-FP8-Dynamic export MODEL_NAME=Qwen3-30B-A3B-Instruct-2507 export VLLM_ALLOW_RUNTIME_LORA_UPDATING=True VLLM_TUNED_CONFIG_FOLDER=./vllm_tuned_dir/ C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Lora support don't work on 0.12.0 with Qwen3-30B-A30B-Instuct-2507 bug ### Your current environment ### 🐛 Describe the bug I'm use vllm dynamic load lora feature with Qwen3-30B-A3B-Instruct-2507 on 4090 (48G) gpu...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: lm 0.12.0, (install normal vllm, flashinfer related package, and fix DeepGEMM missed error with ```uv pip install git+https://github.com/deepseek-ai/DeepGEMM.git@v2.1.1.post3 --no-build-isolation```) it's report a asser...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ) gpu. vllm 0.11.2 is fine; after try vllm 0.12.0, (install normal vllm, flashinfer related package, and fix DeepGEMM missed error with ```uv pip install git+https://github.com/deepseek-ai/DeepGEMM.git@v2.1.1.post3 --no...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37193](https://github.com/vllm-project/vllm/pull/37193) | closes_keyword | 0.95 | [LoRA] Add LoRA support for Qwen3OmniMoeThinkerForConditionalGeneration | FIX #31205 Related: #30461, PR #34097 ### Changes 1. **Import and inherit `SupportsLoRA`** -- enables `--enable-lora` for this model 2. **Define `packed_modules_mapping`** -- map |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
