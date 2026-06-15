# vllm-project/vllm#24082: [Bug]: v1.10.x is slower than 0.8.5.post1 when running qwen3

| 字段 | 值 |
| --- | --- |
| Issue | [#24082](https://github.com/vllm-project/vllm/issues/24082) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v1.10.x is slower than 0.8.5.post1 when running qwen3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have tested every version since 0.8.5.post1, especially 0.10.x to run **qwen3 models** and their quantized models. I find the 0.8.5.post1 version always has fastest response time for qwen3 model (turn off thinking). I do not see the performance optimizations mentioned in 0.90, 0.10.x at all. This is my test code [qwen3_openai_stress_test.py](https://github.com/user-attachments/files/22088751/qwen3_openai_stress_test.py) The response times for 0.85 are around ``` │ Concurrent Requests │ 5 │ │ Total Requests │ 100 │ │ Successful Requests │ 100 (100.0%) │ │ Failed Requests │ 0 (0.0%) │ │ Total Test Duration │ 68.61 seconds │ │ Min Response Time │ 0.79 seconds │ │ Max Response Time │ 3.58 seconds │ │ Average Response Time │ 3.34 seconds │ │ Median Response Time │ 3.53 seconds │ │ P90 Response Time │ 3.55 seconds │ │ P95 Response Time │ 3.56 seconds │ │ P99 Response Time │ 3.58 seconds │ │ Std Dev Response Time │ 0.58 seconds │ ``` While 0.10.x response times are around 4.12, so basically 3.55 s vs 4.12. The 0.85 version is 16% faster. ``` │ Concurrent Requests │ 5 │ │ Total Requests │ 100 │ │ Successful Requests │ 100 (100.0%) │ │...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Your current environment ### 🐛 Describe the bug I have tested every version since 0.8.5.post1, especially 0.10.x to run **qwen3 models** and their quantized models. I find the 0.8.5.post1 version always has fastest resp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: v1.10.x is slower than 0.8.5.post1 when running qwen3 bug;stale ### Your current environment ### 🐛 Describe the bug I have tested every version since 0.8.5.post1, especially 0.10.x to run **qwen3 models** and the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: v1.10.x is slower than 0.8.5.post1 when running qwen3 bug;stale ### Your current environment ### 🐛 Describe the bug I have tested every version since 0.8.5.post1, especially 0.10.x to run **qwen3 models** and the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: since 0.8.5.post1, especially 0.10.x to run **qwen3 models** and their quantized models. I find the 0.8.5.post1 version always has fastest response time for qwen3 model (turn off thinking). I do not see the performance...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
