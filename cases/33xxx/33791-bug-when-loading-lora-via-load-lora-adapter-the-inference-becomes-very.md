# vllm-project/vllm#33791: [Bug]: When loading LoRA via load_lora_adapter, the inference becomes very slow with high CPU usage

| 字段 | 值 |
| --- | --- |
| Issue | [#33791](https://github.com/vllm-project/vllm/issues/33791) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When loading LoRA via load_lora_adapter, the inference becomes very slow with high CPU usage

### Issue 正文摘录

### Your current environment When loading LoRA via load_lora_adapter, the inference becomes very slow with high CPU usage. Seems it's using CPU instead of GPU for inference. However, using --lora-modules works at normal speed. Setting OMP_NUM_THREADS to 2 is not working. ### 🐛 Describe the bug ``` docker rm -f Qwen3-30B-A3B-Instruct-2507 docker run -d \ --gpus '"device=0"' \ -v /etc/localtime:/etc/localtime \ -v /mnt/data2/ai_deploy/models/pretrained/modelscope:/root/.cache/modelscope \ -v ./:/workspace/ \ -e VLLM_USE_MODELSCOPE=True \ -e VLLM_ALLOW_RUNTIME_LORA_UPDATING=True \ -e VLLM_LORA_DISABLE_PDL=1 \ -p 9999:8000 \ --ipc=host \ --shm-size=4gb \ --name Qwen3-30B-A3B-Instruct-2507 \ --restart always \ vllm/vllm-openai:v0.15.0 \ --model /root/.cache/modelscope/hub/unsloth/Qwen3-30B-A3B-Instruct-2507 \ --served-model-name Qwen3-30B-A3B-Instruct-2507 \ --port 8000 \ --trust_remote_code \ --max-num-seqs 8 \ --max-model-len 2048 \ --max-num-batched-tokens 2048 \ --gpu-memory-utilization 0.5 \ --tensor-parallel-size 1 \ --disable-fastapi-docs \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --enable-lora \ --max-loras 4 \ --max-lora-rank 64 ``` ``` curl -X POST http://local...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: M_THREADS to 2 is not working. ### 🐛 Describe the bug ``` docker rm -f Qwen3-30B-A3B-Instruct-2507 docker run -d \ --gpus '"device=0"' \ -v /etc/localtime:/etc/localtime \ -v /mnt/data2/ai_deploy/models/pretrained/model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: etting OMP_NUM_THREADS to 2 is not working. ### 🐛 Describe the bug ``` docker rm -f Qwen3-30B-A3B-Instruct-2507 docker run -d \ --gpus '"device=0"' \ -v /etc/localtime:/etc/localtime \ -v /mnt/data2/ai_deploy/models/pre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lways \ vllm/vllm-openai:v0.15.0 \ --model /root/.cache/modelscope/hub/unsloth/Qwen3-30B-A3B-Instruct-2507 \ --served-model-name Qwen3-30B-A3B-Instruct-2507 \ --port 8000 \ --trust_remote_code \ --max-num-seqs 8 \ --max...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ad_lora_adapter, the inference becomes very slow with high CPU usage bug;stale ### Your current environment When loading LoRA via load_lora_adapter, the inference becomes very slow with high CPU usage. Seems it's using...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
