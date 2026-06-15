# vllm-project/vllm#3131: There is a error in output text. but output's token_ids is right.

| 字段 | 值 |
| --- | --- |
| Issue | [#3131](https://github.com/vllm-project/vllm/issues/3131) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> There is a error in output text. but output's token_ids is right.

### Issue 正文摘录

maybe the error happend in the file detokenize_incrementally.py the fuc is : from vllm import LLM model = LLM('*') response = model.generate('xxxxx') the result response.outputs[0].text will be truncationed. but the .tokens_ids is right. ``` version: vllm: 0.3.1 torch:2.1.2 cuda:11.8 ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ppend in the file detokenize_incrementally.py the fuc is : from vllm import LLM model = LLM('*') response = model.generate('xxxxx') the result response.outputs[0].text will be truncationed. but the .tokens_ids is right....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. but the .tokens_ids is right. ``` version: vllm: 0.3.1 torch:2.1.2 cuda:11.8 ``` development frontend_api;model_support cuda env_dependency maybe the error happend in the file detokenize_incrementally.py
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: file detokenize_incrementally.py the fuc is : from vllm import LLM model = LLM('*') response = model.generate('xxxxx') the result response.outputs[0].text will be truncationed. but the .tokens_ids is right. ``` version:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: There is a error in output text. but output's token_ids is right. stale maybe the error happend in the file detokenize_incrementally.py the fuc is : from vllm import LLM model = LLM('*') response = model.generate('xxxxx...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
