# vllm-project/vllm#42839: [Bug]: P2pNcclConnector hangs in disaggregated prefill because tensor keys use engine-local request_id

| 字段 | 值 |
| --- | --- |
| Issue | [#42839](https://github.com/vllm-project/vllm/issues/42839) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: P2pNcclConnector hangs in disaggregated prefill because tensor keys use engine-local request_id

### Issue 正文摘录

### Your current environment Additional GPU info collected without `nvidia-smi`: ```text Note: this environment does not have nvidia-smi installed, so collect_env could not collect GPU model, driver, or topology through nvidia-smi. NVML driver version: 580.105.08 /proc/driver/nvidia/version: NVIDIA UNIX Open Kernel Module for x86_64 580.105.08 GPU count: 2 GPU 0: Tesla T4, 15360 MiB by NVML, 14912 MiB usable by torch, compute capability 7.5, 40 SMs, PCI bus 0000:00:04.0 GPU 1: Tesla T4, 15360 MiB by NVML, 14912 MiB usable by torch, compute capability 7.5, 40 SMs, PCI bus 0000:00:05.0 GPU topology: could not collect because nvidia-smi topo is unavailable. ``` ### 🐛 Describe the bug When running vLLM v1 disaggregated prefill with `P2pNcclConnector`, prefill completes and NCCL initializes successfully on both prefill and decode instances, but decode hangs waiting for KV and the proxy request times out. The suspected cause is that `P2pNcclConnector` uses the engine-local internal `request_id` as the cross-engine tensor key. In vLLM v1, prefill and decode are separate engine instances, so they generate different internal request IDs for the same external request. #### Relevant code In...

## 现有链接修复摘要

#42931 [Bugfix] P2pNcclConnector: use stable external_req_id as NCCL tensor key to fix disaggregated prefill hang | #44179 fix offline disaggregated prefill request ids for P2P NCCL

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: t `nvidia-smi`: ```text Note: this environment does not have nvidia-smi installed, so collect_env could not collect GPU model, driver, or topology through nvidia-smi. NVML driver version: 580.105.08 /proc/driver/nvidia/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ur current environment Additional GPU info collected without `nvidia-smi`: ```text Note: this environment does not have nvidia-smi installed, so collect_env could not collect GPU model, driver, or topology through nvidi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: -1.5B","prompt":"Hello world","max_tokens":16,"temperature":0,"stream":false}' ``` #### Observed behavior - `/v1/models` is healthy on both prefill and decode. - NCCL init succeeds on both sides. - Proxy sends the reque...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: does not have nvidia-smi installed, so collect_env could not collect GPU model, driver, or topology through nvidia-smi. NVML driver version: 580.105.08 /proc/driver/nvidia/version: NVIDIA UNIX Open Kernel Module for x86...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: P2pNcclConnector hangs in disaggregated prefill because tensor keys use engine-local request_id ### Your current environment Additional GPU info collected without `nvidia-smi`: ```text Note: this environment does...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42931](https://github.com/vllm-project/vllm/pull/42931) | closes_keyword | 0.95 | [Bugfix] P2pNcclConnector: use stable external_req_id as NCCL tensor key to fix disaggregated prefill hang | Fixes #42839. `P2pNcclConnector` hangs in disaggregated prefill because `assign_request_id()` appends an independent random suffix on each engine (`abc123-xxxx` vs `abc123-yyyy`), |
| [#44179](https://github.com/vllm-project/vllm/pull/44179) | mentioned | 0.6 | fix offline disaggregated prefill request ids for P2P NCCL | g in `P2pNcclConnector`, including work referenced in #33947, #42931, #42839, and possibly #34277, but it does not try to generalize that broader effort. - Instead, it keeps the s… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
