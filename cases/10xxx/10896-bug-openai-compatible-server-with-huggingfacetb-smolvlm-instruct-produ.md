# vllm-project/vllm#10896: [Bug]: Openai compatible server with HuggingFaceTB/SmolVLM-Instruct producing smaller outputs than expected

| 字段 | 值 |
| --- | --- |
| Issue | [#10896](https://github.com/vllm-project/vllm/issues/10896) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Openai compatible server with HuggingFaceTB/SmolVLM-Instruct producing smaller outputs than expected

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The openai compatible server with smovlm producing smaller prompt outputs than directly using smolvlm. **Smolvlm code:** ``` from transformers import AutoProcessor, AutoModelForVision2Seq import torch from PIL import Image from transformers.image_utils import load_image DEVICE = "cuda" if torch.cuda.is_available() else "cpu" processor = AutoProcessor.from_pretrained("HuggingFaceTB/SmolVLM-Instruct") model = AutoModelForVision2Seq.from_pretrained("HuggingFaceTB/SmolVLM-Instruct", torch_dtype=torch.bfloat16, _attn_implementation="flash_attention_2" if DEVICE == "cuda" else "eager").to(DEVICE) # Load images image1 = load_image("https://huggingface.co/spaces/HuggingFaceTB/SmolVLM/resolve/main/example_images/rococo.jpg") detailed_prompt = """You are an expert image captioner. Please provide a detailed description of the image that covers: Main subjects and their characteristics Background elements and setting Colors, lighting, and atmosphere Notable details or unique features Spatial relationships between elements Overall mood or impression Your description should be at least 100 words long and cove...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Openai compatible server with HuggingFaceTB/SmolVLM-Instruct producing smaller outputs than expected bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The openai compatib...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Openai compatible server with HuggingFaceTB/SmolVLM-Instruct producing smaller outputs than expected bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The openai compatib...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: SmolVLM-Instruct", torch_dtype=torch.bfloat16, _attn_implementation="flash_attention_2" if DEVICE == "cuda" else "eager").to(DEVICE) # Load images image1 = load_image("https://huggingface.co/space
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Openai compatible server with HuggingFaceTB/SmolVLM-Instruct producing smaller outputs than expected bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The openai compatib...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: esolve/main/example_images/rococo.jpg") detailed_prompt = """You are an expert image captioner. Please provide a detailed description of the image that covers: Main subjects and their characteristics Background elements...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
