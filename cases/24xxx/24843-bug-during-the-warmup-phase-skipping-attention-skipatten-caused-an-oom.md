# vllm-project/vllm#24843: [Bug]: During the warmup phase, skipping attention (skipatten) caused an OOM (Out of Memory) error later.

| 字段 | 值 |
| --- | --- |
| Issue | [#24843](https://github.com/vllm-project/vllm/issues/24843) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: During the warmup phase, skipping attention (skipatten) caused an OOM (Out of Memory) error later.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # 1.code block: ``` @torch.inference_mode() def _dummy_run( self, num_tokens: int, skip_attn: bool = True, ) -> torch.Tensor: # Padding for DP num_pad, num_tokens_across_dp = self.get_dp_padding(num_tokens) num_tokens += num_pad ``` ``` if self.chunked_prefill_enabled: self.chunked_prefill_workspace_size = min( # Max sure there is enough for 8 full length request or at least # 4 pages of cache per request max( 8 * model_config.max_model_len, 4 * scheduler_config.max_num_seqs * cache_config.block_size), # For long-context models try not to over-allocate limiting # kv-cache space, limiting it to 64k tokens, # which would result in the workspace being: # 2*(576)*(64*1024) = 144mb # (assuming 576 MLA head dim, and fp16) # which would result in up-projected context being # 2*(192*128)*(64*1024) = 3gb # (assuming 192 QK head dim, 128 heads, and fp16) 128 * 1024) ``` # Situation description Context length of 64K, gpu-memory-utilization set to 0.85, with 4–5 GB of remaining memory on the D node. # Bug description: chunked_prefill_workspace_size itself is a relatively large hyperparameter, which causes GPU memory usage to increase during...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ing attention (skipatten) caused an OOM (Out of Memory) error later. bug;stale ### Your current environment ### 🐛 Describe the bug # 1.code block: ``` @torch.inference_mode() def _dummy_run( self, num_tokens: int, skip_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling build_error;nan_inf;oom...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: During the warmup phase, skipping attention (skipatten) caused an OOM (Out of Memory) error later. bug;stale ### Your current environment ### 🐛 Describe the bug # 1.code block: ``` @torch.inference_mode() def _du...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ;stale ### Your current environment ### 🐛 Describe the bug # 1.code block: ``` @torch.inference_mode() def _dummy_run( self, num_tokens: int, skip_attn: bool = True, ) -> torch.Tensor: # Padding for DP num_pad, num_toke...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
