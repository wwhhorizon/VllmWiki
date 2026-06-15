# vllm-project/vllm#13855: [Feature]: Pin vLLM process to the right NUMA Region

| 字段 | 值 |
| --- | --- |
| Issue | [#13855](https://github.com/vllm-project/vllm/issues/13855) |
| 状态 | closed |
| 标签 | good first issue;feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Pin vLLM process to the right NUMA Region

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In DGX machines, the CPUs are typically divided into two NUMA region, for example ``` (base) ➜ ~ nvidia-smi topo -m GPU0 GPU1 GPU2 GPU3 GPU4 GPU5 GPU6 GPU7 NIC0 NIC1 NIC2 NIC3 NIC4 NIC5 NIC6 NIC7 NIC8NIC9 NIC10 NIC11 CPU Affinity NUMA Affinity GPU NUMA ID GPU0 X NV18 NV18 NV18 NV18 NV18 NV18 NV18 PXB NODE NODE NODE NODE NODE SYS SYS SYS SYS SYS SYS 0-55,112-167 0 N/A GPU1 NV18 X NV18 NV18 NV18 NV18 NV18 NV18 NODE NODE NODE PXB NODE NODE SYS SYS SYS SYS SYS SYS 0-55,112-167 0 N/A GPU2 NV18 NV18 X NV18 NV18 NV18 NV18 NV18 NODE NODE NODE NODE PXB NODE SYS SYS SYS SYS SYS SYS 0-55,112-167 0 N/A GPU3 NV18 NV18 NV18 X NV18 NV18 NV18 NV18 NODE NODE NODE NODE NODE PXB SYS SYS SYS SYS SYS SYS 0-55,112-167 0 N/A GPU4 NV18 NV18 NV18 NV18 X NV18 NV18 NV18 SYS SYS SYS SYS SYS SYS PXB NODE NODENODE NODE NODE 56-111,168-223 1 N/A GPU5 NV18 NV18 NV18 NV18 NV18 X NV18 NV18 SYS SYS SYS SYS SYS SYS NODE NODE NODEPXB NODE NODE 56-111,168-223 1 N/A GPU6 NV18 NV18 NV18 NV18 NV18 NV18 X NV18 SYS SYS SYS SYS SYS SYS NODE NODE NODENODE PXB NODE 56-111,168-223 1 N/A GPU7 NV18 NV18 NV18 NV18 NV18 NV18 NV18 X SYS SYS SYS SYS SYS SYS NODE NODE NODENODE NODE PXB 56-111,1...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: the GPU H2D and D2H performance is more predictable. I ran the following benchmark to confirm this: * 8xH100, Llama 8B, model to run on GPU 0, but setting the vLLM processes to either NUMA 0 or NUMA 1 The end result sho...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: NODENODE NODE X Legend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI) NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridge...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pically divided into two NUMA region, for example ``` (base) ➜ ~ nvidia-smi topo -m GPU0 GPU1 GPU2 GPU3 GPU4 GPU5 GPU6 GPU7 NIC0 NIC1 NIC2 NIC3 NIC4 NIC5 NIC6 NIC7 NIC8NIC9 NIC10 NIC11 CPU Affinity NUMA Affinity GPU NUM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: re predictable. I ran the following benchmark to confirm this: * 8xH100, Llama 8B, model to run on GPU 0, but setting the vLLM processes to either NUMA 0 or NUMA 1 The end result shows lower variance for the GPU0 settin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ure]: Pin vLLM process to the right NUMA Region good first issue;feature request;stale ### 🚀 The feature, motivation and pitch In DGX machines, the CPUs are typically divided into two NUMA region, for example ``` (base)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
