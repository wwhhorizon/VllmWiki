# vllm-project/vllm#421: +34% higher throughput?

| 字段 | 值 |
| --- | --- |
| Issue | [#421](https://github.com/vllm-project/vllm/issues/421) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 46; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cache;cuda;kernel;sampling |
| 症状 | slowdown |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> +34% higher throughput?

### Issue 正文摘录

# +34% higher throughput? TLDR: Seeing vLLM has been really fascinating! @oleitersdorf and I investigated whether we could further accelerate vLLM by profiling its performance with GPU counters. Currently, we believe we have achieve a speed-up of 1.34x for the benchmark reported on the vLLM website. As the vLLM site claims "24x higher throughput compared to HF and up to 3.5x higher throughput than TGI", and the techniques we show below improve a further 1.34x, then vLLM has the potential to have a **29.5x higher throughput compared to the baseline HF and 4.7x over TGI**. Many thanks to the authors for developing this really exciting work -- we had a great time reading your code! We are sure that you probably already thought of the improvements we show below (and maybe just didn't get to them), and would love to hear your thoughts. Below we write out the optimizations we found, and list several open directions which could hopefully speed up even further. **The goal of this issue is to encourage discussion and brainstorm potential improvements** -- some parts are still a POC and require more work to make reach production-ready levels. For the part which is already production-ready,...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: NUM_THREADS / THREAD_GROUP_SIZE; const scalar_t* q_ptr = q + seq_idx * q_stride + head_idx * HEAD_SIZE; __shared__ Q_vec q_vecs[THREAD_GROUP_SIZE][NUM_VECS_PER_THREAD]; if (thread_group_idx (q_ptr + vec_idx * VEC_SIZE);...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: +34% higher throughput? feature request # +34% higher throughput? TLDR: Seeing vLLM has been really fascinating! @oleitersdorf and I investigated whether we could further accelerate vLLM by profiling its performance wit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e request # +34% higher throughput? TLDR: Seeing vLLM has been really fascinating! @oleitersdorf and I investigated whether we could further accelerate vLLM by profiling its performance with GPU counters. Currently, we...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: --dataset ./ShareGPT_V3_unfiltered_cleaned_split.json --model openlm-research/open_llama_13b --tokenizer hf-internal-testing/llama-tokenizer --num-prompts=1000 ``` We begin by running the above on a clean clone of vLLM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vLLM website. As the vLLM site claims "24x higher throughput compared to HF and up to 3.5x higher throughput than TGI", and the techniques we show below improve a further 1.34x, then vLLM has the potential to have a **2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
