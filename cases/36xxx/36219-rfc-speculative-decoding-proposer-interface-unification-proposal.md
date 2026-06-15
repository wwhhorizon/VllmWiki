# vllm-project/vllm#36219: [RFC]: Speculative Decoding Proposer Interface Unification Proposal

| 字段 | 值 |
| --- | --- |
| Issue | [#36219](https://github.com/vllm-project/vllm/issues/36219) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Speculative Decoding Proposer Interface Unification Proposal

### Issue 正文摘录

### Motivation. The speculative decoding (spec decode) module in vLLM faces significant maintainability and extensibility challenges that hinder both upstream development and hardware plugin integrations. ## Current Problems #### 1. Inconsistent Proposer Interfaces Different speculative decoding algorithms implement vastly different interfaces, making it difficult for the model runner to interact with them uniformly: - **NgramProposer**: `propose(sampled_token_ids, num_tokens_no_spec, token_ids_cpu, slot_mappings=None)` - **SuffixDecodingProposer**: `propose(input_batch, sampled_token_ids, slot_mappings=None)` - **MedusaProposer**: `propose(target_hidden_states, sampling_metadata, slot_mappings=None)` - **EagleProposer**: Inherits from `SpecDecodeBaseProposer` - **DraftModelProposer**: Similar to EagleProposer but with different initialization Only Eagle and DraftModel proposers share a common base class (`SpecDecodeBaseProposer`), while others follow completely independent implementations. #### 2. Model Runner Coupling The `gpu_model_runner.py` contains extensive `if-else` branching to handle different speculation methods: ```python if spec_config.method == "ngram": draft_token_i...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: oposer**: `propose(sampled_token_ids, num_tokens_no_spec, token_ids_cpu, slot_mappings=None)` - **SuffixDecodingProposer**: `propose(input_batch, sampled_token_ids, slot_mappings=None)` - **MedusaProposer**: `propose(ta...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: Speculative Decoding Proposer Interface Unification Proposal RFC ### Motivation. The speculative decoding (spec decode) module in vLLM faces significant maintainability and extensibility challenges that hinder bo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ride class EagleProposer(BaseProposer): """Shared implementation for CUDA/ROCm""" pass class AscendEagleProposer(EagleProposer): """Ascend-specific overrides only where needed""" def prepare_inputs(self, ...): # Ascend-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ser_input: ProposerInput) -> ProposerOutput: pass # Hardware-specific implementations inherit and override class EagleProposer(BaseProposer): """Shared implementation for CUDA/ROCm""" pass class AscendEagleProposer(Eagl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ithms implement vastly different interfaces, making it difficult for the model runner to interact with them uniformly: - **NgramProposer**: `propose(sampled_token_ids, num_tokens_no_spec, token_ids_cpu, slot_mappings=No...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
