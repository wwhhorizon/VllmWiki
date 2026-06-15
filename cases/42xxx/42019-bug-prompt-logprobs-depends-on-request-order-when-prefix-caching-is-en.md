# vllm-project/vllm#42019: [Bug]: `prompt_logprobs` depends on request order when prefix caching is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#42019](https://github.com/vllm-project/vllm/issues/42019) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `prompt_logprobs` depends on request order when prefix caching is enabled

### Issue 正文摘录

### Your current environment ### Describe the bug I found that `prompt_logprobs` for the same fixed token prompts can change when the same prompts are scored in a different batch order. This is a scoring-only repro: no sampling path is involved. Each prompt is fixed token ids, and logprobs are read via `lp_dict[token_id].logprob`. With `enable_prefix_caching=True` (default), reordering the requests changes per-token logprobs for the same prompt. With `enable_prefix_caching=False`, the same test prints exact zeros. ## Expected behavior Reordering independent requests in a batch should not change: ```text log p(t_k | t_<k) ``` for any fixed prompt. ## Repro ```python import gc import torch from vllm import LLM, SamplingParams PROMPTS = [ [1, 10408, 15, 3312, 16315, 7519, 47932, 247, 16204, 275, 4255, 20098, 19083, 15, 2064, 6505, 347, 11853, 665, 1978, 368, 1977, 432, 4076, 8737, 13, 12868, 342, 326, 28148, 2929, 13], [2, 187, 6759, 16, 681, 16, 12929, 316, 14, 88, 1087, 16, 73, 1976, 16, 73, 15, 5581, 2, 1387, 4311, 187, 7330, 14, 9150, 9283, 608, 14, 2420, 187, 7330, 14], [3, 16440, 323, 368, 24174, 634, 12108, 13, 38857, 17087, 294, 4399, 19083, 15, 2064, 368, 971, 11853, 14565,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ``text log p(t_k | t_<k) ``` for any fixed prompt. ## Repro ```python import gc import torch from vllm import LLM, SamplingParams PROMPTS = [ [1, 10408, 15, 3312, 16315, 7519, 47932, 247, 16204, 275, 4255, 20098, 19083,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: pos].item():.6f}" ) llm = LLM( "EleutherAI/pythia-14m", dtype="float32", gpu_memory_utilization=0.5, # enable_prefix_caching=False makes this repro print exact zeros. ) try: ref = score(llm, (0, 1, 2)) same_order = scor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: except Exception: pass del llm gc.collect() if torch.cuda.is_available(): torch.cuda.empty_cache() ``` ## Output ```text same order repeated: prompt starting with 1: max=0.000000 at pos=0 ref=0.000000 cur=0.000000 promp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: `prompt_logprobs` depends on request order when prefix caching is enabled bug ### Your current environment ### Describe the bug I found that `prompt_logprobs` for the same fixed token prompts can change when the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: quantization;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
