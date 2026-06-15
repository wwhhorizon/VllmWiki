# vllm-project/vllm#42125: [Bug]: Runtime LoRA same-name reload can reuse stale prefix-cache blocks from previous adapter version

| 字段 | 值 |
| --- | --- |
| Issue | [#42125](https://github.com/vllm-project/vllm/issues/42125) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;sampling;triton |
| 症状 | build_error;mismatch;nondeterministic |
| 根因提示 | env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Runtime LoRA same-name reload can reuse stale prefix-cache blocks from previous adapter version

### Issue 正文摘录

### Your current environment ### Describe the bug When replacing a LoRA adapter at runtime under the same `lora_name`, vLLM can reuse prefix-cache blocks computed with the previous adapter version. In this repro, adapter B is validated independently and produces `BETA_ADAPTER_VERSION_B` on a cold server. After warming adapter A under the same name and replacing it with adapter B using `/v1/load_lora_adapter` with `load_inplace=true`, the same prompt returns `BETA_VERSION_B` instead. That non-cold B output only appears when prefix-cache blocks can be reused. The exact B output is restored when prefix caching is disabled, when `cache_salt` is changed, when the first prompt block is changed, when the server is restarted and B is loaded cold, or when B is loaded under a unique adapter name. I also reproduced the same non-cold B output after `/v1/unload_lora_adapter` followed by `/v1/load_lora_adapter` under the same `lora_name`, so the issue appears to be same-name runtime adapter reload/replacement without adapter-version cache invalidation, not only the `load_inplace` branch. Related but not exact duplicates: - #30931 covers the known/general same-name LoRA prefix-cache collision wi...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: is loaded cold, or when B is loaded under a unique adapter name. I also reproduced the same non-cold B output after `/v1/unload_lora_adapter` followed by `/v1/load_lora_adapter` under the same `lora_name`, so the issue...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: me-name reload can reuse stale prefix-cache blocks from previous adapter version ### Your current environment ### Describe the bug When replacing a LoRA adapter at runtime under the same `lora_name`, vLLM can reuse pref...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: B output, consistent with stale blocks being bypassed. ### Duplicate search performed I searched open and closed issues for: - `load_inplace prefix cache lora` - `load_lora_adapter prefix cache` - `unload_lora_adapter p...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: Runtime LoRA same-name reload can reuse stale prefix-cache blocks from previous adapter version ### Your current environment ### Describe the bug When replacing a LoRA adapter at runtime under the same `lora_name...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: Runtime LoRA same-name reload can reuse stale prefix-cache blocks from previous adapter version ### Your current environment ### Describe the bug When replacing a LoRA adapter at runtime under the same `lora_name...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
