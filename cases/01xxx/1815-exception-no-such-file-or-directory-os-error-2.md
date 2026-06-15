# vllm-project/vllm#1815: Exception: No such file or directory (os error 2)

| 字段 | 值 |
| --- | --- |
| Issue | [#1815](https://github.com/vllm-project/vllm/issues/1815) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Exception: No such file or directory (os error 2)

### Issue 正文摘录

I lost hope ... I am trying to inference an AWQ model from the block. I have already search on the issue pages and tryied several things without success. OS: Linux +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.129.03 Driver Version: 535.129.03 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 NVIDIA GeForce RTX 2070 ... Off | 00000000:08:00.0 On | N/A | | 24% 28C P8 18W / 235W | 745MiB / 8192MiB | 7% Default | | | | N/A | +-----------------------------------------+----------------------+----------------------+ As you can see i have cuda 12.2 installed at sys level. I have created a fresh venv, python 3.10.13, and i have installed vllm via pip directly as well by compailing from source. Both scenarios error: cmd: python -m vllm.entrypoints.api_server --model TheBloke/samantha-mistral-7B-AWQ --quantization awq --dtype half...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ----------------------------+ | NVIDIA-SMI 535.129.03 Driver Version: 535.129.03 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: r directory (os error 2) I lost hope ... I am trying to inference an AWQ model from the block. I have already search on the issue pages and tryied several things without success. OS: Linux +-----------------------------...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: . I am trying to inference an AWQ model from the block. I have already search on the issue pages and tryied several things without success. OS: Linux +--------------------------------------------------------------------...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: m vllm.entrypoints.api_server --model TheBloke/samantha-mistral-7B-AWQ --quantization awq --dtype half ``` WARNING 11-28 15:30:19 config.py:140] awq quantization is not fully optimized yet. The speed can be slower than...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: error 2) I lost hope ... I am trying to inference an AWQ model from the block. I have already search on the issue pages and tryied several things without success. OS: Linux +---------------------------------------------...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
