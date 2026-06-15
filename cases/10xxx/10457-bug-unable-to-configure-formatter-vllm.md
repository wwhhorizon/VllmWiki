# vllm-project/vllm#10457: [Bug]: Unable to configure formatter 'vllm'

| 字段 | 值 |
| --- | --- |
| Issue | [#10457](https://github.com/vllm-project/vllm/issues/10457) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Unable to configure formatter 'vllm'

### Issue 正文摘录

### Your current environment ### Model Input Dumps ### 🐛 Describe the bug Raise ValueError: Unable to configure formatter 'vllm' when using the latest version of vllm, using the previous verson don't break anything. Rolling back the vllm version to `0.6.2` resolves the issue. The content of `vllm_logging_config.json` can be found in https://github.com/vllm-project/vllm/blob/main/examples/logging_configuration.md The content is: ``` { "formatters": { "vllm": { "class": "vllm.logging.NewLineFormatter", "datefmt": "%m-%d %H:%M:%S", "format": "%(levelname)s %(asctime)s %(filename)s:%(lineno)d] %(message)s" } }, "handlers": { "vllm": { "class" : "logging.StreamHandler", "formatter": "vllm", "level": "INFO", "stream": "ext://sys.stdout" } }, "loggers": { "vllm": { "handlers": ["vllm"], "level": "DEBUG", "propagage": false }, "vllm.example_noisy_logger": { "propagate": false } }, "version": 1 } ``` The related content in .env file: ``` VLLM_CONFIGURE_LOGGING=1 VLLM_LOGGING_CONFIG_PATH="./utils/vllm_logging_config.json" ``` The error: ``` File "/root/llm-project/LVLM/model/blip2.py", line 12, in from vllm import LLM File "/root/anaconda3/envs/LVLM/lib/python3.10/site-packages/vllm/__init_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e ValueError: Unable to configure formatter 'vllm' when using the latest version of vllm, using the previous verson don't break anything. Rolling back the vllm version to `0.6.2` resolves the issue. The content of `vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Unable to configure formatter 'vllm' bug ### Your current environment ### Model Input Dumps ### 🐛 Describe the bug Raise ValueError: Unable to configure formatter 'vllm' when using the latest version of vllm, usi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "handlers": ["vllm"], "level": "DEBUG", "propagage": false }, "vllm.example_noisy_logger": { "propagate": false } }, "version": 1 } ``` The related content in .env file: ``` VLLM_CONFIGURE_LOGGING=1 VLLM_LOGGING_CONFIG_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
