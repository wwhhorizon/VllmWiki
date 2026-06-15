# vllm-project/vllm#26211: [Bug]: vLLM does not support DeepSeek series on RTX PRO 6000/SM120

| 字段 | 值 |
| --- | --- |
| Issue | [#26211](https://github.com/vllm-project/vllm/issues/26211) |
| 状态 | open |
| 标签 | bug |
| 评论 | 36; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;gemm;kernel;operator |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM does not support DeepSeek series on RTX PRO 6000/SM120

### Issue 正文摘录

### Your current environment Here is my configuration information: PRETTY_NAME="Ubuntu 24.04.3 LTS" === GPU Information === index, name, compute_cap, memory.total [MiB], driver_version 0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 12.0, 97887 MiB, 580.65.06 1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 12.0, 97887 MiB, 580.65.06 2, NVIDIA RTX PRO 6000 Blackwell Server Edition, 12.0, 97887 MiB, 580.65.06 3, NVIDIA RTX PRO 6000 Blackwell Server Edition, 12.0, 97887 MiB, 580.65.06 4, NVIDIA RTX PRO 6000 Blackwell Server Edition, 12.0, 97887 MiB, 580.65.06 5, NVIDIA RTX PRO 6000 Blackwell Server Edition, 12.0, 97887 MiB, 580.65.06 6, NVIDIA RTX PRO 6000 Blackwell Server Edition, 12.0, 97887 MiB, 580.65.06 7, NVIDIA RTX PRO 6000 Blackwell Server Edition, 12.0, 97887 MiB, 580.65.06 8, NVIDIA RTX PRO 6000 Blackwell Server Edition, 12.0, 97887 MiB, 580.65.06 CUDA: 12.9 PyTorch uses https://download.pytorch.org/whl/nightly/cu130, but version 12.8 has also been tried. ### 🐛 Describe the bug Reproducing the issue on SM120: ```python llm = LLM( model="deepseek-ai/DeepSeek-V3.1", # Same applies to deepseek-ai/DeepSeek-V3.2-Exp tensor_parallel_size=8, max_model_len=4096, gpu_memory_utiliz...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: vLLM does not support DeepSeek series on RTX PRO 6000/SM120 bug ### Your current environment Here is my configuration information: PRETTY_NAME="Ubuntu 24.04.3 LTS" === GPU Information === index, name, compute_cap...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: Invalid status # At line 667 in vllm/_custom_ops.py torch.ops._C.cutlass_scaled_mm(out, a, b, scale_a, scale_b, bias) # RuntimeError: Invalid status is thrown here ``` Here are the issues I've collected, which might ser...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: GPU Information === index, name, compute_cap, memory.total [MiB], driver_version 0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 12.0, 97887 MiB, 580.65.06 1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 12.0, 97887 M...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: eries on RTX PRO 6000/SM120 bug ### Your current environment Here is my configuration information: PRETTY_NAME="Ubuntu 24.04.3 LTS" === GPU Information === index, name, compute_cap, memory.total [MiB], driver_version 0,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ensorRT-LLM/issues/5581) According to this issue, it seems that the FP8 block-scaled GEMM kernel written for SM100 does not work on RTX Pro 6000 (SM120) because SM120 is not a superset of the SM100 architecture and requ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
