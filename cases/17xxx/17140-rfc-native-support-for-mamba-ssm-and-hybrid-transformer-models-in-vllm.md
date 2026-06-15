# vllm-project/vllm#17140: [RFC]: Native support for Mamba, SSM, and hybrid transformer models in vLLM V1

| 字段 | 值 |
| --- | --- |
| Issue | [#17140](https://github.com/vllm-project/vllm/issues/17140) |
| 状态 | open |
| 标签 | RFC;keep-open |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;quantization;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | attention;cache;cuda;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Native support for Mamba, SSM, and hybrid transformer models in vLLM V1

### Issue 正文摘录

### Motivation. Mamba, SSM, and hybrid transformer models are an important path forward towards models that scale linearly with sequence length. vLLM currently supports many models of this class ([Jamba](https://github.com/vllm-project/vllm/pull/4115), [Mamba](https://github.com/vllm-project/vllm/pull/6484), [Codestral Mamba](https://github.com/vllm-project/vllm/pull/9292), [Falcon Mamba](https://github.com/vllm-project/vllm/pull/9325), [Bamba](https://github.com/vllm-project/vllm/pull/10909), [Zamba2](https://github.com/vllm-project/vllm/pull/13185), [MinimaxText01](https://github.com/vllm-project/vllm/pull/13454), [Plamo2](https://github.com/vllm-project/vllm/pull/14323)), and should continue to maintain excellent support for these models. **The Problem** SSM model generally are less-well supported than transformers in vLLM, and have several deficiencies. This RFC proposes several improvements (some already in progress) to SSM models, and additionally will serve as an issue tracker. The major issue is that SSM models not supported in vLLM V1, and should be supported before V0 is deprecated. In addition: * [SSM state management](https://github.com/vllm-project/vllm/blob/05e1fbfc5...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: p-open ### Motivation. Mamba, SSM, and hybrid transformer models are an important path forward towards models that scale linearly with sequence length. vLLM currently supports many models of this class ([Jamba](https://...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC]: Native support for Mamba, SSM, and hybrid transformer models in vLLM V1 RFC;keep-open ### Motivation. Mamba, SSM, and hybrid transformer models are an important path forward towards models that scale linearly wit...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: SM models are incompatible with prefix caching, KV cache offloading, and prefill-decode disaggregation. * There are major performance issues with chunked prefill. ### Proposed Change. **Blockers for SSM and hybrid model...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: rid transformer models are an important path forward towards models that scale linearly with sequence length. vLLM currently supports many models of this class ([Jamba](https://github.com/vllm-project/vllm/pull/4115), [...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: d by the block manager, SSM models are incompatible with prefix caching, KV cache offloading, and prefill-decode disaggregation. * There are major performance issues with chunked prefill. ### Proposed Change. **Blockers...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
