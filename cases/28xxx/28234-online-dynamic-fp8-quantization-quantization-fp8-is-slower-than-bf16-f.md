# vllm-project/vllm#28234: Online Dynamic FP8 Quantization (--quantization="fp8") is slower than BF16/FP16 on RTX 5090

| 字段 | 值 |
| --- | --- |
| Issue | [#28234](https://github.com/vllm-project/vllm/issues/28234) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Online Dynamic FP8 Quantization (--quantization="fp8") is slower than BF16/FP16 on RTX 5090

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Issue Description When enabling Online Dynamic FP8 quantization ( --quantization="fp8" ) for the Qwen3-4B (BF16) model, inference on an RTX 5090 becomes slower than BF16 (no quantization). Wall time increases by ~ 17.9% (395.82s → 466.58s) Token throughput drops by ~ 17.2% (3370.29 → 2791.53 tokens/s) Reproduction Server A (BF16, no quantization) export CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.openai.api_server \ --port 12888 \ --model Qwen/Qwen3-4B \ --tensor-parallel-size 1 \ --served-model-name qwen3-4b \ --gpu-memory-utilization 0.8 \ --max-model-len 8192 Server B (Online Dynamic FP8) export CUDA_VISIBLE_DEVICES=1 python3 -m vllm.entrypoints.openai.api_server \ --port 12999 \ --model Qwen/Qwen3-4B \ --tensor-parallel-size 1 \ --served-model-name qwen3-4b_fp8 \ --gpu-memory-utilization 0.8 \ --max-model-len 8192 \ --quantization="fp8" Benchmark setup 5 rounds × each round randomly sampling 1000 prompts from my self-built JSONL dataset Concurrency=5 , max_tokens=1024 Disabled thinking via chat_template_kwargs.enable_thinking=False Measured wall time and tokens/s (from usage.total_tokens ) Results (5-round averages) Mo...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: Online Dynamic FP8 Quantization (--quantization="fp8") is slower than BF16/FP16 on RTX 5090 bug;stale ### Your current environment ### 🐛 Describe the bug Issue Description When enabling Online Dynamic FP8 quantization (...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: RTX 5090 GPUs? Any guidance or recommended configurations would be appreciated. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: amic FP8 Quantization (--quantization="fp8") is slower than BF16/FP16 on RTX 5090 bug;stale ### Your current environment ### 🐛 Describe the bug Issue Description When enabling Online Dynamic FP8 quantization ( --quantiz...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ling Online Dynamic FP8 quantization ( --quantization="fp8" ) for the Qwen3-4B (BF16) model, inference on an RTX 5090 becomes slower than BF16 (no quantization). Wall time increases by ~ 17.9% (395.82s → 466.58s) Token...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Wall time increases by ~ 17.9% (395.82s → 466.58s) Token throughput drops by ~ 17.2% (3370.29 → 2791.53 tokens/s) Reproduction Server A (BF16, no quantization) export CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
