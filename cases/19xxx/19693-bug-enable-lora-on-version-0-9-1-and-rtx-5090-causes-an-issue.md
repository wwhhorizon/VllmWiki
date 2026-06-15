# vllm-project/vllm#19693: [Bug]: Enable LORA on Version 0.9.1 and RTX 5090 causes an issue

| 字段 | 值 |
| --- | --- |
| Issue | [#19693](https://github.com/vllm-project/vllm/issues/19693) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | edge_case |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Enable LORA on Version 0.9.1 and RTX 5090 causes an issue

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Okay so when i run the above command without --enable-lora `vllm serve models/Llama-3.1-8B --max-model-len 9000 --quantization bitsandbytes --load-format bitsandbytes --enable-lora ` with any configuration it works Once **--enable-lora** is added it goes crazy with this error Note: it's not related to me providing a lora adapters to it, because i did using: ` --lora-modules adapter_name=adapter_path` gives the. same issue too Update: Added --enforce-eager now it can't see the kernel image at all Error: torch.AcceleratorError: CUDA error: no kernel image is available for execution on the device ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Enable LORA on Version 0.9.1 and RTX 5090 causes an issue bug;stale ### Your current environment ### 🐛 Describe the bug Okay so when i run the above command without --enable-lora `vllm serve models/Llama-3.1-8B -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Enable LORA on Version 0.9.1 and RTX 5090 causes an issue bug;stale ### Your current environment ### 🐛 Describe the bug Okay so when i run the above command without --enable-lora `vllm serve models/Llama-3.1-8B -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Okay so when i run the above command without --enable-lora `vllm serve models/Llama-3.1-8B --max-model-len 9000 --quantization bitsandbytes --load-format bitsandbytes --enable-lora ` with any configuration it works Once...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: out --enable-lora `vllm serve models/Llama-3.1-8B --max-model-len 9000 --quantization bitsandbytes --load-format bitsandbytes --enable-lora ` with any configuration it works Once **--enable-lora** is added it goes crazy...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ntion;cache;cuda;kernel;operator;quantization;sampling build_error;crash;mismatch;slowdown dtype;env_dependency;memory_layout;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
