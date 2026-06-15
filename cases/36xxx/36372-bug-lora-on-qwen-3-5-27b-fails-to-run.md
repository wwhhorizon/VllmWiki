# vllm-project/vllm#36372: [Bug]: LoRA on Qwen-3.5-27B fails to run

| 字段 | 值 |
| --- | --- |
| Issue | [#36372](https://github.com/vllm-project/vllm/issues/36372) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LoRA on Qwen-3.5-27B fails to run

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running Qwen-3.5 models like 27B runs fine with vllm, but when trying to load a LoRA adapter for it. It fails with this error on startup: ``` (Worker pid=190481) (Worker_TP1 pid=190481) WARNING 03-07 20:00:38 [model_manager.py:332] Regarding Qwen3_5ForConditionalGeneration, vLLM currently only supports adding LoRA to language model, visual.blocks.26.mlp.linear_fc1 will be ignored. (Worker pid=190481) (Worker_TP1 pid=190481) WARNING 03-07 20:00:38 [model_manager.py:332] Regarding Qwen3_5ForConditionalGeneration, vLLM currently only supports adding LoRA to language model, visual.blocks.26.mlp.linear_fc2 will be ignored. (Worker pid=190480) (Worker_TP0 pid=190480) INFO 03-07 20:00:39 [gpu_model_runner.py:4532] Model loading took 26.37 GiB memory and 6.007381 seconds (Worker pid=190480) (Worker_TP0 pid=190480) INFO 03-07 20:00:39 [gpu_model_runner.py:5454] Encoder cache will be initialized with a budget of 16384 tokens, and profiled with 1 image items of the maximum feature size. (Worker pid=190481) (Worker_TP1 pid=190481) INFO 03-07 20:00:39 [gpu_model_runner.py:5454] Encoder cache will be initialized with a budget of 16384 tokens,...

## 现有链接修复摘要

#36652 Fix Qwen3.5 LoRA packed module mapping | #36825 [Bugfix] Fix Qwen3.5 LoRA IndexError in packed_modules_mapping | #37019 fix: generalize LoRA layer handling for N-way fused projections

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 58 [backends.py:920] Using cache directory: /home/arli/.cache/vllm/torch_compile_cache/695823b8aa/rank_0_0/backbone for vLLM's torch.compile (Worker pid=190480) (Worker_TP0 pid=190480) INFO 03-07 20:00:58 [backends.py:9...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 54] Encoder cache will be initialized with a budget of 16384 tokens, and profiled with 1 image items of the maximum feature size. (Worker pid=190481) (Worker_TP1 pid=190481) INFO 03-07 20:00:39 [gpu_model_runner.py:5454...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e size. (Worker pid=190480) (Worker_TP0 pid=190480) INFO 03-07 20:00:58 [backends.py:920] Using cache directory: /home/arli/.cache/vllm/torch_compile_cache/695823b8aa/rank_0_0/backbone for vLLM's torch.compile (Worker p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: TP0 pid=190480) INFO 03-07 20:01:10 [gpu_model_runner.py:5575] Profiling CUDA graph memory: PIECEWISE=102 (largest=512), FULL=102 (largest=512) (Worker pid=190481) (Worker_TP1 pid=190481) INFO 03-07 20:01:10 [gpu_model_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: tion, vLLM currently only supports adding LoRA to language model, visual.blocks.26.mlp.linear_fc1 will be ignored. (Worker pid=190481) (Worker_TP1 pid=190481) WARNING 03-07 20:00:38 [model_manager.py:332] Regarding Qwen...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36652](https://github.com/vllm-project/vllm/pull/36652) | closes_keyword | 0.95 | Fix Qwen3.5 LoRA packed module mapping | fix for the crash reported in: - #36478 - #36372 ## Test Plan 1. Reproduce the issue with a Qwen3.5 model + LoRA adapter. Before this change, engine initialization fails durin |
| [#36825](https://github.com/vllm-project/vllm/pull/36825) | mentioned | 0.6 | [Bugfix] Fix Qwen3.5 LoRA IndexError in packed_modules_mapping | olumnParallelLinearWithLoRA`, but that's a larger refactor. Related: #36372, #36478 ## Test plan - [x] Verified LoRA training (TP=1) completes successfully with Qwen3.5-9B on 2x R… |
| [#37019](https://github.com/vllm-project/vllm/pull/37019) | closes_keyword | 0.95 | fix: generalize LoRA layer handling for N-way fused projections | fix for free. Related: #36372, #36478, #36976 ## Test plan Tested on 2x RTX PRO 6000 Blackwell with LoRA adapters targeting GDN layers (`in_proj_qkv`, `in_proj_z`): **Qwen/Qwen |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
