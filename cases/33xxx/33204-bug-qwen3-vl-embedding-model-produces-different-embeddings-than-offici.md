# vllm-project/vllm#33204: [Bug]: Qwen3-VL-Embedding model produces different embeddings than official qwen_vl_utils implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#33204](https://github.com/vllm-project/vllm/issues/33204) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | gemm;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-Embedding model produces different embeddings than official qwen_vl_utils implementation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary When using `Qwen/Qwen3-VL-Embedding-8B` with vLLM's pooling runner, the generated embeddings differ significantly from the official implementation using `qwen_vl_utils`, resulting in ~0.92 cosine similarity instead of 1.0 for identical video inputs. ## Environment - **vLLM version:** v0.14.0 - **Model:** `Qwen/Qwen3-VL-Embedding-8B` - **Hardware:** NVIDIA A100 80GB - **OS:** Ubuntu 22.04 ## Setup ### vLLM Server Configuration ```bash python3 -m vllm.entrypoints.openai.api_server \ --port 8080 \ --model Qwen/Qwen3-VL-Embedding-8B \ --served-model-name Qwen3VL-Embedding-8B \ --runner pooling \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.90 \ --trust-remote-code \ --max-model-len 8192 \ --mm-processor-kwargs '{"fps": 2.0, "max_frames": 64}' \ --pooler-config '{"pooling_type": "LAST", "normalize": true}' ``` ### Official Implementation (qwen_vl_utils) ```python from qwen_vl_utils import process_vision_info from transformers import Qwen2VLForConditionalGeneration, AutoProcessor model = Qwen2VLForConditionalGeneration.from_pretrained( "Qwen/Qwen3-VL-Embedding-8B", torch_dtype=torch.bfloat16 ) processor = AutoProces...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Qwen3-VL-Embedding model produces different embeddings than official qwen_vl_utils implementation bug;unstale ### Your current environment ### 🐛 Describe the bug ## Summary When using `Qwen/Qwen3-VL-Embedding-8B`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Qwen3-VL-Embedding model produces different embeddings than official qwen_vl_utils implementation bug;unstale ### Your current environment ### 🐛 Describe the bug ## Summary When using `Qwen/Qwen3-VL-Embedding-8B`...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: lGeneration.from_pretrained( "Qwen/Qwen3-VL-Embedding-8B", torch_dtype=torch.bfloat16 ) processor = AutoProcessor.from_pretrained( "Qwen/Qwen3-VL-Embedding-8B", min_pixels=256*28*28, max_pixels=1280*28*28 ) messages = [...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: v0.14.0 - **Model:** `Qwen/Qwen3-VL-Embedding-8B` - **Hardware:** NVIDIA A100 80GB - **OS:** Ubuntu 22.04 ## Setup ### vLLM Server Configuration ```bash python3 -m vllm.entrypoints.openai.api_server \ --port 8080 \ --mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: es different embeddings than official qwen_vl_utils implementation bug;unstale ### Your current environment ### 🐛 Describe the bug ## Summary When using `Qwen/Qwen3-VL-Embedding-8B` with vLLM's pooling runner, the gener...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
