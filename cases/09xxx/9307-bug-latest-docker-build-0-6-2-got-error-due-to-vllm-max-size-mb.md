# vllm-project/vllm#9307: [Bug]: latest docker build (0.6.2) got error due to VLLM_MAX_SIZE_MB

| 字段 | 值 |
| --- | --- |
| Issue | [#9307](https://github.com/vllm-project/vllm/issues/9307) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: latest docker build (0.6.2) got error due to VLLM_MAX_SIZE_MB

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug it's a docker build issue, ```sh DOCKER_BUILDKIT=1 docker build . --tag vllm:0.6.2 ``` error log: ```yml => ERROR [build 15/15] RUN if [ "true" = "true" ]; then python3 check-wheel-size.py dist; else echo "Skipping wheel size check 0.4s ------ > [build 15/15] RUN if [ "true" = "true" ]; then python3 check-wheel-size.py dist; else echo "Skipping wheel size check."; fi: 0.354 Not allowed: Wheel dist/vllm-0.6.3.dev173+g36ea7907.d20241012.cu124-cp38-abi3-linux_x86_64.whl is larger (291.37 MB) than the limit (250 MB). 0.354 vllm/_C.abi3.so: 530.03 MBs uncompressed. 0.354 vllm/vllm_flash_attn/vllm_flash_attn_c.abi3.so: 257.26 MBs uncompressed. 0.354 vllm/_moe_C.abi3.so: 94.64 MBs uncompressed. 0.354 vllm/_core_C.abi3.so: 4.59 MBs uncompressed. 0.354 vllm/worker/model_runner.py: 0.08 MBs uncompressed. 0.354 vllm/config.py: 0.08 MBs uncompressed. 0.354 vllm/engine/llm_engine.py: 0.08 MBs uncompressed. 0.354 vllm/core/scheduler.py: 0.07 MBs uncompressed. 0.354 vllm/model_executor/layers/sampler.py: 0.05 MBs uncompressed. 0.354 vllm/sequence.py: 0.05 MBs uncompressed. ------ Dockerfile:128 --------------...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: latest docker build (0.6.2) got error due to VLLM_MAX_SIZE_MB bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug it's a docker build issue, ```sh DOCKER_BUILDKIT=1 d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rks ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: r due to VLLM_MAX_SIZE_MB bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug it's a docker build issue, ```sh DOCKER_BUILDKIT=1 docker build . --tag vllm:0.6.2 ``` error lo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: latest docker build (0.6.2) got error due to VLLM_MAX_SIZE_MB bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug it's a docker build issue, ```sh DOCKER_BUILDKIT=1 d...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [ "true" = "true" ]; then python3 check-wheel-size.py dist; else echo "Skipping wheel size check 0.4s ------ > [build 15/15] RUN if [ "true" = "true" ]; then python3 check-wheel-size.py dist; else echo "Skipping wheel s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
