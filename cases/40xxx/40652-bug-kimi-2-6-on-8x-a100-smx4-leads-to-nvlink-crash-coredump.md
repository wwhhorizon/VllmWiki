# vllm-project/vllm#40652: [Bug]: Kimi 2.6 on 8x A100 SMX4 leads to NVLink Crash Coredump

| 字段 | 值 |
| --- | --- |
| Issue | [#40652](https://github.com/vllm-project/vllm/issues/40652) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;fp8;kernel;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Kimi 2.6 on 8x A100 SMX4 leads to NVLink Crash Coredump

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are running vLLM on a Talos OS v1.12.6 Bare Metal Environment with 8x A100 SMX4 with NVLink. Loading of the Kimi 2.6 models breaks the GPUS and NVLinks with heavy impact. Highlight Kernel Logs (all logs below): `````` 192.168.11.119: kern: warning: [2026-04-22T21:25:20.458998481Z]: NVRM: GPU at PCI:0000:48:00: GPU-5fc0bcec-c2e1-38dc-8994-2a9f9f3b709e 192.168.11.119: kern: err: [2026-04-22T21:25:20.466440686Z]: nvidia-nvswitch1: SXid (PCI:0000:aa:00.0): 24007, Severity 1 Engine instance 12 Sub-engine instance 00 192.168.11.119: kern: warning: [2026-04-22T21:25:20.473962892Z]: NVRM: GPU Board Serial Number: 1563521020414 192.168.11.119: kern: err: [2026-04-22T21:25:20.500049682Z]: nvidia-nvswitch1: SXid (PCI:0000:aa:00.0): 24007, Data {0x10000000, 0x10008100, 0x10000000, 0x10008100, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000} 192.168.11.119: kern: warning: [2026-04-22T21:25:20.505406921Z]: NVRM: Xid (PCI:0000:48:00): 62, 00002740 00002b08 00001126 0000117a 0000279f 0002a91a 00000011 00000000 192.168.11.119: kern: warning: [2026-04-22T21:25:20.560106789Z]: NVRM: Xid (PCI:0000:48:00): 45, pid=22884, name=VLLM::Work...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Kimi 2.6 on 8x A100 SMX4 leads to NVLink Crash Coredump bug ### Your current environment ### 🐛 Describe the bug We are running vLLM on a Talos OS v1.12.6 Bare Metal Environment with 8x A100 SMX4 with NVLink. Load...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Kimi 2.6 on 8x A100 SMX4 leads to NVLink Crash Coredump bug ### Your current environment ### 🐛 Describe the bug We are running vLLM on a Talos OS v1.12.6 Bare Metal Environment with 8x A100 SMX4 with NVLink. Load...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ions. performance attention_kv_cache;ci_build;frontend_api;model_support;quantization cache;cuda;fp8;kernel;quantization build_error;crash dtype;env_dependency;memory_layout Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Metal Environment with 8x A100 SMX4 with NVLink. Loading of the Kimi 2.6 models breaks the GPUS and NVLinks with heavy impact. Highlight Kernel Logs (all logs below): `````` 192.168.11.119: kern: warning: [2026-04-22T21...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: da;fp8;kernel;quantization build_error;crash dtype;env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
