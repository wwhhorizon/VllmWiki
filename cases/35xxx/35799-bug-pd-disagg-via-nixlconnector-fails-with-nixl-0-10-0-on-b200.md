# vllm-project/vllm#35799: [Bug] PD disagg via NixlConnector fails with NIXL 0.10.0 on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#35799](https://github.com/vllm-project/vllm/issues/35799) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] PD disagg via NixlConnector fails with NIXL 0.10.0 on B200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary PD disagg via NixlConnector fails with NIXL 0.10.0 - UCX selects RDMA (rc_mlx5) instead of NVLink (cuda_ipc) for intra-node transfers. Reproduction script and all logs: [gist](https://gist.github.com/ZhanqiuHu/f1a0630b537eb4321586639286f2b2fe). ## Context PR #35495 already pins `nixl < 0.10.0` as a workaround. This issue documents the root cause with UCX transport logs. ## Bug description PD disaggregation via `NixlConnector` fails on B200 with NIXL 0.10.0 but works with earlier versions. The root cause is a **UCX transport selection regression in NIXL 0.10.0** — UCX now prefers `rc_mlx5` (RDMA over ConnectX NIC) over `cuda_ipc` (NVLink) for intra-node VRAM-to-VRAM transfers on machines where RDMA is available. | Hardware | GPU pair | NUMA | RDMA available | UCX transport chosen | PD result | |----------|----------|------|----------------|---------------------|-----------| | H100 | 6→2 | same | No (`rdma_create_event_channel failed`) | `tcp` + `cuda_ipc` | **Works** | | B200 | 6→7 | same | Yes | `rc_mlx5` | **Works** | | B200 | 6→1 | cross | Yes | `rc_mlx5` (`cuda_ipc` briefly appears then drops) | **Fails** | On H100,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nnector fails with NIXL 0.10.0 - UCX selects RDMA (rc_mlx5) instead of NVLink (cuda_ipc) for intra-node transfers. Reproduction script and all logs: [gist](https://gist.github.com/ZhanqiuHu/f1a0630b537eb4321586639286f2b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug] PD disagg via NixlConnector fails with NIXL 0.10.0 on B200 bug ### Your current environment ### 🐛 Describe the bug ## Summary PD disagg via NixlConnector fails with NIXL 0.10.0 - UCX selects RDMA (rc_mlx5) instead...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: X_LOG_FILE` and inspecting the `cfg#` lines from `ucp_worker.c`. **H100 decode server (GPU 6→2, works):** ([full log](https://gist.github.com/ZhanqiuHu/f1a0630b537eb4321586639286f2b2fe#file-h100_ucx_decode_gpu6_2-log))...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ted) to force NVLink path ## Suggested fix (in NIXL) NIXL 0.10.0's UCX backend should prefer `cuda_ipc` for intra-node VRAM-to-VRAM transfers, regardless of RDMA availability. The UCX transport selection heuristic chang...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
