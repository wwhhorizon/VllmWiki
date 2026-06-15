# vllm-project/vllm#1467: Proposal: Add model registration to support proprietary models

| 字段 | 值 |
| --- | --- |
| Issue | [#1467](https://github.com/vllm-project/vllm/issues/1467) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Proposal: Add model registration to support proprietary models

### Issue 正文摘录

So far, users have had to fork and maintain an internal version of vLLM in order to run a proprietary model with it. Is it a good idea adding model registration, similar to `AutoModelForCausalLM.register(config_class, model_class)` in [Hugging Face Transformer](https://huggingface.co/docs/transformers/v4.34.1/en/quicktour#automodel)? In this way, users could define their models in their private Git repos. For example, in https://github.com/my/private_model.git, I could have `mymodel.py`: ```python import torch import vllm # Register MyModel to vllm.model_executor.model_loader._MODEL_REGISTRY vllm.register(model_class=MyModel) class MyModel(torch.nn.Module): def __init__(self, config: MyModelConfig) -> None: super().__init__() vocab_size = ((config.vocab_size + 63) // 64) * 64 self.embed_tokens = vllm.parallel_utils.layers.VocabParallelEmbedding( vocab_size, config.hidden_size, ) self.norm = vllm.layers.RMSNorm(config.hidden_size, eps=config.rms_norm_eps) ``` Then, I would run a vLLM service with the following command to serve a pre-trained `MyModel`: ```shell pip install -e ~/w/mymodel python -m vllm.entrypoints.api_server -m mymodel ``` Or, ```shell python -m vllm.entrypoint.api_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: re request;stale So far, users have had to fork and maintain an internal version of vLLM in order to run a proprietary model with it. Is it a good idea adding model registration, similar to `AutoModelForCausalLM.registe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Proposal: Add model registration to support proprietary models feature request;stale So far, users have had to fork and maintain an internal version of vLLM in order to run a proprietary model with it. Is it a good idea...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Proposal: Add model registration to support proprietary models feature request;stale So far, users have had to fork and maintain an internal version of vLLM in order to run a proprietary model with it. Is it a good idea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
