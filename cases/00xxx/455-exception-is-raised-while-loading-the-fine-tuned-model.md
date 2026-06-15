# vllm-project/vllm#455: Exception is raised while loading the fine tuned model

| 字段 | 值 |
| --- | --- |
| Issue | [#455](https://github.com/vllm-project/vllm/issues/455) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Exception is raised while loading the fine tuned model

### Issue 正文摘录

Hi, I have fine-tuned the `mpt-30b` and wanted to load it using vllm for inference `model = LLM(model=/local_path, tensor_parallel_size=self.vllm_args.tensor_parallel_size, pipeline_parallel_size=self.vllm_args.pipeline_parallel_size, gpu_memory_utilization=self.vllm_args.gpu_memory_utilization)` I am getting the following error: `/local_path does not appear to have a file named mosaicml/mpt-30b--configuration_mpt.py. Checkout 'https://huggingface.co//home/ubuntu/fine_tune/op/mpt_30b_gradient_accumu_checkpoint_11072023/None' for available files.` Wanted to check how to load my locally fine tuned model in the vllm

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Exception is raised while loading the fine tuned model Hi, I have fine-tuned the `mpt-30b` and wanted to load it using vllm for inference `model = LLM(model=/local_path, tensor_parallel_size=self.vllm_args.tensor_parall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
