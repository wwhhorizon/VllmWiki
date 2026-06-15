# vllm-project/vllm#3828: [Bug]: no device id found when using vllm 0.4.0

| 字段 | 值 |
| --- | --- |
| Issue | [#3828](https://github.com/vllm-project/vllm/issues/3828) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: no device id found when using vllm 0.4.0

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ```text GPU Topology: GPU0 GPU1 GPU2 GPU3 NIC0 NIC1 CPU Affinity NUMA Affinity GPU NUMA ID GPU0 X NV12 SYS SYS NODE NODE 0-23 0 N/A GPU1 NV12 X SYS SYS SYS SYS 24-47 1 N/A GPU2 SYS SYS X NV12 SYS SYS 48-71 2 N/A GPU3 SYS SYS NV12 X SYS SYS 72-95 3 N/A NIC0 NODE SYS SYS SYS X NODE NIC1 NODE SYS SYS SYS NODE X Legend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI) NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node PHB = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU) PXB = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge) PIX = Connection traversing at most a single PCIe bridge NV# = Connection traversing a bonded set of # NVLinks NIC Legend: NIC0: mlx5_0 NIC1: mlx5_1 ``` ### 🐛 Describe the bug I installed vllm==0.4.0 and I am getting invalid device id. INFO 04-03 14:21:32 selector.py:21] Using XFormers backend. (RayWorkerVllm pid=74267) INFO 04-03 14:21:32 selector.py:45] Cannot use FlashAttention because the package is not...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: SYS NODE X Legend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI) NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges wit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: egend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI) NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA n...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: g invalid device id. INFO 04-03 14:21:32 selector.py:21] Using XFormers backend. (RayWorkerVllm pid=74267) INFO 04-03 14:21:32 selector.py:45] Cannot use FlashAttention because the package is not found. Please install i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: OR 04-03 14:21:32 ray_utils.py:44] _check_if_gpu_supports_dtype(self.model_config.dtype) (RayWorkerVllm pid=74267) ERROR 04-03 14:21:32 ray_utils.py:44] File "/local_disk0/.ephemeral_nfs/envs/pythonEnv-2424aae1-472c-43f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: =74267) ERROR 04-03 14:21:32 ray_utils.py:44] _check_if_gpu_supports_dtype(self.model_config.dtype) (RayWorkerVllm pid=74267) ERROR 04-03 14:21:32 ray_utils.py:44] File "/local_disk0/.ephemeral_nfs/envs/pythonEnv-2424aa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
