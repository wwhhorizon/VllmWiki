# vllm-project/vllm#21339: [Bug]: vllm crashes using Eight RTX 3090s

| 字段 | 值 |
| --- | --- |
| Issue | [#21339](https://github.com/vllm-project/vllm/issues/21339) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm crashes using Eight RTX 3090s

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have an EPYC 7282 with 128GB of RAM on a ASROCK ROME8D-2T. I am running the forbidden ‘You must call Support’ Bios of like 4.3, and I have eight RTX 3090s. - When I run vllm with four 3090s plugged into the slots directly with GEN4 x16 extenders, where the slot is set to GEN3, I load a AWQ Quat at INT4 with no issue. - When I run vllm with four 3090s plugged into X16 to x8x8 bifurcation cards, I load the same AWQ quant at INT4 with no issue. - When I run vllm with eight 3090s plugged into x16 to x8x8 bifurcation cards, I load the same AWQ quant at INT4 and it dies hard. - On CUDA12.2 with a bare metal install and VENV, vllm HARD CRASHES, and nvidia-smi shows no cards until I reboot. - On CUDA 12.6 with a bare metal install and VENV, vllm HARD CRASHES, but nvidia-smi does still show cards, but a restart is needed to make the system truly happy - Using the vllm provided container, vllm dies inside the container hard, but nvidia-smi still shows the cards, but docker is HORKED and needs a reboot. Modprobe for nvidia drm is locked. I’ve tried everything I can think of. It’s not power (as at one point I used an HP 1200W PSU for each...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ame AWQ quant at INT4 and it dies hard. - On CUDA12.2 with a bare metal install and VENV, vllm HARD CRASHES, and nvidia-smi shows no cards until I reboot. - On CUDA 12.6 with a bare metal install and VENV, vllm HARD CRA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: vllm crashes using Eight RTX 3090s bug;stale ### Your current environment ### 🐛 Describe the bug I have an EPYC 7282 with 128GB of RAM on a ASROCK ROME8D-2T. I am running the forbidden ‘You must call Support’ Bio...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: GEN4 x16 extenders, where the slot is set to GEN3, I load a AWQ Quat at INT4 with no issue. - When I run vllm with four 3090s plugged into X16 to x8x8 bifurcation cards, I load the same AWQ quant at INT4 with no issue....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e eight RTX 3090s. - When I run vllm with four 3090s plugged into the slots directly with GEN4 x16 extenders, where the slot is set to GEN3, I load a AWQ Quat at INT4 with no issue. - When I run vllm with four 3090s plu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ith vllm, and Eight RTX 3090s. Is there some magic of PCI bus I need to configure so these cards don’t step on each other? Since four cards with bifurcation slots work without an issue, I know the bifurcation cards have...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
