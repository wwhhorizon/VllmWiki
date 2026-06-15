# vllm-project/vllm#43096: [Bug]: Performance degradation on MoE models with low batch sizes since vLLM v0.20.0

| 字段 | 值 |
| --- | --- |
| Issue | [#43096](https://github.com/vllm-project/vllm/issues/43096) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Performance degradation on MoE models with low batch sizes since vLLM v0.20.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, I have observed a performance decrease in MoE models, notably gpt-oss-120b since vLLM v0.20.0 I use this bench command to measure the performance, on 2xH100 (same performance drop with and without NvLink) ``` MODEL=openai/gpt-oss-120b vllm bench throughput --model $MODEL--num-prompts 200 --random-input-len 600 --random-output-len 600 --max-num-seqs=10 --tensor-parallel-size=2 ``` The performance drops happens only with --max-num-seqs=10, if I don't set it (so batch sizes of 1000), no performance drop is observed On docker image vllm/vllm-openai:v0.19.1: ``` Throughput: 1.88 requests/s, 2252.27 total tokens/s, 1126.14 output tokens/s Total num prompt tokens: 120000 Total num output tokens: 120000 ``` On vllm/vllm-openai:v0.20.0: ``` Throughput: 1.46 requests/s, 1750.12 total tokens/s, 875.06 output tokens/s Total num prompt tokens: 120000 Total num output tokens: 120000 ``` On vllm/vllm-openai:v0.20.0-cu129 ``` Throughput: 1.46 requests/s, 1750.30 total tokens/s, 875.15 output tokens/s Total num prompt tokens: 120000 Total num output tokens: 120000 ``` No configuration changes in the log output of vLLM startup, only flags t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ure the performance, on 2xH100 (same performance drop with and without NvLink) ``` MODEL=openai/gpt-oss-120b vllm bench throughput --model $MODEL--num-prompts 200 --random-input-len 600 --random-output-len 600 --max-num...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Performance degradation on MoE models with low batch sizes since vLLM v0.20.0 bug ### Your current environment ### 🐛 Describe the bug Hello, I have observed a performance decrease in MoE models, notably gpt-oss-1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: _cold_start (from True to False in v0.20.0), changing it has no impact - quantization=mxfp4 changed to quantization=gpt_oss_mxfp4, but from my investigations this seems to be a simple renaming I tried the following: - u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vLLM v0.20.0 I use this bench command to measure the performance, on 2xH100 (same performance drop with and without NvLink) ``` MODEL=openai/gpt-oss-120b vllm bench throughput --model $MODEL--num-prompts 200 --random-in...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ng I tried the following: - used VLLM_MXFP4_USE_MARLIN=1 VLLM_MXFP4_USE_TRITON=1, same issue - set VLLM_ATTENTION_BACKEND=TRITON_ATTN, same issue - benched on meta-llama/Llama-3.1-8B-Instruct, difference is minimal (221...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
