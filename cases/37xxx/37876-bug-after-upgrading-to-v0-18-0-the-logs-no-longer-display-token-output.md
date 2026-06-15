# vllm-project/vllm#37876: [Bug]: After upgrading to v0.18.0, the logs no longer display token output speed

| 字段 | 值 |
| --- | --- |
| Issue | [#37876](https://github.com/vllm-project/vllm/issues/37876) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: After upgrading to v0.18.0, the logs no longer display token output speed

### Issue 正文摘录

### Your current environment docker images: vllm/vllm-openai:v0.18.0-cu130 The environment variable VLLM_LOGGING_CONFIG_PATH has been configured. The logging configuration is as follows: ```json { "version": 1, "disable_existing_loggers": false, "formatters": { "standard": { "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s" } }, "handlers": { "rotating_file": { "class": "logging.handlers.RotatingFileHandler", "level": "INFO", "formatter": "standard", "filename": "/app/workspace/logs/vllm.log", "maxBytes": 10485760, "backupCount": 5, "encoding": "utf8" } }, "root": { "handlers": ["rotating_file"], "level": "INFO" } } ``` ### 🐛 Describe the bug After upgrading to v0.18.0, the logs no longer display token output speed; only API call information is shown. In version v0.17.1, the log output is as follows: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s no longer display token output speed bug ### Your current environment docker images: vllm/vllm-openai:v0.18.0-cu130 The environment variable VLLM_LOGGING_CONFIG_PATH has been configured. The logging configuration is a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: es: vllm/vllm-openai:v0.18.0-cu130 The environment variable VLLM_LOGGING_CONFIG_PATH has been configured. The logging configuration is as follows: ```json { "version": 1, "disable_existing_loggers": false, "formatters":...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: is as follows: ```json { "version": 1, "disable_existing_loggers": false, "formatters": { "standard": { "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s" } }, "handlers": { "rotating_file": { "class": "lo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
