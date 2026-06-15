# vllm-project/vllm#17337: [Bug]: sm75 can not serve qwen3 bnb 4bit model

| 字段 | 值 |
| --- | --- |
| Issue | [#17337](https://github.com/vllm-project/vllm/issues/17337) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: sm75 can not serve qwen3 bnb 4bit model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm-openai: runtime: nvidia restart: always deploy: resources: reservations: devices: - driver: nvidia device_ids: [ '2', '3'] capabilities: [ gpu ] volumes: - ~/.cache/huggingface:/root/.cache/huggingface - /home/hucd/models:/models environment: - HUGGING_FACE_HUB_TOKEN= - CUDA_VISIBLE_DEVICES=0,1 ports: - 8001:8000 ipc: host image: vllm/vllm-openai:v0.8.5 command: --model /models/Qwen3-30B-A3B-bnb-4bit --served-model-name qwen3-a3b --tensor_parallel_size 2 --max_model_len 8192 --dtype half --max_num_seqs 1 --gpu_memory_utilization 0.9 --enable-reasoning --reasoning-parser deepseek_r1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;model_support;quantization quantization crash;mismatch dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: sm75 can not serve qwen3 bnb 4bit model bug ### Your current environment ### 🐛 Describe the bug vllm-openai: runtime: nvidia restart: always deploy: resources: reservations:
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: sm75 can not serve qwen3 bnb 4bit model bug ### Your current environment ### 🐛 Describe the bug vllm-openai: runtime: nvidia restart: always deploy: resources: reservations: devices:
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ved-model-name qwen3-a3b --tensor_parallel_size 2 --max_model_len 8192 --dtype half --max_num_seqs 1 --gpu_memory_utilization 0.9 --enable-reasoning --reasoning-parser deepseek_r1 ### Before submitting a new issue... -...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ions. correctness ci_build;model_support;quantization quantization crash;mismatch dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
