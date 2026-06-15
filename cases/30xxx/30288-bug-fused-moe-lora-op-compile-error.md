# vllm-project/vllm#30288: [Bug]:fused_moe_lora_op compile error

| 字段 | 值 |
| --- | --- |
| Issue | [#30288](https://github.com/vllm-project/vllm/issues/30288) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:fused_moe_lora_op compile error

### Issue 正文摘录

### Your current environment ### Bug description Triton compilation fails in `fused_moe_lora_op.py` when serving GPT-OSS with `--enable-lora`. Running the recommended `serve` command with the LoRA flag ``` VLLM_USE_FLASHINFER_MXFP4_BF16_MOE=1 vllm serve openai/gpt-oss-120b --tensor-parallel-size 4 --async-scheduling --enable-lora ``` Ends with this Triton crash: ``` [0;36m(Worker_TP2 pid=92976)[0;0m WARNING 12-09 01:51:13 [fused_moe.py:888] Using default MoE config. Performance might be sub-optimal! Config file not found at ['/opt/my_venv/lib/python3.12/site-packages/vllm/model_executor/layers/fused_moe/configs/E=128,N=2880,device_name=NVIDIA_B200.json'] /opt/my_venv/lib/python3.12/site-packages/vllm/lora/ops/triton_ops/fused_moe_lora_op.py:164:12: error: 'tt.elementwise_inline_asm' op pipeliner doesn't know how to predicate this op. tl.extra.cuda.gdc_wait() ^ LLVM ERROR: Fatal pipeliner error module { tt.func public @_fused_moe_lora_kernel(%arg0: !tt.ptr {tt.divisibility = 16 : i32}, %arg1: !tt.ptr {tt.divisibility = 16 : i32}, %arg2: !tt.ptr {tt.divisibility = 16 : i32}, %arg3: !tt.ptr {tt.divisibility = 16 : i32}, %arg4: !tt.ptr {tt.divisibility = 16 : i32}, %arg5: !tt.ptr {t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]:fused_moe_lora_op compile error bug;stale ### Your current environment ### Bug description Triton compilation fails in `fused_moe_lora_op.py` when serving GPT-OSS with `--enable-lora`. Running the recommended `ser...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: /model_executor/layers/fused_moe/configs/E=128,N=2880,device_name=NVIDIA_B200.json'] /opt/my_venv/lib/python3.12/site-packages/vllm/lora/ops/triton_ops/fused_moe_lora_op.py:164:12: error: 'tt.elementwise_inline_asm' op...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: recommended `serve` command with the LoRA flag ``` VLLM_USE_FLASHINFER_MXFP4_BF16_MOE=1 vllm serve openai/gpt-oss-120b --tensor-parallel-size 4 --async-scheduling --enable-lora ``` Ends with this Triton crash: ``` [0;3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ription Triton compilation fails in `fused_moe_lora_op.py` when serving GPT-OSS with `--enable-lora`. Running the recommended `serve` command with the LoRA flag ``` VLLM_USE_FLASHINFER_MXFP4_BF16_MOE=1 vllm serve openai...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]:fused_moe_lora_op compile error bug;stale ### Your current environment ### Bug description Triton compilation fails in `fused_moe_lora_op.py` when serving GPT-OSS with `--enable-lora`. Running the recommended `ser...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
