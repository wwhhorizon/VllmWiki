# vllm-project/vllm#32353: [Bug]: Nemotron-3-Nano is broken when using TRTLLM attention on Blackwell

| 字段 | 值 |
| --- | --- |
| Issue | [#32353](https://github.com/vllm-project/vllm/issues/32353) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;hardware_porting |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Nemotron-3-Nano is broken when using TRTLLM attention on Blackwell

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It seems that adding this `is_strictly_contiguous` check has broken Nemotron-3-Nano on Blackwell https://github.com/vllm-project/vllm/pull/32008 ``` vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 --trust-remote-code ... (EngineCore_DP0 pid=327429) WARNING 01-14 16:23:26 [flashinfer.py:380] Using TRTLLM prefill attention (auto-detected). Capturing CUDA graphs (decode, FULL): 98%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▉ | 50/51 [00:03<00:00, 13.40it/s] (EngineCore_DP0 pid=327429) ERROR 01-14 16:23:30 [core.py:936] EngineCore failed to start. (EngineCore_DP0 pid=327429) ERROR 01-14 16:23:30 [core.py:936] Traceback (most recent call last): ... (EngineCore_DP0 pid=327429) ERROR 01-14 16:23:30 [core.py:936] File "/home/mgoin/code/vllm/vllm/v1/attention/backends/flashinfer.py", line 1507, in forward (EngineCore_DP0 pid=327429) ERROR 01-14 16:23:30 [core.py:936] assert is_strictly_contiguous(decode_query) ``` When I disable trtllm attn with `--attention-config.use_trtllm_attention=0` it works fine ### Before submitting...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Nemotron-3-Nano is broken when using TRTLLM attention on Blackwell bug ### Your current environment ### 🐛 Describe the bug It seems that adding this `is_strictly_contiguous` check has broken Nemotron-3-Nano on Bl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rust-remote-code ... (EngineCore_DP0 pid=327429) WARNING 01-14 16:23:26 [flashinfer.py:380] Using TRTLLM prefill attention (auto-detected). Capturing CUDA graphs (decode, FULL): 98%|█████████████████████████████████████...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ct/vllm/pull/32008 ``` vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 --trust-remote-code ... (EngineCore_DP0 pid=327429) WARNING 01-14 16:23:26 [flashinfer.py:380] Using TRTLLM prefill attention (auto-detected)....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: _DP0 pid=327429) WARNING 01-14 16:23:26 [flashinfer.py:380] Using TRTLLM prefill attention (auto-detected). Capturing CUDA graphs (decode, FULL): 98%|█████████████████████████████████████████████████████████████████████...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pment attention_kv_cache;hardware_porting attention;cuda crash dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
