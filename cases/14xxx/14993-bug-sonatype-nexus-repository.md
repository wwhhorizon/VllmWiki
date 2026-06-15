# vllm-project/vllm#14993: [Bug]: 使用Sonatype Nexus Repository时下载模型错误。

| 字段 | 值 |
| --- | --- |
| Issue | [#14993](https://github.com/vllm-project/vllm/issues/14993) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 使用Sonatype Nexus Repository时下载模型错误。

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## docker 运行 vllm版本：vllm/vllm-openai:latest docker中的： huggingface-cli version huggingface_hub version: 0.28.1 运行时环境变量：HF_ENDPOINT=http://mvn.services.apps/repository/hf-mirror/ error log： ``` huggingface_hub.errors.HfHubHTTPError: 404 Client Error: Not Found for url: http://mvn.services.apps/repository/hf-mirror/InfiniFlow/text_concat_xgb_v1.0/resolve/main/config.json ``` ## 使用外部huggingface-cli huggingface-cli version huggingface_hub version: 0.29.3 huggingface-cli env - ENDPOINT: http://mvn.services.apps/repository/hf-mirror 使用 `huggingface-cli download InfiniFlow/text_concat_xgb_v1.0` 可以正常下载模型 实际正确可以访问的config.json的url： `http://mvn.services.apps/repository/hf-mirror/api/models/InfiniFlow/text_concat_xgb_v1.0/revision/main` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 误。 bug;stale ### Your current environment ### 🐛 Describe the bug ## docker 运行 vllm版本：vllm/vllm-openai:latest docker中的： huggingface-cli version huggingface_hub version: 0.28.1 运行时环境变量：HF_ENDPOINT=http://mvn.services.apps...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: scribe the bug ## docker 运行 vllm版本：vllm/vllm-openai:latest docker中的： huggingface-cli version huggingface_hub version: 0.28.1 运行时环境变量：HF_ENDPOINT=http://mvn.services.apps/repository/hf-mirror/ error log： ``` huggingface_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: in` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: 使用Sonatype Nexus Repository时下载模型错误。 bug;stale ### Your current environment ### 🐛 Describe the bug ## docker 运行 vllm版本：vllm/vllm-openai:latest docker中的： huggingface-cli version huggingface_hub version: 0.28.1 运行时环...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
