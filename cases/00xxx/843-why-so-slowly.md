# vllm-project/vllm#843: why so slowly？

| 字段 | 值 |
| --- | --- |
| Issue | [#843](https://github.com/vllm-project/vllm/issues/843) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> why so slowly？

### Issue 正文摘录

python-3.11 torch-2.0.1 cuda-11.8 A100-40g llama-13b I build the vllm on my wsl with RTX3060， then I install the vllm‘s wheel on A100, the speed is only 37tokens/s. How can I install vllm offline? It always download the dependencies when I build it, though I have installed all the dependencies . My A100 env con't connect to the internet

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: why so slowly？ python-3.11 torch-2.0.1 cuda-11.8 A100-40g llama-13b I build the vllm on my wsl with RTX3060， then I install the vllm‘s wheel on A100, the speed is only 37tokens/s. How can I install vllm offline? It alwa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: why so slowly？ python-3.11 torch-2.0.1 cuda-11.8 A100-40g llama-13b I build the vllm on my wsl with RTX3060， then I install the vllm‘s wheel on A100, the speed is only 37tokens/s. How can I install vllm offline? It alwa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: why so slowly？ python-3.11 torch-2.0.1 cuda-11.8 A100-40g llama-13b I build the vllm on my wsl with RTX3060， then I install the vllm‘s wheel on A100, the speed is only 37tokens/s. How can I install vllm offline? It alwa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
