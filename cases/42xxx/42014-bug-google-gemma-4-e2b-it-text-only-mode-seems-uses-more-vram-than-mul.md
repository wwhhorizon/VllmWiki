# vllm-project/vllm#42014: [Bug]: google/gemma-4-E2B-it text-only mode seems uses more VRAM than multimodal-mode

| 字段 | 值 |
| --- | --- |
| Issue | [#42014](https://github.com/vllm-project/vllm/issues/42014) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support;multimodal_vlm |
| 子分类 | memory |
| Operator 关键词 | gemm |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: google/gemma-4-E2B-it text-only mode seems uses more VRAM than multimodal-mode

### Issue 正文摘录

### Your current environment ```sh docker pull vllm/vllm-openai:v0.20.1 ``` I use docker image. ### 🐛 Describe the bug When I enable modalities (image=1, video=1, audio=1), vllm seems able to load on RTX 3060 VRAM 12 GB, ```yaml name: vllm-deploy services: vllm: runtime: nvidia deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: - gpu volumes: - ${PWD}/.cache/:/root/.cache/ ports: - 8791:8000 env_file: - path: ${PWD}/vllm/.env image: vllm/vllm-openai:v0.20.1 command: > google/gemma-4-E2B-it --max-model-len 1024 --max_num_batched_tokens 1024 --max-num-seqs 1 --gpu-memory-utilization 0.95 --no-enable-prefix-caching --trust-remote-code --limit-mm-per-prompt '{"image":1, "video": 1, "audio": 1}' ``` but when I configure to use text-only, ```yaml name: vllm-deploy services: vllm: runtime: nvidia deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: - gpu volumes: - ${PWD}/.cache/:/root/.cache/ ports: - 8791:8000 env_file: - path: ${PWD}/vllm/.env image: vllm/vllm-openai:v0.20.1 command: > google/gemma-4-E2B-it --max-model-len 1024 --max_num_batched_tokens 1024 --max-num-seqs 1 --gpu-memory-utilization 0.95 --no-enable-prefix...

## 现有链接修复摘要

#42439 [Bugfix] Add safety buffer for multimodal models in text-only mode

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: google/gemma-4-E2B-it text-only mode seems uses more VRAM than multimodal-mode bug ### Your current environment ```sh docker pull vllm/vllm-openai:v0.20.1 ``` I use docker image. ### 🐛 Describe the bug When I ena...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s more VRAM than multimodal-mode bug ### Your current environment ```sh docker pull vllm/vllm-openai:v0.20.1 ``` I use docker image. ### 🐛 Describe the bug When I enable modalities (image=1, video=1, audio=1), vllm seem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nable modalities (image=1, video=1, audio=1), vllm seems able to load on RTX 3060 VRAM 12 GB, ```yaml name: vllm-deploy services: vllm: runtime: nvidia deploy: resources: reservations: devices: - driver: nvidia count: a...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: google/gemma-4-E2B-it text-only mode seems uses more VRAM than multimodal-mode bug ### Your current environment ```sh docker pull vllm/vllm-openai:v0.20.1 ``` I use docker image. ### 🐛 Describe the bug When I ena...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance ci_build;model_support;multimodal_vlm gemm env_dependency #42439 [Bugfix]...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42439](https://github.com/vllm-project/vllm/pull/42439) | closes_keyword | 0.95 | [Bugfix] Add safety buffer for multimodal models in text-only mode | Fix #42014 When a multimodal model runs in text-only mode (all mm limits = 0), encoder towers are skipped, causing the memory profiler to underestimate memory usage. The KV cac |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
