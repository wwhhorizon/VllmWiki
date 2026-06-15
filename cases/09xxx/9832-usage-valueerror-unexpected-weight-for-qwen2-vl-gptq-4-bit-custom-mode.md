# vllm-project/vllm#9832: [Usage]: ValueError: Unexpected weight for Qwen2-VL GPTQ 4-bit custom model.

| 字段 | 值 |
| --- | --- |
| Issue | [#9832](https://github.com/vllm-project/vllm/issues/9832) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization;sampling;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: ValueError: Unexpected weight for Qwen2-VL GPTQ 4-bit custom model.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` WARNING 10-30 12:11:37 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Microsoft Windows 11 Home Single Language GCC version: Could not collect Clang version: Could not collect CMake version: Could not collect Libc version: N/A Python version: 3.10.0 (tags/v3.10.0:b494f59, Oct 4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] (64-bit runtime) Python platform: Windows-10-10.0.22631-SP0 Is CUDA available: False CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA GeForce RTX 2060 Nvidia driver version: 565.90 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture=9 CurrentClockSpeed=2900 DeviceID=CPU0 Family=107 L2CacheSize=4096 L2CacheSpeed= Manufacturer=AuthenticAMD MaxClockSpeed=2900 Name=AMD Ryzen 7 4800H with Radeon Graphics ProcessorType=3 Revision=24577 Versions of relevant libraries: [pip3] numpy...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 10: [Usage]: ValueError: Unexpected weight for Qwen2-VL GPTQ 4-bit custom model. usage ### Your current environment ```text The output of `python collect_env.py` WARNING 10-30 12:11:37 _custom_ops.py:19] Failed to import fr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: hon collect_env.py` WARNING 10-30 12:11:37 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: odule named 'vllm._C'") PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Microsoft Windows 11 Home Single Language GCC version: Could not...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: LM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'GraniteForCausalLM',...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.46.1 [pip3] triton==3.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.3 vLLM Build Flags: CUDA Archs:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
