# vllm-project/vllm#16019: [New Model]:  support for fashion-clip

| 字段 | 值 |
| --- | --- |
| Issue | [#16019](https://github.com/vllm-project/vllm/issues/16019) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]:  support for fashion-clip

### Issue 正文摘录

### The model to consider. [This](https://huggingface.co/patrickjohncyh/fashion-clip) model is based on the CLIP architecture, which is popular for image-text tasks. ### The closest model vllm already supports. Transformers model ### What's your difficulty of supporting the model you want? When I tried evaluating the model, I got the error Code ``` from vllm import LLM import torch from PIL import Image from transformers import CLIPProcessor # Load the model llm = LLM(model="patrickjohncyh/fashion-clip") # Load and preprocess the image image = Image.open("/Users/pkumari/Downloads/monitor.png") processor = CLIPProcessor.from_pretrained("patrickjohncyh/fashion-clip") inputs = processor(images=image, return_tensors="pt") # Generate embeddings outputs = llm.generate({ "prompt": " ", "multi_modal_data": {"image": inputs['pixel_values']}, }) # Print the embeddings print(outputs) ``` Error ``` [rank0]: ValueError: CLIPModel has no vLLM implementation and the Transformers implementation is not compatible with vLLM. Try setting VLLM_USE_V1=0. (search-eval) pkumari@GF4MX6XF00 search-eval % pip list ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant is...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: support for fashion-clip new-model;stale ### The model to consider. [This](https://huggingface.co/patrickjohncyh/fashion-clip) model is based on the CLIP architecture, which is popular for image-text tasks....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: # What's your difficulty of supporting the model you want? When I tried evaluating the model, I got the error Code ``` from vllm import LLM import torch from PIL import Image from transformers import CLIPProcessor # Loa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: When I tried evaluating the model, I got the error Code ``` from vllm import LLM import torch from PIL import Image from transformers import CLIPProcessor # Load the model llm = LLM(model="patrickjohncyh/fashion-clip")...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /huggingface.co/patrickjohncyh/fashion-clip) model is based on the CLIP architecture, which is popular for image-text tasks. ### The closest model vllm already supports. Transformers model ### What's your difficulty of...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: support for fashion-clip new-model;stale ### The model to consider. [This](https://huggingface.co/patrickjohncyh/fashion-clip) model is based on the CLIP architecture, which is popular for image-text tasks....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
