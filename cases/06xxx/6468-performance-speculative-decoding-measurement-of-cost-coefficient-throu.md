# vllm-project/vllm#6468: [Performance]: [Speculative Decoding] Measurement of Cost Coefficient through vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#6468](https://github.com/vllm-project/vllm/issues/6468) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: [Speculative Decoding] Measurement of Cost Coefficient through vLLM

### Issue 正文摘录

### Proposal to improve performance Recently, vLLM has been conducting a lot of work related to Speculative Decoding, and we often see remarkable achievements. For the Speculative Decoding algorithm to achieve maximum efficiency, it is important to consider not only the performance of the draft and target models but also the **speed of each model**. According to the Definition 3.7 from [original Speculative Decoding paper](https://arxiv.org/pdf/2211.17192), the latency ratio between the target model and the draft model is referred to as the Cost Coefficient `c`. And it is assumed that the `c` value is very small. 🤔 **However, when I examined the vLLM github repo as far as I can, I could not find any information related to the Cost Coefficient.** I have attempted various methods to obtain the Cost Coefficient value for each model on my own. For example: ``` VLLM_ATTENTION_BACKEND=FLASH_ATTN nsys profile -t cuda,nvtx,osrt,cudnn,cublas -o llama_7b_nsight_report ./venv/bin/python3 ./benchmarks/benchmark_latency.py --model NousResearch/Llama-2-7b-hf --enforce-eager --input-len 128 --output-len 2 --batch-size 1 --num-iters-warmup 5 --num-iters 5 VLLM_ATTENTION_BACKEND=FLASH_ATTN nsys pr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: s important to consider not only the performance of the draft and target models but also the **speed of each model**. According to the Definition 3.7 from [original Speculative Decoding paper](https://arxiv.org/pdf/2211...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ginal Speculative Decoding paper](https://arxiv.org/pdf/2211.17192), the latency ratio between the target model and the draft model is referred to as the Cost Coefficient `c`. And it is assumed that the `c` value is ver...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Performance]: [Speculative Decoding] Measurement of Cost Coefficient through vLLM performance ### Proposal to improve performance Recently, vLLM has been conducting a lot of work related to Speculative Decoding, and we...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: s the Cost Coefficient `c`. And it is assumed that the `c` value is very small. 🤔 **However, when I examined the vLLM github repo as far as I can, I could not find any information related to the Cost Coefficient.** I ha...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: [Speculative Decoding] Measurement of Cost Coefficient through vLLM performance ### Proposal to improve performance Recently, vLLM has been conducting a lot of work related to Speculative Decoding, and we...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
