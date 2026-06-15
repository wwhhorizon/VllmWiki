# vllm-project/vllm#19738: Release dataset of bug-fixing commits and test cases on Hugging Face

| 字段 | 值 |
| --- | --- |
| Issue | [#19738](https://github.com/vllm-project/vllm/issues/19738) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Release dataset of bug-fixing commits and test cases on Hugging Face

### Issue 正文摘录

Hi @Isotr0py 🤗 I'm Niels and work as part of the open-source team at Hugging Face. I discovered your work on Arxiv and was wondering whether you would like to submit it to [hf.co/papers](https://hf.co/papers) to improve its discoverability.If you are one of the authors, you can submit it at https://huggingface.co/papers/submit. The paper page lets people discuss about your paper and lets them find artifacts about it (your dataset for instance), you can also claim the paper as yours which will show up on your public profile at HF, add Github and project page URLs. Would you like to host the datasets you've released on https://huggingface.co/datasets? I see you're using Google Drive for it. Hosting on Hugging Face will give you more visibility/enable better discoverability, and will also allow people to do: ```python from datasets import load_dataset dataset = load_dataset("your-hf-org-or-username/your-dataset") ``` If you're down, leaving a guide here: https://huggingface.co/docs/datasets/loading. We also support Webdataset, useful for image/video datasets: https://huggingface.co/docs/datasets/en/loading#webdataset. Besides that, there's the [dataset viewer](https://huggingface.co/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: work on Arxiv and was wondering whether you would like to submit it to [hf.co/papers](https://hf.co/papers) to improve its discoverability.If you are one of the authors, you can submit it at https://huggingface.co/paper...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Release dataset of bug-fixing commits and test cases on Hugging Face Hi @Isotr0py 🤗 I'm Niels and work as part of the open-source team at Hugging Face. I discovered your work on Arxiv and was wondering whether you would...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: coverability, and will also allow people to do: ```python from datasets import load_dataset dataset = load_dataset("your-hf-org-or-username/your-dataset") ``` If you're down, leaving a guide here: https://huggingface.co...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
