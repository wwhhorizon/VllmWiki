# vllm-project/vllm#39030: [Bug]: Certain Ranks Take a Look Time to Load Weights

| 字段 | 值 |
| --- | --- |
| Issue | [#39030](https://github.com/vllm-project/vllm/issues/39030) |
| 状态 | open |
| 标签 | bug;help wanted |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Certain Ranks Take a Look Time to Load Weights

### Issue 正文摘录

### Your current environment B200 VM ### 🐛 Describe the bug I noticed that sometimes certain ranks take a very long time to load. monkeypatched log (so it logs the load time per rank) ``` r_TP0_EP0 pid=3425910) INFO 04-05 11:38:59 [default_loader.py:369] Starting load weights (Worker_TP3_EP3 pid=3425913) INFO 04-05 11:38:59 [default_loader.py:369] Starting load weights Loading safetensors checkpoint shards: 0% Completed | 0/163 [00:00<?, ?it/s] Loading safetensors checkpoint shards: 1% Completed | 1/163 [00:00<00:48, 3.31it/s] Loading safetensors checkpoint shards: 1% Completed | 2/163 [00:00<00:41, 3.88it/s] Loading safetensors checkpoint shards: 2% Completed | 4/163 [00:00<00:35, 4.51it/s] Loading safetensors checkpoint shards: 3% Completed | 5/163 [00:01<00:29, 5.38it/s] Loading safetensors checkpoint shards: 4% Completed | 7/163 [00:01<00:29, 5.25it/s] Loading safetensors checkpoint shards: 5% Completed | 8/163 [00:01<00:26, 5.93it/s] Loading safetensors checkpoint shards: 6% Completed | 9/163 [00:01<00:27, 5.69it/s] Loading safetensors checkpoint shards: 6% Completed | 10/163 [00:01<00:28, 5.41it/s] Loading safetensors checkpoint shards: 7% Completed | 12/163 [00:02<00:19, 7....

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: .py:109] Checkpoint does not provide a q scaling factor. Setting it to k_scale. This only matters for FP8 Attention backends (flash-attn or flashinfer). (Worker_TP0_EP0 pid=3425910) WARNING 04-05 11:39:27 [kv_cache.py:1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: aling factor. Setting it to k_scale. This only matters for FP8 Attention backends (flash-attn or flashinfer). (Worker_TP0_EP0 pid=3425910) WARNING 04-05 11:39:27 [kv_cache.py:123] Using KV cache scaling factor 1.0 for f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Look Time to Load Weights bug;help wanted ### Your current environment B200 VM ### 🐛 Describe the bug I noticed that sometimes certain ranks take a very long time to load. monkeypatched log (so it logs the load time per...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: rker_TP0_EP0 pid=3425910) WARNING 04-05 11:39:27 [kv_cache.py:123] Using KV cache scaling factor 1.0 for fp8_e4m3. If this is unintended, verify that k/v_scale scaling factors are properly set in the checkpoint. (Worker...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: EP0 pid=3425910) INFO 04-05 11:39:30 [interface.py:484] Setting kv cache block size to 32 for FLASHINFER_MLA backend. (Worker_TP2_EP2 pid=3425912) INFO 04-05 11:39:31 [interface.py:484] Setting kv cache block size to 32...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
