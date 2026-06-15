# vllm-project/vllm#40466: [Bug]: Streaming output incorrectly mapped to `reasoning` field instead of `content` when `enable_thinking=False`

| 字段 | 值 |
| --- | --- |
| Issue | [#40466](https://github.com/vllm-project/vllm/issues/40466) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Streaming output incorrectly mapped to `reasoning` field instead of `content` when `enable_thinking=False`

### Issue 正文摘录

### Your current environment ============================== vLLM Info ============================== ROCM Version : Could not collect vLLM Version : 0.11.1rc6.dev157+g3755c1453 (git sha: 3755c1453) vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; XPU: Disabled GPU Topology: GPU0 GPU1 CPU Affinity NUMA Affinity GPU NUMA ID GPU0 X SYS 0-27,56-83 0 N/A GPU1 SYS X 28-55,84-111 1 N/A Legend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI) NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node PHB = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU) PXB = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge) PIX = Connection traversing at most a single PCIe bridge NV# = Connection traversing a bonded set of # NVLinks ### 🐛 Describe the bug ### 🐛 Describe the bug When starting the `vllm/vllm-openai:nightly` server **without** enabling tool calling arguments at startup, and passing `chat_template_kwargs={"enable_thinking": False}` via the client to explicitly disable reasoning, the streaming output (`stream=True`)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ================= vLLM Info ============================== ROCM Version : Could not collect vLLM Version : 0.11.1rc6.dev157+g3755c1453 (git sha: 3755c1453) vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; XPU: Dis...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ====================== vLLM Info ============================== ROCM Version : Could not collect vLLM Version : 0.11.1rc6.dev157+g3755c1453 (git sha: 3755c1453) vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; XPU...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: mapped to `reasoning` field instead of `content` when `enable_thinking=False` bug ### Your current environment ============================== vLLM Info ============================== ROCM Version : Could not collect vLL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: reasoning` field instead of the `content` field. **Observed chunk delta format:** ```text {'role': 'assistant', 'content': ''} {'reasoning': 'Hello'} {'reasoning': '! How can'} {'reasoning': ' I assist'} {'reasoning': '...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: parser` flags in the Docker run command). - `stream=True` is used in the request. - `chat_template_kwargs={"enable_thinking": False}` is passed in the request body. **Conditions where it works CORRECTLY:** 1. **Non-stre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
