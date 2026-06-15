# vllm-project/vllm#32807: [Usage]: How to use tensorizer to load models from S3 with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#32807](https://github.com/vllm-project/vllm/issues/32807) |
| 状态 | open |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to use tensorizer to load models from S3 with vLLM

### Issue 正文摘录

### Current environment ### How would you like to use vllm I am following the [coreweave's tensorizer model loading documentation](https://docs.vllm.ai/en/stable/models/extensions/tensorizer/#serving-the-model-using-tensorizer) and I have serialized and pushed the model to an S3 endpoint. However when loading the model as per documentation: ``` vllm serve s3://my-bucket/vllm/facebook/opt-125m/v1 \ --load-format tensorizer ``` It picks the `s3://` as `runai_streamer` which fails because load-format doesn't matches with that. ``` Value error, To load a model from S3, 'load_format' must be 'runai_streamer' or 'runai_streamer_sharded', but got 'tensorizer'. ``` Upon taking a look at the source, this is expected because `s3://` and `gs://` prefix model path are considered to be using `runai_streamer` in https://github.com/vllm-project/vllm/blob/180fba653ead2274bfcd3951a275f4d6cf9ade04/vllm/transformers_utils/runai_utils.py#L16 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked question...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: L16 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to use tensorizer to load models from S3 with vLLM usage ### Current environment ### How would you like to use vllm I am following the [coreweave's tensorizer model loading documentation](https://docs.vllm....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
