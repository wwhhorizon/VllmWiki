# vllm-project/vllm#15468: [Usage]:Phi-4-multimodal-instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#15468](https://github.com/vllm-project/vllm/issues/15468) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;multimodal_vlm |
| 子分类 | kernel_eff |
| Operator 关键词 | gemm |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]:Phi-4-multimodal-instruct

### Issue 正文摘录

### Your current environment I'm using vllm in kubernetes, docker image version 0.8.1. I'm having a hard time getting LoRAs to load although I can see that the path is availble inside the running Pod. My deployment yaml: ``` apiVersion: apps/v1 kind: Deployment metadata: name: phi-4-multimodal-instruct labels: app: phi-4-multimodal-instruct spec: replicas: 1 selector: matchLabels: app: phi-4-multimodal-instruct template: metadata: labels: app: phi-4-multimodal-instruct spec: volumes: - name: model-cache hostPath: path: /mnt/data type: Directory # vLLM needs to access the host's shared memory for tensor parallel inference. - name: shm emptyDir: medium: Memory sizeLimit: "2Gi" containers: - name: phi-4-multimodal-instruct image: vllm/vllm-openai:v0.8.1 command: ["/bin/sh", "-c"] args: [ "vllm serve microsoft/Phi-4-multimodal-instruct --trust-remote-code --port 8000 --enforce-eager --gpu-memory-utilization 0.8 --dtype auto --max-model-len 128000 --enable-lora --max-lora-rank 320 --lora-extra-vocab-size 512 --limit-mm-per-prompt audio=3,image=3 --max-loras 2" ] env: - name: VLLM_ALLOW_RUNTIME_LORA_UPDATING value: "True" ports: - containerPort: 8000 resources: limits: cpu: "10" memory:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: usage;stale ### Your current environment I'm using vllm in kubernetes, docker image version 0.8.1. I'm having a hard time getting LoRAs to load although I can see that the path is availble inside the running Pod. My dep...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]:Phi-4-multimodal-instruct usage;stale ### Your current environment I'm using vllm in kubernetes, docker image version 0.8.1. I'm having a hard time getting LoRAs to load although I can see that the path is avail...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]:Phi-4-multimodal-instruct usage;stale ### Your current environment I'm using vllm in kubernetes, docker image version 0.8.1. I'm having a hard time getting LoRAs to load although I can see that the path is avail...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: -remote-code --port 8000 --enforce-eager --gpu-memory-utilization 0.8 --dtype auto --max-model-len 128000 --enable-lora --max-lora-rank 320 --lora-extra-vocab-size 512 --limit-mm-per-prompt audio=3,image=3 --max-loras 2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
