# vllm-project/vllm#18318: [Bug] [Vul]: weak use of MD5 hashing in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#18318](https://github.com/vllm-project/vllm/issues/18318) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [Vul]: weak use of MD5 hashing in vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Related to #17031. When enabling `FIPS`, vLLM throws the error `ValueError: Model architectures ['OPTForCausalLM'] failed to be inspected. Please check the logs for more details.`, due to the lack of `usedforsecurity=False` for MD5 hashing. Previous PRs (#17043 and #15299) have fixed this. But some places still lack this parameter. https://github.com/vllm-project/vllm/blob/9ab2c02ff8ef05cb6c4b2bdc9a4faaee61892450/vllm/model_executor/model_loader/neuronx_distributed.py#L146-L147 https://github.com/vllm-project/vllm/blob/9ab2c02ff8ef05cb6c4b2bdc9a4faaee61892450/vllm/model_executor/model_loader/neuronx_distributed.py#L266-L267 https://github.com/vllm-project/vllm/blob/9ab2c02ff8ef05cb6c4b2bdc9a4faaee61892450/vllm/model_executor/model_loader/neuronx_distributed.py#L429-L430 **Warning** `usedforsecurity=False` is a "do not explode in FIPS mode" flag to make software FIPS tolerant, not making the code comply with FIPS.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: oftware FIPS tolerant, not making the code comply with FIPS. development ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: o #17031. When enabling `FIPS`, vLLM throws the error `ValueError: Model architectures ['OPTForCausalLM'] failed to be inspected. Please check the logs for more details.`, due to the lack of `usedforsecurity=False` for...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: check the logs for more details.`, due to the lack of `usedforsecurity=False` for MD5 hashing. Previous PRs (#17043 and #15299) have fixed this. But some places still lack this parameter. https://github.com/vllm-project...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ated to #17031. When enabling `FIPS`, vLLM throws the error `ValueError: Model architectures ['OPTForCausalLM'] failed to be inspected. Please check the logs for more details.`, due to the lack of `usedforsecurity=False...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
