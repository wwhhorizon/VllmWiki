# vllm-project/vllm#8005: [Performance]: Issues with prefix cache usage 

| 字段 | 值 |
| --- | --- |
| Issue | [#8005](https://github.com/vllm-project/vllm/issues/8005) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Issues with prefix cache usage 

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression I have been using vLLM with prefix caching to optimise inference in cases where majority of operations are pre-fills with large shared prefix. Specially, most of the prompts are 130 tokens in size with 90% of it is a shared system prompt. The decode is only phase is only one token. There benchmark is a 100000 prompts (`formatted_prompts` below) executed via generate: ```python from outlines import models, generate llm = LLM("meta-llama/Meta-Llama-3-8B-Instruct", enable_prefix_caching=True) sampling_params = SamplingParams(temperature=0.5, top_p=0.2, max_tokens=1) model = models.VLLM(llm) generator = generate.choice(model, ["yes", "no"]) predictions = generator(formatted_prompts, sampling_params=sampling_params) ``` During experiments I have observed that if I use the **same prompt** repeatedly (`formatted_prompts` is identical prompt repeated 100000 times) I observe **no throughput speed up** in inference compared to cases where only 90% of tokens are shared between prompts. This is true for different backends and block sizes. In fact, increasing block size from 4 to 16 increases to inference 3-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: where majority of operations are pre-fills with large shared prefix. Specially, most of the prompts are 130 tokens in size with 90% of it is a shared system prompt. The decode is only phase is only one token. There benc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: s necessary) ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: e is only phase is only one token. There benchmark is a 100000 prompts (`formatted_prompts` below) executed via generate: ```python from outlines import models, generate llm = LLM("meta-llama/Meta-Llama-3-8B-Instruct",...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: roposal to improve performance _No response_ ### Report of performance regression I have been using vLLM with prefix caching to optimise inference in cases where majority of operations are pre-fills with large shared pr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Performance]: Issues with prefix cache usage performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I have been using vLLM with prefix caching to optimise inference in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
