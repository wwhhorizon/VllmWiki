# vllm-project/vllm#25623: [Bug]: torch.compile padding causes IMA on Hopper + DBO

| 字段 | 值 |
| --- | --- |
| Issue | [#25623](https://github.com/vllm-project/vllm/issues/25623) |
| 状态 | open |
| 标签 | bug;help wanted;torch.compile;unstale |
| 评论 | 40; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: torch.compile padding causes IMA on Hopper + DBO

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug torch.compile generated padding kernel causes an Illegal Memory Access when padding inouts to block-quantized fp8 cutlass kernels on Hopper and DBO enabled. This bug was introduced in #24666, with the revert in #25607, and the reapply with padding wrapped in #25696. ``` ^[[1;36m(APIServer pid=1)^[[0;0m ^[[1;36m(EngineCore_DP0 pid=276)^[[0;0m ERROR 09-24 13:00:49 [core.py:708] RuntimeError: Failed: CUDA error /tmp/deepep/csrc/kernels/internode_ll.cu:391 'an illegal memory access was encountered' ``` ### Minimal Repro instructions: Credit to @ElizaWszola for finding this smaller repro. ``` VLLM_USE_DEEP_GEMM=0 VLLM_ALL2ALL_BACKEND=deepep_low_latency vllm serve \ Qwen/Qwen3-30B-A3B-FP8 \ --port 7557 \ --disable-uvicorn-access-log \ --trust-remote-code \ --enable-expert-parallel \ --data-parallel-hybrid-lb \ --tensor-parallel-size 2 \ --data-parallel-size 2 \ --data-parallel-size-local 2 \ --data-parallel-address localhost \ --data-parallel-rpc-port 5555 \ --data-parallel-start-rank 0 \ --enable-eplb \ --eplb-config '{"window_size":"1000", "step_interval":"3000", "num_redundant_experts":"32", "log_balancedness":"False"}' \ --enable-d...

## 现有链接修复摘要

#24666 [Performance] Move apply_w8a8_block_fp8_linear to an op class | #25607 Revert "[Performance] Move apply_w8a8_block_fp8_linear to an op class… | #25696 [Perf] Fix and reapply move apply w8a8 block fp8 linear to class | #28580 [torch.compile] Try using Dynamo-native padding

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: torch.compile padding causes IMA on Hopper + DBO bug;help wanted;torch.compile;unstale ### Your current environment ### 🐛 Describe the bug torch.compile generated padding kernel causes an Illegal Memory Access wh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: torch.compile padding causes IMA on Hopper + DBO bug;help wanted;torch.compile;unstale ### Your current environment ### 🐛 Describe the bug torch.compile generated padding kernel causes an Illegal Memory Access wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uses an Illegal Memory Access when padding inouts to block-quantized fp8 cutlass kernels on Hopper and DBO enabled. This bug was introduced in #24666, with the revert in #25607, and the reapply with padding wrapped in #...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ding kernel causes an Illegal Memory Access when padding inouts to block-quantized fp8 cutlass kernels on Hopper and DBO enabled. This bug was introduced in #24666, with the revert in #25607, and the reapply with paddin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ed padding kernel causes an Illegal Memory Access when padding inouts to block-quantized fp8 cutlass kernels on Hopper and DBO enabled. This bug was introduced in #24666, with the revert in #25607, and the reapply with...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24666](https://github.com/vllm-project/vllm/pull/24666) | mentioned | 0.45 | [Performance] Move apply_w8a8_block_fp8_linear to an op class | cutlass kernels on hopper and dbo enabled. this bug was introduced in #24666, with the revert in #25607, and the reapply with padding wrapped in #25696. ``` ^[[1;36m(apiserver pid… |
| [#25607](https://github.com/vllm-project/vllm/pull/25607) | mentioned | 0.6 | Revert "[Performance] Move apply_w8a8_block_fp8_linear to an op class… | Move apply_w8a8_block_fp8_linear to an op class… Revert #24666 due to #25623, reapplied in #25696. This reverts commit 63400259d05485330fb23635af892b3fce160dea. That commit is cau… |
| [#25696](https://github.com/vllm-project/vllm/pull/25696) | closes_keyword | 0.95 | [Perf] Fix and reapply move apply w8a8 block fp8 linear to class | resolves the issue (#25623) raised in https://github.com/vllm-project/vllm/pull/25607 by using a single padding-cutlass custom op on Hopper. We are waiting to merge this after v0. |
| [#28580](https://github.com/vllm-project/vllm/pull/28580) | mentioned | 0.6 | [torch.compile] Try using Dynamo-native padding | ive padding ## Purpose Reapply padding from #24666, which caused bug #25623. Currently fails with different error due to torch==2.9 (works with torch==2.8): ``` VLLM_USE_DEEP_GEMM… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
