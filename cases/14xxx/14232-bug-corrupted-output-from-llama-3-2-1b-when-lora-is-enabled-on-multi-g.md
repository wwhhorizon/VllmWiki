# vllm-project/vllm#14232: [Bug]: Corrupted output from Llama-3.2-1B when LoRA is enabled on multi-GPU instance

| 字段 | 值 |
| --- | --- |
| Issue | [#14232](https://github.com/vllm-project/vllm/issues/14232) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Corrupted output from Llama-3.2-1B when LoRA is enabled on multi-GPU instance

### Issue 正文摘录

### Your current environment N/A, running docker images (v0.7.3 and v0.6.3.post1) ### 🐛 Describe the bug vLLM docker image (tested v0.7.3 and v0.6.3.post1) produces corrupted output for Llama-3.2-1B on multi-GPU instance (ml.g6e.12xlarge (AWS) == 4 x L40s) when enabling LoRA adapters. Works fine on a single-GPU instance (ml.g6e.4xlarge == 1 x L40s). To reproduce: 1. start the vLLM container: ```bash docker run --runtime nvidia --gpus all \ -p 8000:8000 \ --ipc=host \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -e HF_TOKEN=$HF_TOKEN \ vllm/vllm-openai:v0.7.3 \ --tensor-parallel-size 4 \ --model meta-llama/Llama-3.2-1B \ --served-model-name model \ --enable_lora \ --max-loras 2 ``` Send the inference request using `curl`: ```bash curl localhost:8000/v1/completions -H "Content-Type: application/json" -d '{ "model": "model", "prompt": "What is Amazon SageMaker?" }' ``` result: ``` {"id":"cmpl-332d784b82674c149f371069e2a831e8","object":"text_completion","created":1741103308,"model":"model","choices":[{"index":0,"text":"TumblrgetDbprogetDb MYSQLPlay on meetup in Zh conformsTumblr\n\n\n\n\n\n\n\n Tag movers","logprobs":null,"finish_reason":"length","stop_reason":null,"prompt_logpr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Corrupted output from Llama-3.2-1B when LoRA is enabled on multi-GPU instance bug ### Your current environment N/A, running docker images (v0.7.3 and v0.6.3.post1) ### 🐛 Describe the bug vLLM docker image (tested...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s. Works fine on a single-GPU instance (ml.g6e.4xlarge == 1 x L40s). To reproduce: 1. start the vLLM container: ```bash docker run --runtime nvidia --gpus all \ -p 8000:8000 \ --ipc=host \ -v ~/.cache/huggingface:/root/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: led on multi-GPU instance bug ### Your current environment N/A, running docker images (v0.7.3 and v0.6.3.post1) ### 🐛 Describe the bug vLLM docker image (tested v0.7.3 and v0.6.3.post1) produces corrupted output for Lla...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: )** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ame model \ --enable_lora \ --max-loras 2 ``` Send the inference request using `curl`: ```bash curl localhost:8000/v1/completions -H "Content-Type: application/json" -d '{ "model": "model", "prompt": "What is Amazon Sag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
