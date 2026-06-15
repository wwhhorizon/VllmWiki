# vllm-project/vllm#24763: [Bug]: CPU backend W8A8: AttributeError: '_OpNamespace' '_C' object has no attribute 'create_onednn_scaled_mm_handler'

| 字段 | 值 |
| --- | --- |
| Issue | [#24763](https://github.com/vllm-project/vllm/issues/24763) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPU backend W8A8: AttributeError: '_OpNamespace' '_C' object has no attribute 'create_onednn_scaled_mm_handler'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have a pure CPU build of the main branch `vllm`, following the installation in https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html to build from source (with uv). When trying to run a W8A8 quantized model (which is claimed to be supported), I get this attached error. [log.txt](https://github.com/user-attachments/files/22302534/log.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: # Your current environment ### 🐛 Describe the bug I have a pure CPU build of the main branch `vllm`, following the installation in https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html to build from sourc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: CPU backend W8A8: AttributeError: '_OpNamespace' '_C' object has no attribute 'create_onednn_scaled_mm_handler' bug ### Your current environment ### 🐛 Describe the bug I have a pure CPU build of the main branch `...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: tributeError: '_OpNamespace' '_C' object has no attribute 'create_onednn_scaled_mm_handler' bug ### Your current environment ### 🐛 Describe the bug I have a pure CPU build of the main branch `vllm`, following the instal...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: xt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tml to build from source (with uv). When trying to run a W8A8 quantized model (which is claimed to be supported), I get this attached error. [log.txt](https://github.com/user-attachments/files/22302534/log.txt) ### Befo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
