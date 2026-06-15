# vllm-project/vllm#28063: [Bug]: Error processing images with Qwen3-VL

| 字段 | 值 |
| --- | --- |
| Issue | [#28063](https://github.com/vllm-project/vllm/issues/28063) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;gemm |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error processing images with Qwen3-VL

### Issue 正文摘录

### Your current environment Error processing images with Qwen3-VL ### 🐛 Describe the bug I am using vllm with two 5070ti video cards and the qwe3-vl-4b-instruct model, and after approximately 10 sequential requests to process images, the service crashes and with some responses it repeats the same thing infinitely. My docker-compose: services: vllm-server: image: dockerhub.timeweb.cloud/vllm/vllm-openai:latest container_name: vllm-server ports: - "8000:8000" volumes: - /home/notires/huggingface:/root/.local/share/vllm - ./cache:/root/.cache/huggingface environment: - CUDA_VISIBLE_DEVICES=0,1 - TOKENIZERS_PARALLELISM=false - HF_HOME=/root/.cache/huggingface command: - --model=/root/.local/share/vllm/qwen3-vl-4b-instruct - --served-model-name=qwen3-vl - --host=0.0.0.0 - --port=8000 - --tensor-parallel-size=2 - --download-dir=/root/.local/share/vllm - --max-num-seqs=128 - --gpu-memory-utilization=0.85 - --max-model-len=16384 - --enable-chunked-prefill - --enable-prefix-caching - --trust-remote-code - --mm-encoder-tp-mode=data deploy: resources: reservations: devices: - driver: nvidia count: 2 capabilities: [gpu] restart: unless-stopped ERROR vllm-server | (APIServer pid=1) INFO: 172....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Error processing images with Qwen3-VL bug;stale ### Your current environment Error processing images with Qwen3-VL ### 🐛 Describe the bug I am using vllm with two 5070ti video cards and the qwe3-vl-4b-instruct mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rashes and with some responses it repeats the same thing infinitely. My docker-compose: services: vllm-server: image: dockerhub.timeweb.cloud/vllm/vllm-openai:latest container_name: vllm-server ports: - "8000:8000" volu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Error processing images with Qwen3-VL bug;stale ### Your current environment Error processing images with Qwen3-VL ### 🐛 Describe the bug I am using vllm with two 5070ti video cards and the qwe3-vl-4b-instruct mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e/vllm - ./cache:/root/.cache/huggingface environment: - CUDA_VISIBLE_DEVICES=0,1 - TOKENIZERS_PARALLELISM=false - HF_HOME=/root/.cache/huggingface command: - --model=/root/.local/share/vllm/qwen3-vl-4b-instruct - --ser...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nment: - CUDA_VISIBLE_DEVICES=0,1 - TOKENIZERS_PARALLELISM=false - HF_HOME=/root/.cache/huggingface command: - --model=/root/.local/share/vllm/qwen3-vl-4b-instruct - --served-model-name=qwen3-vl - --host=0.0.0.0 - --por...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
