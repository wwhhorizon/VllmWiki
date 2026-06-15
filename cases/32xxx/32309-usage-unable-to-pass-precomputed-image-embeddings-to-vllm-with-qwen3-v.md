# vllm-project/vllm#32309: [Usage]: Unable to pass precomputed image embeddings to vLLM with Qwen3-VL

| 字段 | 值 |
| --- | --- |
| Issue | [#32309](https://github.com/vllm-project/vllm/issues/32309) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Unable to pass precomputed image embeddings to vLLM with Qwen3-VL

### Issue 正文摘录

Hi. I try to pass multiple image embeddings to Qwen3-VL via the OpenAI-compatible API in vLLM, however it does not seem to work, regardless of format. Single-image embedding works correctly, but as soon as a second embedding is included, vLLM either rejects the request or crashes internally. My code: ``` import torch from openai import OpenAI import base64 import io def inference_with_vllm_embeds(): client = OpenAI( base_url="http://localhost:8001/v1", api_key="EMPTY", ) model = client.models.list().data[0].id prompt = "OCR:" image_embedding = torch.zeros((220, 8192)) # two_image_embeddings = torch.stack([image_embedding, image_embedding]) # two_image_embeddings = two_image_embeddings.view(-1, 8192) two_image_embeddings = torch.concatenate([image_embedding, image_embedding], dim=0) buffer = io.BytesIO() torch.save(two_image_embeddings, buffer) buffer.seek(0) binary_data = buffer.read() base64_image_embedding = base64.b64encode(binary_data).decode('utf-8') thw_embedding = torch.tensor([[1, 22, 40]]) two_thw_embeddings = torch.stack([thw_embedding, thw_embedding]) buffer = io.BytesIO() torch.save(two_thw_embeddings, buffer) buffer.seek(0) binary_data = buffer.read() base64_image_gri...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Unable to pass precomputed image embeddings to vLLM with Qwen3-VL usage Hi. I try to pass multiple image embeddings to Qwen3-VL via the OpenAI-compatible API in vLLM, however it does not seem to work, regardles...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: , but as soon as a second embedding is included, vLLM either rejects the request or crashes internally. My code: ``` import torch from openai import OpenAI import base64 import io def inference_with_vllm_embeds(): clien...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ed, vLLM either rejects the request or crashes internally. My code: ``` import torch from openai import OpenAI import base64 import io def inference_with_vllm_embeds(): client = OpenAI( base_url="http://localhost:8001/v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 203 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
