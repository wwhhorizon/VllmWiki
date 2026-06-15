# vllm-project/vllm#32919: [Bug]: Memory fault access when serving DeepSeek-R1-0528 with mori-ep + concurrency of 128 / 256

| 字段 | 值 |
| --- | --- |
| Issue | [#32919](https://github.com/vllm-project/vllm/issues/32919) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Memory fault access when serving DeepSeek-R1-0528 with mori-ep + concurrency of 128 / 256

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Encounter memory fault access when performing "vllm serve bench with concurrency of 128 and 256". No error for the case of concurrency of 64 vllm serve command ```text VLLM_ROCM_USE_AITER=1 vllm serve deepseek-ai/DeepSeek-R1-0528 \ -tp 1 \ -dp 8 \ --enable-expert-parallel \ --block-size 1 \ --disable-nccl-for-dp-synchronization \ --swap-space 16 \ --all2all-backend mori ``` vllm serve bench command ```text vllm bench serve \ --backend vllm \ --model deepseek-ai/DeepSeek-R1-0528 \ --dataset-name random \ --random-input-len 8192 \ --port 8000 \ --max-concurrency 64 \ --num-prompts 640 \ --ignore-eos \ --percentile_metrics ttft,tpot,itl,e2el \ --random-output-len 1024 ``` error: concurrency -128 Memory fault access by GPU node-8 (Agent handle: 0xacc7930) on address 0x7fac074e2000. Reason: Unknown. concurrency - 256 Memory fault access by GPU node-2 (Agent handle: 0xb127610) on address 0x7ec7f81eb000. Reason: Unknown. Memory fault access by GPU node-3 (Agent handle: 0xc229850) on address 0x7ec4b665d000. Reason: Unknown. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbo...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: the case of concurrency of 64 vllm serve command ```text VLLM_ROCM_USE_AITER=1 vllm serve deepseek-ai/DeepSeek-R1-0528 \ -tp 1 \ -dp 8 \ --enable-expert-parallel \ --block-size 1 \ --disable-nccl-for-dp-synchronization...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;kernel;moe;operator;sampling;triton bui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: hen serving DeepSeek-R1-0528 with mori-ep + concurrency of 128 / 256 bug;rocm ### Your current environment ### 🐛 Describe the bug Encounter memory fault access when performing "vllm serve bench with concurrency of 128 a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: /DeepSeek-R1-0528 \ -tp 1 \ -dp 8 \ --enable-expert-parallel \ --block-size 1 \ --disable-nccl-for-dp-synchronization \ --swap-space 16 \ --all2all-backend mori ``` vllm serve bench command ```text vllm bench serve \ --...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: vllm serve deepseek-ai/DeepSeek-R1-0528 \ -tp 1 \ -dp 8 \ --enable-expert-parallel \ --block-size 1 \ --disable-nccl-for-dp-synchronization \ --swap-space 16 \ --all2all-backend mori ``` vllm serve bench command ```text...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
