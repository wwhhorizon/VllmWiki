# vllm-project/vllm#2891: Mpt based model generates different outputs for varying tensor_parallel_size

| 字段 | 值 |
| --- | --- |
| Issue | [#2891](https://github.com/vllm-project/vllm/issues/2891) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Mpt based model generates different outputs for varying tensor_parallel_size

### Issue 正文摘录

Hi! Wanted to be able to send longer inputs (of the range 8k input tokens) to a 7b mpt based model and hence switched from a single GPU instance (AWS sagemaker g5.2xlarge, 24GB GPU mem) to a multi-GPU instance (AWS sagemaker g5.12x large, 4 gpus, 24GB GPU mem each). Also switched from using a tensor_parallel_size of 1 to 4 in the configurations, but now I get different outputs for the same input provided in both the scenarios (greedy based output token generation strategy). Have I missed some configuration? Why am I getting different outputs when the tensor_parallel_size is changed from 1 to 4? Serving the model using djl-serving with rolling_batch set to vllm. djl serving configuration on g5.2x large instance: ``` engine=Python option.task=text-generation option.s3url={{s3url}} option.tensor_parallel_degree=1 option.rolling_batch=vllm option.dtype=bf16 Dai.djl.logging.level=debug ``` djl serving configuration on g5.12x large instance: ``` engine=Python option.task=text-generation option.s3url={{s3url}} option.tensor_parallel_degree=4 option.rolling_batch=vllm option.dtype=bf16 Dai.djl.logging.level=debug ``` Deep learning container used: [DJLServing 0.26.0 with DeepSpeed 0.12.6,...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: s3url}} option.tensor_parallel_degree=1 option.rolling_batch=vllm option.dtype=bf16 Dai.djl.logging.level=debug ``` djl serving configuration on g5.12x large instance: ``` engine=Python option.task=text-generation optio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Mpt based model generates different outputs for varying tensor_parallel_size Hi! Wanted to be able to send longer inputs (of the range 8k input tokens) to a 7b mpt based model and hence switched from a single GPU instan...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Mpt based model generates different outputs for varying tensor_parallel_size Hi! Wanted to be able to send longer inputs (of the range 8k input tokens) to a 7b mpt based model and hence switched from a single GPU instan...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: pe=bf16 Dai.djl.logging.level=debug ``` Deep learning container used: [DJLServing 0.26.0 with DeepSpeed 0.12.6, Hugging Face Transformers 4.36.2 and Hugging Face Accelerate 0.25.0](https://github.com/aws/deep-learning-c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
