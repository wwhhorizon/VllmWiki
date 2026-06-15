# vllm-project/vllm#10084: [Usage]: Sending in pre-tokenized question during inference doesn't seem any faster than raw text.  

| 字段 | 值 |
| --- | --- |
| Issue | [#10084](https://github.com/vllm-project/vllm/issues/10084) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Sending in pre-tokenized question during inference doesn't seem any faster than raw text.  

### Issue 正文摘录

### Your current environment ```text I'm running some tests to see if my use case would benefit from tokenizing my context before sending it in as I want to re-use my same context possibly hundreds of times. So I ran a simple test case where I first ran the same context and question 5000 times with raw text and then ran that same API call with just the tokenized version of the context and question. I'm getting roughly ~1,900 tokens/s and my context+question are 1,132 Tokens. My response tokens are very short with just a Json respons of {"Category": [{"AI_Found": "No"}]}. From the 5,000 consecutive test runs, this is the times I received. Raw Text Time taken: 49:46.963 Tokenized Text Time taken: 49:45.073 I'm running the latest version of vllm. Here is my Docker run code: docker run --gpus all --env CUDA_VISIBLE_DEVICES=1\ --env CUDA_DEVICE_ORDER=PCI_BUS_ID \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN=*******" \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model neuralmagic/Mistral-Nemo-Instruct-2407-FP8 \ --max-model-len 5000 \ --gpu-memory-utilization 0.98 I'm running my API calls against v1/completions and only sending the below b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: es with raw text and then ran that same API call with just the tokenized version of the context and question. I'm getting roughly ~1,900 tokens/s and my context+question are 1,132 Tokens. My response tokens are very sho...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rsion of vllm. Here is my Docker run code: docker run --gpus all --env CUDA_VISIBLE_DEVICES=1\ --env CUDA_DEVICE_ORDER=PCI_BUS_ID \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN=******...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: IBLE_DEVICES=1\ --env CUDA_DEVICE_ORDER=PCI_BUS_ID \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN=*******" \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model neuralmagic/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: /vllm-openai:latest \ --model neuralmagic/Mistral-Nemo-Instruct-2407-FP8 \ --max-model-len 5000 \ --gpu-memory-utilization 0.98 I'm running my API calls against v1/completions and only sending the below body: model = "n...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: question during inference doesn't seem any faster than raw text. usage;stale ### Your current environment ```text I'm running some tests to see if my use case would benefit from tokenizing my context before sending it i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
