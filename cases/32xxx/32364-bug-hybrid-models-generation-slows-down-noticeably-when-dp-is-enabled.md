# vllm-project/vllm#32364: [Bug]: Hybrid models generation slows down noticeably when DP is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#32364](https://github.com/vllm-project/vllm/issues/32364) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Hybrid models generation slows down noticeably when DP is enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We have noticed a significant slowdown in generation speed of hybrid models, when using DP in vLLM server. We first noticed it with vLLM v0.11, but it is present in the latest release and dev versions. Pure transformer models (both dense and MoE) appear to be working as expected with DP (maybe slight slowdown), so we think this is specific to hybrid models. We tested different hybrid models, and all of them exhibit the same issue. Below you will find our benchmark results with `nvidia/NVIDIA-Nemotron-Nano-9B-v2` model. Consider first the case of DP=1. We benchmark with 1k random requests. ``` vllm serve --model=nvidia/NVIDIA-Nemotron-Nano-9B-v2 --dtype=bfloat16 --port=8010 --seed=0 --gpu-memory-utilization=0.9 --served-model-name=nemotron --data-parallel-size=1 --max-num-seqs=256 --no-enable-prefix-caching --trust-remote-code vllm bench serve --backend vllm --model nvidia/NVIDIA-Nemotron-Nano-9B-v2 --served-model-name nemotron --port 8010 --dataset-name random --num-prompts 1024 --metric-percentiles 1,25,50,75,99 --random-input-len 200 --random-output-len 2048 --ignore-eos ============ Serving Benchmark Result ============ Succes...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: server. We first noticed it with vLLM v0.11, but it is present in the latest release and dev versions. Pure transformer models (both dense and MoE) appear to be working as expected with DP (maybe slight slowdown), so we...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: iced it with vLLM v0.11, but it is present in the latest release and dev versions. Pure transformer models (both dense and MoE) appear to be working as expected with DP (maybe slight slowdown), so we think this is speci...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: om requests. ``` vllm serve --model=nvidia/NVIDIA-Nemotron-Nano-9B-v2 --dtype=bfloat16 --port=8010 --seed=0 --gpu-memory-utilization=0.9 --served-model-name=nemotron --data-parallel-size=1 --max-num-seqs=256 --no-enable...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: here was some slowdown even for "embedding-only" models, but it was much smaller in comparison to hybrid models (hence, we don't think slowdown can be explained by issues in our network). Since in this case there are no...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: s=256 --no-enable-prefix-caching --trust-remote-code vllm bench serve --backend vllm --model nvidia/NVIDIA-Nemotron-Nano-9B-v2 --served-model-name nemotron --port 8010 --dataset-name random --num-prompts 1024 --metric-p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
