# vllm-project/vllm#32478: [Bug]: EPLB hangs in several cases

| 字段 | 值 |
| --- | --- |
| Issue | [#32478](https://github.com/vllm-project/vllm/issues/32478) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EPLB hangs in several cases

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Several scenarios where EPLB hangs have been noticed. 1. Async EPLB with DeepEPLL All2All backend and no async scheduling 2. Async EPLB with default All2All backend and async scheduling 3. Sync EPLB with AgRs All2All backend, noticed for `nvidia/DeepSeek-R1-0528-FP4-v2`. Reproduce scripts. Client: ``` lm_eval --model local-completions --tasks gsm8k --model_args model=Qwen/Qwen3-30B-A3B-Instruct-2507-FP8,base_url=http://0.0.0.0:{port}/v1/completions,num_concurrent=50,max_retries=3,tokenized_requests=False ``` Server: ``` # export VLLM_ALL2ALL_BACKEND=deepep_low_latency vllm serve --model=Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 --trust-remote-code --data-parallel-size 2 --tensor-parallel-size 1 --enable-expert-parallel --enable-eplb --eplb-config.window_size 20 --eplb-config.step_interval 20 --eplb-config.use_async true # --no-async-scheduling ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: dia/DeepSeek-R1-0528-FP4-v2`. Reproduce scripts. Client: ``` lm_eval --model local-completions --tasks gsm8k --model_args model=Qwen/Qwen3-30B-A3B-Instruct-2507-FP8,base_url=http://0.0.0.0:{port}/v1/completions,num_conc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ync EPLB with AgRs All2All backend, noticed for `nvidia/DeepSeek-R1-0528-FP4-v2`. Reproduce scripts. Client: ``` lm_eval --model local-completions --tasks gsm8k --model_args model=Qwen/Qwen3-30B-A3B-Instruct-2507-FP8,ba...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_me...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: produce scripts. Client: ``` lm_eval --model local-completions --tasks gsm8k --model_args model=Qwen/Qwen3-30B-A3B-Instruct-2507-FP8,base_url=http://0.0.0.0:{port}/v1/completions,num_concurrent=50,max_retries=3,tokenize...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ust-remote-code --data-parallel-size 2 --tensor-parallel-size 1 --enable-expert-parallel --enable-eplb --eplb-config.window_size 20 --eplb-config.step_interval 20 --eplb-config.use_async true # --no-async-scheduling ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
