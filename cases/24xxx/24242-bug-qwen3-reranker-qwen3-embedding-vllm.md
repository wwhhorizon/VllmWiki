# vllm-project/vllm#24242: [Bug]: Qwen3-reranker默认示例的输出结果不精准，与Qwen3-embedding仓库中提供的vllm示例输出结果不一致（顺序不一致）。

| 字段 | 值 |
| --- | --- |
| Issue | [#24242](https://github.com/vllm-project/vllm/issues/24242) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-reranker默认示例的输出结果不精准，与Qwen3-embedding仓库中提供的vllm示例输出结果不一致（顺序不一致）。

### Issue 正文摘录

### Your current environment ```text 使用vllm 0.10.1.1 docker镜像运行 ``` ### 🐛 Describe the bug 数据示例如下： queries = ["中国的首都是哪里?"] documents = [ "中国的首都是北京", "中国的首都是南京", "中国的首都是东京" ] 使用vllm [offline示例](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/qwen3_reranker.py)输出结果如下： 结果排序错误。 使用[qwen3-embedding仓库示例](https://github.com/QwenLM/Qwen3-Embedding/blob/main/examples/qwen3_reranker_vllm.py)输出结果如下： 排序结果正确。 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 出结果不一致（顺序不一致）。 bug ### Your current environment ```text 使用vllm 0.10.1.1 docker镜像运行 ``` ### 🐛 Describe the bug 数据示例如下： queries = ["中国的首都是哪里?"] documents = [ "中国的首都是北京", "中国的首都是南京", "中国的首都是东京" ] 使用vllm [offline示例](https:/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 正确。 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Qwen3-reranker默认示例的输出结果不精准，与Qwen3-embedding仓库中提供的vllm示例输出结果不一致（顺序不一致）。 bug ### Your current environment ```text 使用vllm 0.10.1.1 docker镜像运行 ``` ### 🐛 Describe the bug 数据示例如下： queries = ["中国的首都是哪里?"] documents =
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
