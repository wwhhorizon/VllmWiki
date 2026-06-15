# vllm-project/vllm#18421: [Bug]: Cutlass MoE for Llama 4 FP8 broken in 0.9.0 ?

| 字段 | 值 |
| --- | --- |
| Issue | [#18421](https://github.com/vllm-project/vllm/issues/18421) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cutlass MoE for Llama 4 FP8 broken in 0.9.0 ?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On vllm `0.9.0` and also the recent nightly version, there is a functional break when running the FP8 variant of Llama-4 Maverick. I guess it might be a bug in the Cutlass MoE kernel? ``` model=meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 lm_eval --model vllm \ --model_args "pretrained=$model,tensor_parallel_size=8,max_model_len=100000" \ --tasks gsm8k \ --batch_size auto \ --seed 42 \ --trust_remote_code \ --limit 100 ``` on `0.8.5.post1` above results in 94.00% accuracy, whilst on `0.9.0` the accuracy drops to 31.00%. The problem persists in the nightly built of `0.9.1.dev9+gd6c86d09a` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### 🐛 Describe the bug On vllm `0.9.0` and also the recent nightly version, there is a functional break when running the FP8 variant of Llama-4 Maverick. I guess it might be a bug in the Cutlass MoE kernel? ``` model=me...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Cutlass MoE for Llama 4 FP8 broken in 0.9.0 ? bug ### Your current environment ### 🐛 Describe the bug On vllm `0.9.0` and also the recent nightly version, there is a functional break when running the FP8 variant...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: =$model,tensor_parallel_size=8,max_model_len=100000" \ --tasks gsm8k \ --batch_size auto \ --seed 42 \ --trust_remote_code \ --limit 100 ``` on `0.8.5.post1` above results in 94.00% accuracy, whilst on `0.9.0` the accur...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: kernel? ``` model=meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 lm_eval --model vllm \ --model_args "pretrained=$model,tensor_parallel_size=8,max_model_len=100000" \ --tasks gsm8k \ --batch_size auto \ --seed 42 \ -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Cutlass MoE for Llama 4 FP8 broken in 0.9.0 ? bug ### Your current environment ### 🐛 Describe the bug On vllm `0.9.0` and also the recent nightly version, there is a functional break when running the FP8 variant...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
