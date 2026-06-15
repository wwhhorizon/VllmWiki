# vllm-project/vllm#27651: [Bug]: Qwen3 VL describes 512x512 images wrong

| 字段 | 值 |
| --- | --- |
| Issue | [#27651](https://github.com/vllm-project/vllm/issues/27651) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8;gemm;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 VL describes 512x512 images wrong

### Issue 正文摘录

### Your current environment L40S cards, Docker-based ``` services: vllm-qwen3-vl-30b-a3b-instruct: image: vllm/vllm-openai:v0.11.0 container_name: vllm-qwen3-vl-30b-a3b-instruct environment: - VLLM_NO_USAGE_STATS=1 ipc: host deploy: resources: reservations: devices: - driver: nvidia device_ids: ["2", "3"] capabilities: [gpu] network_mode: host volumes: - /mnt/sda/huggingface:/root/.cache/huggingface - .:/opt/vllm command: - --port=8003 - --model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 # FP8 only on CorpIT with L40s - --disable-custom-all-reduce # Only on CorpIT with PCIe - --served-model-name - Qwen/Qwen3-VL-30B-A3B-Instruct - Qwen/Qwen3-VL-30B-A3B - Qwen/Qwen3-VL - Qwen/Qwen2.5-VL-72B-Instruct # Fake for compatibility - --max-model-len=65536 # Default 298,928 - '--limit-mm-per-prompt={"images":3,"videos":1}' - --tensor-parallel-size=2 - --gpu-memory-utilization=0.70 - --swap-space=5 restart: unless-stopped ``` ### 🐛 Describe the bug The following image, depicting a witch in 512x512 pixel, is described totally wrong: ```bash $ curl http://ai1.dev.init:8003/v1/chat/completions -k -H 'Content-Type: application/json' -d @- <<EOF { "model": "Qwen/Qwen3-VL-30B-A3B-Instruct", "messages": [...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 512x512 images wrong bug;stale ### Your current environment L40S cards, Docker-based ``` services: vllm-qwen3-vl-30b-a3b-instruct: image: vllm/vllm-openai:v0.11.0 container_name: vllm-qwen3-vl-30b-a3b-instruct environme...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: and: - --port=8003 - --model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 # FP8 only on CorpIT with L40s - --disable-custom-all-reduce # Only on CorpIT with PCIe - --served-model-name - Qwen/Qwen3-VL-30B-A3B-Instruct - Qwen/Qwen3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3 VL describes 512x512 images wrong bug;stale ### Your current environment L40S cards, Docker-based ``` services: vllm-qwen3-vl-30b-a3b-instruct: image: vllm/vllm-openai:v0.11.0 container_name: vllm-qwen3
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ll. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: uild;distributed_parallel;model_support;quantization;sampling_logits fp8;gemm;sampling dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
