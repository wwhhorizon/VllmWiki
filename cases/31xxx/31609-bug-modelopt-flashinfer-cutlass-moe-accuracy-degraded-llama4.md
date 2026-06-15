# vllm-project/vllm#31609: [Bug][ModelOpt]: FlashInfer CUTLASS MoE Accuracy Degraded (Llama4)

| 字段 | 值 |
| --- | --- |
| Issue | [#31609](https://github.com/vllm-project/vllm/issues/31609) |
| 状态 | closed |
| 标签 | bug;help wanted |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;gemm_linear;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ModelOpt]: FlashInfer CUTLASS MoE Accuracy Degraded (Llama4)

### Issue 正文摘录

### Your current environment H100, B200 ---> vllm 0.13.0 ### 🐛 Describe the bug - running the following: ```bash # modelopt MODEL_TENSOR := "nvidia/Llama-4-Scout-17B-16E-Instruct-FP8" GPUS := "2" PORT := "8001" # sm90 / sm100 launch_cutlass_tensor: VLLM_USE_DEEP_GEMM=0 VLLM_USE_FLASHINFER_MOE_FP8=1 VLLM_FLASHINFER_MOE_BACKEND=throughput vllm serve {{MODEL_TENSOR}} -tp {{GPUS}} --port {{PORT}} --max-model-len 8192 # sm100 launch_trtllm_tensor: VLLM_USE_DEEP_GEMM=0 VLLM_USE_FLASHINFER_MOE_FP8=1 VLLM_FLASHINFER_MOE_BACKEND=latency chg run --gpus {{GPUS}} -- vllm serve {{MODEL_TENSOR}} -tp {{GPUS}} --max-model-len 8192 eval_block: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model={{MODEL_BLOCK}},base_url=http://localhost:{{PORT}}/v1/completions,num_concurrent=1000,tokenized_requests=False" eval_tensor: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model={{MODEL_TENSOR}},base_url=http://localhost:{{PORT}}/v1/completions,num_concurrent=1000,tokenized_requests=False" ``` with cutlass: ```bash local-completions (model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8,base_url=http://localhost:8001/v1/completions,num_concurrent=1000,tokenized_requests=...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: Accuracy Degraded (Llama4) bug;help wanted ### Your current environment H100, B200 ---> vllm 0.13.0 ### 🐛 Describe the bug - running the following: ```bash # modelopt MODEL_TENSOR := "nvidia/Llama-4-Scout-17B-16E-Instru...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug][ModelOpt]: FlashInfer CUTLASS MoE Accuracy Degraded (Llama4) bug;help wanted ### Your current environment H100, B200 ---> vllm 0.13.0 ### 🐛 Describe the bug - running the following: ```bash # modelopt MODEL_TENSOR...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug][ModelOpt]: FlashInfer CUTLASS MoE Accuracy Degraded (Llama4) bug;help wanted ### Your current environment H100, B200 ---> vllm 0.13.0 ### 🐛 Describe the bug - running the following: ```bash # modelopt MODEL_TENSOR...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: `bash # modelopt MODEL_TENSOR := "nvidia/Llama-4-Scout-17B-16E-Instruct-FP8" GPUS := "2" PORT := "8001" # sm90 / sm100 launch_cutlass_tensor: VLLM_USE_DEEP_GEMM=0 VLLM_USE_FLASHINFER_MOE_FP8=1 VLLM_FLASHINFER_MOE_BACKEN...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: } -- vllm serve {{MODEL_TENSOR}} -tp {{GPUS}} --max-model-len 8192 eval_block: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model={{MODEL_BLOCK}},base_url=http://localhost:{{PORT}}/v1/completions,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
