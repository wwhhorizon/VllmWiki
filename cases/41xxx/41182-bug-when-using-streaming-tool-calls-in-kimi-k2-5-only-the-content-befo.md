# vllm-project/vllm#41182: [Bug]: When using streaming tool calls in kimi-k2.5, only the content before the tool call can be obtained

| 字段 | 值 |
| --- | --- |
| Issue | [#41182](https://github.com/vllm-project/vllm/issues/41182) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When using streaming tool calls in kimi-k2.5, only the content before the tool call can be obtained

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I deployed kimi-k2.5 in a dual-machine setup using v0.18.0, its streaming return only included the content before the tool call, and the subsequent content was not returned until stop_reason:'length'. When checking the debug logs, the delta_text printed by the tool parser can be concatenated into a complete content, but the characters between and exceed thirty thousand, and it almost always prints 'Not enough token', yet none of the content is returned. The configuration and some results will be provided later. ---------------------------------------------------------configuration---------------------------------------------------- export HCCL_IF_IP= export GLOO_SOCKET_IFNAME="bond0" export TP_SOCKET_IFNAME="bond0" export HCCL_SOCKET_IFNAME="bond0" export HCCL_INTRA_PCIE_ENABLE=1 export HCCL_INTRA_ROCE_ENABLE=0 export OMP_PROC_BIND=false export OMP_NUM_THREADS=5 export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True" export VLLM_USE_V1=1 export HCCL_BUFFSIZE=1024 echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor sysctl -w vm.swappiness=0 sysctl -w k...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ns 8192 \ --gpu-memory-utilization 0.9 \ --compilation-config '{"cudagraph_capture_sizes":[1,2,4,8,16,32,64,128,196], "cudagraph_mode":"FULL_DECODE_ONLY"}' \ --additional-config '{"multistream_overlap_shared_expert":tru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ways prints 'Not enough token', yet none of the content is returned. The configuration and some results will be provided later. ---------------------------------------------------------configuration---------------------...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: CKET_IFNAME="bond0" export HCCL_SOCKET_IFNAME="bond0" export HCCL_INTRA_PCIE_ENABLE=1 export HCCL_INTRA_ROCE_ENABLE=0 export OMP_PROC_BIND=false export OMP_NUM_THREADS=5 export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: --served-model-name kimi_k2.5 \ --allowed-local-media-path / \ --quantization ascend \ --trust-remote-code \ --tensor-parallel-size 8 \ --data-parallel-size 2 \ --data-parallel-size-local 1 \ --data-parallel-start-rank...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: TRA_PCIE_ENABLE=1 export HCCL_INTRA_ROCE_ENABLE=0 export OMP_PROC_BIND=false export OMP_NUM_THREADS=5 export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True" export VLLM...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
