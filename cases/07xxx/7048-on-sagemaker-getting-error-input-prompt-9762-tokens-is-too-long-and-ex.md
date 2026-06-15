# vllm-project/vllm#7048: On sagemaker, getting error "Input prompt (9762 tokens) is too long and exceeds limit of 8192"

| 字段 | 值 |
| --- | --- |
| Issue | [#7048](https://github.com/vllm-project/vllm/issues/7048) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> On sagemaker, getting error "Input prompt (9762 tokens) is too long and exceeds limit of 8192"

### Issue 正文摘录

I'm running vllm with: - model = `meta-llama/Meta-Llama-3-8B-Instruct` - DJL image = `763104351884.dkr.ecr.us-west-2.amazonaws.com/djl-inference:0.28.0-lmi10.0.0-cu124` - the env of the deployed model is as follow ```python { "TENSOR_PARALLEL_DEGREE": "max", "OPTION_ROLLING_BATCH": "vllm", "OPTION_TRUST_REMOTE_CODE": "true", "MAX_ROLLING_BATCH_SIZE": "32", "MAX_LENGTH": "15360", } ``` The predictor (after deploying the model on the endpoint_name) is instantiated and used as follow: ```python predictor = Predictor( endpoint_name=endpoint_name, session=sagemaker_session, serializer=JSONSerializer(), deserializer=JSONDeserializer(), ) predictor.predict({ "messages": prompt, "parameters": parameters, }) ``` I've tried to add the parameter `MAX_LENGTH=15360` to the env (as above) but it does not seems to make a difference. Should I put some other parameter in the env?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s too long and exceeds limit of 8192" bug;stale I'm running vllm with: - model = `meta-llama/Meta-Llama-3-8B-Instruct` - DJL image = `763104351884.dkr.ecr.us-west-2.amazonaws.com/djl-inference:0.28.0-lmi10.0.0-cu124` -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: r "Input prompt (9762 tokens) is too long and exceeds limit of 8192" bug;stale I'm running vllm with: - model = `meta-llama/Meta-Llama-3-8B-Instruct` - DJL image = `763104351884.dkr.ecr.us-west-2.amazonaws.com/djl-infer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
