# vllm-project/vllm#30872: [Bug]: Triton kernel failing for LoRA on SM100

| 字段 | 值 |
| --- | --- |
| Issue | [#30872](https://github.com/vllm-project/vllm/issues/30872) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Triton kernel failing for LoRA on SM100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hey, i am trying to use a LoRA model and the triton kernel compilation fails. I serve the model like this: CUDA_VISIBLE_DEVICES=5 POOLING_METHOD_TO_EVALUATE="avg" vllm serve --port 1328 --gpu-memory-utilization 0.95 --enforce-eager --enable-lora --lora-modules lora1= Startup works without problems, but once i send the first request like this: curl http://localhost:1328/v1/completions -H "Content-Type: application/json" -d '{ "model": "lora1", "prompt": "Solve 1+1", "temperature": 0.0, "max_tokens": 256 }' The model crashes with this error output: (APIServer pid=293776) INFO: Waiting for application startup. (APIServer pid=293776) INFO: Application startup complete. (APIServer pid=293776) WARNING 12-17 14:09:07 [input_processor.py:243] vLLM has deprecated support for supporting different tokenizers for different LoRAs. By default, vLLM uses base model's tokenizer. If you are using a LoRA with its own tokenizer, consider specifying `--tokenizer [lora_path]` to use the LoRA tokenizer. (EngineCore_DP0 pid=777277) WARNING 12-17 14:09:07 [utils.py:250] Using default LoRA kernel configs /raid/home/q516563/miniforge3/envs/funnel/lib/pyth...

## 现有链接修复摘要

#32836 [BugFix] Add env variable to control PDL in LoRA

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Triton kernel failing for LoRA on SM100 bug ### Your current environment ### 🐛 Describe the bug Hey, i am trying to use a LoRA model and the triton kernel compilation fails. I serve the model like this: CUDA_VISI...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: dules lora1= Startup works without problems, but once i send the first request like this: curl http://localhost:1328/v1/completions -H "Content-Type: application/json" -d '{ "model": "lora1", "prompt": "Solve 1+1", "tem...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: s tokenizer. If you are using a LoRA with its own tokenizer, consider specifying `--tokenizer [lora_path]` to use the LoRA tokenizer. (EngineCore_DP0 pid=777277) WARNING 12-17 14:09:07 [utils.py:250] Using default LoRA...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: i32}, %arg16: i32 {tt.divisibility = 16 : i32}) attributes {noinline = false} { %c1_i32 = arith.constant 1 : i32 %c0_i32 = arith.constant 0 : i32 %cst = arith.constant dense : tensor %c16_i32 = arith.constant 16 : i32 %...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32836](https://github.com/vllm-project/vllm/pull/32836) | closes_keyword | 0.95 | [BugFix]  Add env variable to control PDL in LoRA | FIX #30872 FIX https://github.com/vllm-project/vllm/issues/32424 ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist < |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
