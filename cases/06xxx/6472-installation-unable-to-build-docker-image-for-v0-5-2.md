# vllm-project/vllm#6472: [Installation]: Unable to build docker image for v0.5.2

| 字段 | 值 |
| --- | --- |
| Issue | [#6472](https://github.com/vllm-project/vllm/issues/6472) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Unable to build docker image for v0.5.2

### Issue 正文摘录

### Install command used ```sh docker build . -t vllm-v0.5.2 -f Dockerfile ``` When trying to build vLLM docker image on v0.5.2 getting below errors: 2 warnings found (use --debug to expand): - FromAsCasing: 'as' and 'FROM' keywords' casing do not match (line 83) - LegacyKeyValueFormat: "ENV key=value" should be used instead of legacy "ENV key value" format (line 152)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Unable to build docker image for v0.5.2 installation;stale ### Install command used ```sh docker build . -t vllm-v0.5.2 -f Dockerfile ``` When trying to build vLLM docker image on v0.5.2 getting below err
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 'as' and 'FROM' keywords' casing do not match (line 83) - LegacyKeyValueFormat: "ENV key=value" should be used instead of legacy "ENV key value" format (line 152)
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: Unable to build docker image for v0.5.2 installation;stale ### Install command used ```sh docker build . -t vllm-v0.5.2 -f Dockerfile ``` When trying to build vLLM docker image on v0.5.2 getting below er...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
