# vllm-project/vllm#18786: [Bug]: Not allowed: Wheel dist/vllm-0.9.1.dev2+ge0cbad4e3-cp38-abi3-linux_x86_64.whl is larger (824.73 MB) than the limit (400 MB)

| 字段 | 值 |
| --- | --- |
| Issue | [#18786](https://github.com/vllm-project/vllm/issues/18786) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Not allowed: Wheel dist/vllm-0.9.1.dev2+ge0cbad4e3-cp38-abi3-linux_x86_64.whl is larger (824.73 MB) than the limit (400 MB)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python => ERROR [build 8/8] RUN if [ "true" = "true" ]; then python3 check-wheel-size.py dist; else echo "Skipping wheel size check."; fi 0.3s ------ > [build 8/8] RUN if [ "true" = "true" ]; then python3 check-wheel-size.py dist; else echo "Skipping wheel size check."; fi: 0.235 Not allowed: Wheel dist/vllm-0.9.1.dev2+ge0cbad4e3-cp38-abi3-linux_x86_64.whl is larger (824.73 MB) than the limit (400 MB). 0.235 vllm/vllm_flash_attn/_vllm_fa3_C.abi3.so: 1882.29 MBs uncompressed. 0.235 vllm/_C.abi3.so: 689.38 MBs uncompressed. 0.235 vllm/vllm_flash_attn/_vllm_fa2_C.abi3.so: 424.05 MBs uncompressed. 0.235 vllm/_moe_C.abi3.so: 131.93 MBs uncompressed. 0.235 vllm/_flashmla_C.abi3.so: 4.89 MBs uncompressed. 0.235 vllm/third_party/pynvml.py: 0.22 MBs uncompressed. 0.235 vllm/config.py: 0.19 MBs uncompressed. 0.235 vllm-0.9.1.dev2+ge0cbad4e3.dist-info/RECORD: 0.14 MBs uncompressed. 0.235 vllm/distributed/kv_transfer/disagg_prefill_workflow.jpg: 0.14 MBs uncompressed. 0.235 vllm/worker/hpu_model_runner.py: 0.10 MBs uncompressed. ------ Dockerfile:155 -------------------- 154 | ARG RUN_WHEEL_CHECK=true 155 | >>> RUN if [ "$RUN_WHEEL_CHECK"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Not allowed: Wheel dist/vllm-0.9.1.dev2+ge0cbad4e3-cp38-abi3-linux_x86_64.whl is larger (824.73 MB) than the limit (400 MB) bug;stale ### Your current environment ### 🐛 Describe the bug ```python => ERROR [build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sed. 0.235 vllm/third_party/pynvml.py: 0.22 MBs uncompressed. 0.235 vllm/config.py: 0.19 MBs uncompressed. 0.235 vllm-0.9.1.dev2+ge0cbad4e3.dist-info/RECORD: 0.14 MBs uncompressed. 0.235 vllm/distributed/kv_transfer/dis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: -abi3-linux_x86_64.whl is larger (824.73 MB) than the limit (400 MB) bug;stale ### Your current environment ### 🐛 Describe the bug ```python => ERROR [build 8/8] RUN if [ "true" = "true" ]; then python3 check-wheel-size...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 0.235 vllm/vllm_flash_attn/_vllm_fa3_C.abi3.so: 1882.29 MBs uncompressed. 0.235 vllm/_C.abi3.so: 689.38 MBs uncompressed.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
