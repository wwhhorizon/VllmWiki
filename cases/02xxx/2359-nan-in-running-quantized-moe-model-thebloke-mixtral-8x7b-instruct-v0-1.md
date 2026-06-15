# vllm-project/vllm#2359: NaN in running quantized MoE model (TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ)

| 字段 | 值 |
| --- | --- |
| Issue | [#2359](https://github.com/vllm-project/vllm/issues/2359) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;quantization |
| 症状 | nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> NaN in running quantized MoE model (TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ)

### Issue 正文摘录

Hi vLLM team! I was testing vLLM 0.2.7 for serving Mixtral-8x7B-Instruct-v0.1-AWQ on an A100 40G. Here is my command: `python examples/llm_engine_example.py --model TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ --quantization awq --dtype half --enforce-eager --max-model-len 16` I observed that MixtralForCausalLM produces NaN: > MixtralForCausalLM sample hidden_states:tensor([[[nan, nan, nan, ..., nan, nan, nan], > [nan, nan, nan, ..., nan, nan, nan], > [nan, nan, nan, ..., nan, nan, nan], > ..., > [nan, nan, nan, ..., nan, nan, nan], > [nan, nan, nan, ..., nan, nan, nan], > [nan, nan, nan, ..., nan, nan, nan]]], device='cuda:0', > dtype=torch.float16) The above is printed (I added a print statement) on the hidden_states tensor in the MixtralForCausalLM sample function: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mixtral.py#L360 ```python def sample( self, hidden_states: Optional[torch.Tensor], sampling_metadata: SamplingMetadata, ) -> Optional[SamplerOutput]: print(f"MixtralForCausalLM sample hidden_states:{hidden_states}") next_tokens = self.sampler(self.lm_head.weight, hidden_states, sampling_metadata) return next_tokens ``` Is there a bug?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: NaN in running quantized MoE model (TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ) Hi vLLM team! I was testing vLLM 0.2.7 for serving Mixtral-8x7B-Instruct-v0.1-AWQ on an A100 40G. Here is my command: `python examples/llm_eng...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: was testing vLLM 0.2.7 for serving Mixtral-8x7B-Instruct-v0.1-AWQ on an A100 40G. Here is my command: `python examples/llm_engine_example.py --model TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ --quantization awq --dtype hal...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s model_support;moe;quantization cuda;moe;quantization nan_inf dtype;env_dependency Hi vLLM team!
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: self, hidden_states: Optional[torch.Tensor], sampling_metadata: SamplingMetadata, ) -> Optional[SamplerOutput]: print(f"MixtralForCausalLM sample hidden_states:{hidden_states}") next_tokens = self.sampler(self.lm_head.w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: NaN in running quantized MoE model (TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ) Hi vLLM team! I was testing vLLM 0.2.7 for serving Mixtral-8x7B-Instruct-v0.1-AWQ on an A100 40G. Here is my command: `python examples/llm_eng...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
