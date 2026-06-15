# vllm-project/vllm#12363: [RFC]: Refactor `config-format` and `load-format` as plugins

| 字段 | 值 |
| --- | --- |
| Issue | [#12363](https://github.com/vllm-project/vllm/issues/12363) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Refactor `config-format` and `load-format` as plugins

### Issue 正文摘录

### Motivation. In vLLM there is support already for two kinds of model configuration format and several weight formats. However, there are other less common uses cases that aren't covered by the existing code base. For example https://github.com/vllm-project/vllm/issues/12250 and https://github.com/vllm-project/vllm/pull/10647 . The purpose of this RFC is to enable two use cases: - Custom configuration or weight formats - Loading configurations and weights from custom storage back-ends such as KV stores. ### Proposed Change. Currently the configuration format can be controlled by the following flag: ``` --config-format {auto,hf,mistral} The format of the model config to load. * "auto" will try to load the config in hf format if available else it will try to load in mistral format ``` The proposal of this RFC is to expand it to: ``` --config-format {auto,hf,mistral} or name registered in --config-format-plugin The format of the model config to load. * "auto" will try to load the config in hf format if available else it will try to load in mistral format --config-format-plugin CONFIG_FORMAT_PLUGIN Special config format plugin to load the model configuration from custom formats or c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [RFC]: Refactor `config-format` and `load-format` as plugins RFC;stale ### Motivation. In vLLM there is support already for two kinds of model configuration format and several weight formats. However, there are other le...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: weights with random values, which is mainly for profiling. * "tensorizer" will load the weights using tensorizer from CoreWeave. See the Tensorize vLLM Model script in the Examples section for mor
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: configuration from custom formats or custom storage backends. The name registered for this plugin can be used in ``--config-format``. ``` In same way, currently the weight format is controlled by: ``` --load-format {aut...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: --config-format-plugin CONFIG_FORMAT_PLUGIN Special config format plugin to load the model configuration from custom formats or custom storage backends. The name registered for this plugin can be used in ``--config-for
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: dbytes" will load the weights using bitsandbytes quantization. ``` The proposal of this RFC is to expand it to: ``` --load-format {auto,pt,safetensors,npcache,dummy,tensorizer,sharded_state,gguf,bitsandbytes,mistral,run...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
