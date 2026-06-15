# vllm-project/vllm#5730: api_server.py: error: unrecognized arguments: --tool-use-prompt-template --enable-api-tools --enable-auto-tool-choice

| 字段 | 值 |
| --- | --- |
| Issue | [#5730](https://github.com/vllm-project/vllm/issues/5730) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> api_server.py: error: unrecognized arguments: --tool-use-prompt-template --enable-api-tools --enable-auto-tool-choice

### Issue 正文摘录

My vllm version is 0.5.0 post1. I want to make qwen2:7b-instruct model to have functional calling enabled. So following the issue https://github.com/vllm-project/vllm/pull/5649 here, I run the command `python -m vllm.entrypoints.openai.api_server --model /home/asus/autodl-tmp/qwen/Qwen2-7B-Instruct --tool-use-prompt-template /home/asus/autodl-tmp/examples/chatml.jinja --enable-api-tools --enable-auto-tool-choice` But it shows api_server.py: error: unrecognized arguments: --tool-use-prompt-template --enable-api-tools --enable-auto-tool-choice ![image](https://github.com/vllm-project/vllm/assets/20237650/60c5dfc6-e356-48d7-b409-054587d4df4c)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: o-tool-choice usage;stale My vllm version is 0.5.0 post1. I want to make qwen2:7b-instruct model to have functional calling enabled. So following the issue https://github.com/vllm-project/vllm/pull/5649 here, I run the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: emplate --enable-api-tools --enable-auto-tool-choice usage;stale My vllm version is 0.5.0 post1. I want to make qwen2:7b-instruct model to have functional calling enabled. So following the issue https://github.com/vllm-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: l-use-prompt-template --enable-api-tools --enable-auto-tool-choice usage;stale My vllm version is 0.5.0 post1. I want to make qwen2:7b-instruct model to have functional calling enabled. So following the issue https://gi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
