# vllm-project/vllm#11902: [Bug]: Problems with releasing memory after starting the vllm container

| 字段 | 值 |
| --- | --- |
| Issue | [#11902](https://github.com/vllm-project/vllm/issues/11902) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Problems with releasing memory after starting the vllm container

### Issue 正文摘录

### 🐛 Describe the bug Hi all. Please tell me, is it possible to clear RAM usage after loading the scales onto the GPU? As far as I understand, RAM is only needed when loading scales from the SSD. Now, when running vllm/vllm-openai:latest docker image, almost all of my RAM memory (20+ GB) is occupied by the vllm container to load the model, but after a successful launch, the memory is not released and other docker applications crash when launched due to OOM, which is not allowed in production. Code to reproduce: ``` docker run --gpus '"device=0,1"' --rm -d --net host \ --name vllm \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -v /home/thinclient/llm-server/weights:/mnt/weights \ --env "HUGGING_FACE_HUB_TOKEN= " \ --env "TORCH_USE_CUDA_DSA=1" \ --env "CUDA_LAUNCH_BLOCKING=1" \ --ipc host \ vllm/vllm-openai:latest \ --model /mnt/weights/saiga_nemo_12b-Q6_K.gguf \ --chat-template "{% if messages[0]['role'] == 'system' %}{% set system_message = messages[0]['content'] | trim + '\> --tensor-parallel-size 2 \ --pipeline-parallel-size 1 \ --gpu-memory-utilization 0.99 \ --max_model_len 11000 \ --enable-prefix-caching \ ``` ### Before submitting a new issue... - [X] Make sure you al...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nt/weights \ --env "HUGGING_FACE_HUB_TOKEN= " \ --env "TORCH_USE_CUDA_DSA=1" \ --env "CUDA_LAUNCH_BLOCKING=1" \ --ipc host \ vllm/vllm-openai:latest \ --model /mnt/weights/saiga_nemo_12b-Q6_K.gguf \ --chat-template "{%...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: of my RAM memory (20+ GB) is occupied by the vllm container to load the model, but after a successful launch, the memory is not released and other docker applications crash when launched due to OOM, which is not allowed...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: h when launched due to OOM, which is not allowed in production. Code to reproduce: ``` docker run --gpus '"device=0,1"' --rm -d --net host \ --name vllm \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -v /home/thin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: loading scales from the SSD. Now, when running vllm/vllm-openai:latest docker image, almost all of my RAM memory (20+ GB) is occupied by the vllm container to load the model, but after a successful launch, the memory is...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: all. Please tell me, is it possible to clear RAM usage after loading the scales onto the GPU? As far as I understand, RAM is only needed when loading scales from the SSD. Now, when running vllm/vllm-openai:latest docker...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
