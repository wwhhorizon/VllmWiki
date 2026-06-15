# vllm-project/vllm#20757: [Bug]: Prompt Embedding returns 500 internal error for Qwen 2.5 VL model

| 字段 | 值 |
| --- | --- |
| Issue | [#20757](https://github.com/vllm-project/vllm/issues/20757) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Prompt Embedding returns 500 internal error for Qwen 2.5 VL model

### Issue 正文摘录

### Your current environment vllm: `0.9.1`: vllm command: ``` docker run --rm \ -p 8081:8081 \ -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ -e VLLM_USE_V1=0 \ --ipc=host \ --gpus '"device=1"' \ vllm/vllm-openai:v0.9.1 \ --model Qwen/Qwen2.5-VL-7B-Instruct-AWQ --port 8081 --gpu-memory-utilization 0.95 --max-model-len 8192 --limit-mm-per-prompt image=1 --limit-mm-per-prompt video=0 --task generate --enable-prompt-embeds ``` ### 🐛 Describe the bug Hello, I tried to replicate the [example of prompt embed inference](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/prompt_embed_inference_with_openai_client.py) (also the example does not write that prompt embed inference is only for v0 engine) with Qwen 2.5 VL model. But there is a: `INFO: XXXXXXXXXX - "POST /v1/completions HTTP/1.1" 500 Internal Server Error`. Here's my inference code to replicate the internal error: ```py import transformers from transformers import Qwen2_5_VLForConditionalGeneration model_name = "Qwen/Qwen2.5-VL-7B-Instruct-AWQ" tokenizer = transformers.AutoTokenizer.from_pretrained(model_name) transformers_model = Qwen2_5_VLForConditionalGeneration.from_pretrained(model_name, device_map...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: model bug ### Your current environment vllm: `0.9.1`: vllm command: ``` docker run --rm \ -p 8081:8081 \ -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ -e VLLM_USE_V1=0 \ --ipc=host \ --gpus '"device=1"' \ vllm/v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .9.1`: vllm command: ``` docker run --rm \ -p 8081:8081 \ -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ -e VLLM_USE_V1=0 \ --ipc=host \ --gpus '"device=1"' \ vllm/vllm-openai:v0.9.1 \ --model Qwen/Qwen2.5-VL-7B-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Prompt Embedding returns 500 internal error for Qwen 2.5 VL model bug ### Your current environment vllm: `0.9.1`: vllm command: ``` docker run --rm \ -p 8081:8081 \ -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nary_data = buffer.read() encoded_embeds = base64.b64encode(binary_data).decode('utf-8') completion = openai_client.completions.create( model="Qwen/Qwen2.5-VL-7B-Instruct-AWQ", # NOTE: The OpenAI client does not allow `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
