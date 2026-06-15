# vllm-project/vllm#17162: Error：kimi-vl：Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.

| 字段 | 值 |
| --- | --- |
| Issue | [#17162](https://github.com/vllm-project/vllm/issues/17162) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Error：kimi-vl：Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` [conda] torch 2.6.0 pypi_0 pypi [conda] torchaudio 2.6.0 pypi_0 pypi [conda] torchvision 0.21.0 pypi_0 pypi [conda] transformers 4.51.3 pypi_0 pypi [conda] triton 3.2.0 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.8.4 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 GPU1 GPU2 GPU3 GPU4 GPU5 GPU6 GPU7 NICO CPU Affinity NUMA Affinity GPU NUMA GPU0 PIX PIX PXB PXB PXB PXB PXB PXB NODE 0-23,48-71 0 N/A GPU1 PIX X PXB PXB PXB PXB PXB PXB NODE 0-23,48-71 0 N/A GPU2 PXB PXB X PXB PXB PXB PXB PXB NODE 0-23,48-71 0 N/A GPU3 PXB PXB PXB X PIX PXB PXB PXB NODE 0-23,48-71 0 N/A GPU4 PXB PXB PXB PXB X PXB PXB PXB NODE 0-23,48-71 0 N/A GPU5 PXB PXB PXB PXB PXB X PXB PXB NODE 0-23,48-71 0 N/A GPU6 PXB PXB PXB PXB PXB PXB X PXB NODE 0-23,48-71 0 N/A GPU7 PXB PXB PXB PXB PXB PXB PXB X NODE 0-23,48-71 0 N/A NICO NODE NODE NODE NODE NODE NODE NODE NODE X 0 N/A Legend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI) NODE = Connection traversing PCIe as well as the interconnect betwee...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: nda] triton 3.2.0 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.8.4 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 GPU1 GPU2 GPU3 GPU4 GP...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: i [conda] triton 3.2.0 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.8.4 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 GPU1 GPU2 GPU3 GP...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ] transformers 4.51.3 pypi_0 pypi [conda] triton 3.2.0 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.8.4 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: cesses, shutting down. See stack trace above for root cause issue. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` [conda] torch 2.6.0 pypi_0 pypi [conda] torchaudio 2.6.0 pypi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: r is prompted. The final installed version is 0.8.4. Can I install the latest code using the source code? ![Image](https://github.com/user-attachments/assets/45e3425a-62fe-4f6c-a31f-9ce1931e9896) Directly running kimi-v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
